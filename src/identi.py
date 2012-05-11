import requests
import urllib
from identica_mappings import base_url, api_table
from oauth_hook import OAuthHook
from error import IdentiError

class Identi:
    def __init__(self,identi_token=None,identi_secret=None,oauth_token=None,oauth_secret=None,callback_url=None,header=None):
        # Needed for hitting that there API.
        self.request_token_url = 'https://identi.ca/api/oauth/request_token'
        self.access_token_url = 'https://identi.ca/api/oauth/access_token'
        self.authorize_url = 'https://identi.ca/api/oauth/authorize' #This is not used up.
        self.authenticate_url = 'https://twitter.com/oauth/authenticate' #This is also not used up.
        
        self.identi_token = identi_token
        self.identi_secret = identi_secret
        self.oauth_token = oauth_token
        self.oauth_secret = oauth_secret
        self.callback_url = callback_url
        
        OAuthHook.consumer_key = self.identi_token
        OAuthHook.consumer_secret = self.identi_secret
        oauth_hook = OAuthHook(self.oauth_token,self.oauth_secret)
        self.headers = header
        if self.headers is None:
            self.headers = { 'User-agent': 'Identi.ca Python Library' }

        self.client = None

        if self.identi_token is not None and self.identi_secret is not None:
            self.client = requests.session(hooks={'pre_request': oauth_hook})

        if self.oauth_token is not None and self.oauth_secret is not None:
            self.oauth_hook = OAuthHook(self.oauth_token, self.oauth_secret)
            self.client = requests.session(hooks={'pre_request': self.oauth_hook})
        
        if self.client is None:
            self.client = requests.session()

        def setFunc(key):
            return lambda **kwargs: self._constructFunc(key, **kwargs)
        for key in api_table.keys():
            self.__dict__[key] = setFunc(key)

    def _constructFunc(self,api_call, **kwargs):
        fn = api_table[api_call]
        url = base_url + fn['url']
        method = fn['method'].lower()
        if not method in ('get', 'post'):
            print "error"
        
        content = self._request(url,method = method, params=kwargs)
        return content

    def _request(self,url,method = 'GET', params=None, api_call=None):
        myargs = {}
        method = method.lower()

        if method == 'get':
            url = '%s?%s' % (url,urllib.urlencode(params))
        else:
            myargs = params

        func = getattr(self.client,method)
        response = func(url, data=myargs)
        content = response.content.decode('utf-8')
        print content
        return content

  def get_authentication_tokens(self):
        """
            get_auth_url(self)

            Returns an authorization URL for a user to hit.
        """
        callback_url = self.callback_url

        request_args = {}
        if callback_url:
            request_args['oauth_callback'] = callback_url

        method = 'get'

        func = getattr(self.client, method)
        response = func(self.request_token_url, data=request_args)

        if response.status_code != 200:
            raise IdentiError("Seems something couldn't be verified with OAuth")

        request_tokens = dict(parse_qsl(response.content))
        if not request_tokens:
            raise IdentiError('Unable to decode request tokens.')

        oauth_callback_confirmed = request_tokens.get('oauth_callback_confirmed') == 'true'

        auth_url_params = {
            'oauth_token': request_tokens['oauth_token'],
        }

        # Use old-style callback argument if server didn't accept new-style
        if callback_url and not oauth_callback_confirmed:
            auth_url_params['oauth_callback'] = callback_url

        request_tokens['auth_url'] = self.authenticate_url + '?' + urllib.urlencode(auth_url_params)

        return request_tokens

    def get_authorized_tokens(self):
        """
            get_authorized_tokens

            Returns authorized tokens after they go through the auth_url phase.
        """
        response = self.client.get(self.access_token_url)
        authorized_tokens = dict(parse_qsl(response.content))
        if not authorized_tokens:
            raise IdentiError('Unable to decode authorized tokens.')
        
        return authorized_tokens


if __name__=="__main__":
    #idc = Identi()
    #user_timeline = idc.updateStatus(status="Test Message #test")
    #group_timeline = idc.getGroupLists(id='psibi')
    pass


