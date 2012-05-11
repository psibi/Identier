#
#Reference: http://status.net/wiki/Twitter-compatible_API
#
base_url = 'http://identi.ca/api/'

api_table = {
    'getPublicTimeline': {
        'url': 'statuses/public_timeline.json',
        'method': 'GET',
        },
    
    'getHomeTimeline': {
        'url': 'statuses/home_timeline.json',
        'method': 'GET',
        },

    'getFriendsTimeline': {
        'url': 'statuses/friends_timeline.json',
        'method': 'GET',
        },

    'getMentions': {
        'url': 'statuses/mentions.json',
        'method': 'GET',
        },

    'getReplies': {
        'url': 'statuses/replies.json',
        'method': 'GET',
        },

    'getUserTimeline': {
        'url': 'statuses/user_timeline.json',
        'method': 'GET',
        },

    'getRetweetsOfMe': {
        'url': 'statuses/retweets_of_me.json',
        'method': 'GET',
        },

    # Status resources 
    'showStatus': {
        'url': '/statuses/show/{{id}}.json',
        'method': 'GET',
        },

    'updateStatus': {
        'url': '/statuses/update.json',
        'method': 'POST',
        },

    'destroyStatus': {
        'url': '/statuses/destroy/{{id}}.json',
        'method': 'POST'
        },

    'retweetStatus': {
        'url': '/statuses/retweet/{{id}}.json',
        'method': 'POST'
        }
}


