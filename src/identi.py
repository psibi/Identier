import requests
import urllib
from identica_mappings import base_url, api_table

class Identi:
    def __init__(self,header=None):
        self.headers = header
        if self.headers is None:
            self.headers = { 'User-agent': 'Identi.ca Python Library' }

        self.client = None
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
        if not method in ('get', 'post', 'delete'):
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

    def get(self,endpoint,params = None):
        params = params or {}
        return self.request(endpoint,params)

    def post(self,endpoint,params=None):
        params = params or {}
        return self.request(endpoint,params)

if __name__=="__main__":
    idc = Identi()
    idc.getPublicTimeline()
