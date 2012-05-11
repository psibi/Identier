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
        'url': 'statuses/show/{{id}}.json',
        'method': 'GET',
        },

    'updateStatus': {
        'url': 'statuses/update.json',
        'method': 'POST',
        },

    'destroyStatus': {
        'url': 'statuses/destroy/{{id}}.json',
        'method': 'POST'
        },

    'retweetStatus': {
        'url': 'statuses/retweet/{{id}}.json',
        'method': 'POST'
        },

    'getFriendsStatus': {
        'url': 'statuses/friends.json',
        'method': 'GET'
        },

    'getFollowersStatus': {
        'url': 'statuses/followers.json',
        'method': 'GET'
        },

    'getDirectMessages' : {
        'url': 'statuses/direct_messages.json',
        'method': 'GET'
        },

    'getSentMessages': {
        'url': '/direct_messages/sent.json',
        'method': 'GET',
        },

    'sendDirectMessage': {
        'url': '/direct_messages/new.json',
        'method': 'POST',
        },

    'createFriendship': {
        'url': '/friendships/create.json',
        'method': 'POST',
        },

    'destroyFriendship': {
        'url': '/friendships/destroy.json',
        'method': 'POST',
        },

    'checkIfFriendshipExists': {
        'url': '/friendships/exists.json',
        'method': 'GET',
        },

    'showFriendship': {
        'url': '/friendships/show.json',
        'method': 'GET',
        },

    'getFriendsIDs': {
        'url': '/friends/ids.json',
        'method': 'GET',
        },

    'getFollowersIDs': {
        'url': '/followers/ids.json',
        'method': 'GET',
        },

    'verifyCredentials': {
        'url': '/account/verify_credentials.json',
        'method': 'GET',
        },

    'getFavorites': {
        'url': '/favorites.json',
        'method': 'GET',
        },
    
    'createFavorite': {
        'url': '/favorites/create/{{id}}.json',
        'method': 'POST',
        },

    'destroyFavorite': {
        'url': '/favorites/destroy/{{id}}.json',
        'method': 'POST',
        },

    'createBlock': {
        'url': '/blocks/create/{{id}}.json',
        'method': 'POST',
        },

    'destroyBlock': {
        'url': '/blocks/destroy/{{id}}.json',
        'method': 'POST',
        },

    'showGroupTimeline': {
        'url': 'statusnet/groups/timeline.json',
        'method': 'GET',
        },

    'getGroupLists': {
        'url': 'statusnet/groups/list.json',
        'method': 'GET',
        },

    'createGroup': {
        'url': 'statusnet/groups/create.json',
        'method': 'POST',
        },

    'joinGroup': {
        'url': 'statusnet/groups/join.json',
        'method': 'POST',
        },

    'leaveGroup': {
        'url': 'statusnet/groups/leave.json',
        'method': 'POST',
        },

    'getAllList': {
        'url': 'statusnet/groups/list_all.json',
        'method': 'GET',
        },

    'getMembers': {
        'url': 'statusnet/groups/membership.json',
        'method': 'GET',
        },

    'isMember': {
        'url': 'statusnet/group/is_member.json',
        'method': 'GET',
        },

    'getTagTimeline': {
        'url': 'statusnet/tags/timeline.json',
        'method': 'GET',
        }
}


