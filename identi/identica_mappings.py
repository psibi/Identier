#!/usr/bin/python
#
# Copyright (C) 2012 Sibi <sibi@psibi.in>
#
# This file is part of Identity.
#
# Identity is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Identity is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Identity.  If not, see <http://www.gnu.org/licenses/>.
#
# Author:   Sibi <sibi@psibi.in>
#
# Reference: http://status.net/wiki/Twitter-compatible_API
#
base_url = 'http://identi.ca/api/'

api_table = {
    'getPublicTimeline': {
        'url': 'statuses/public_timeline.xml',
        'method': 'GET',
        },
    
    'getHomeTimeline': {
        'url': 'statuses/home_timeline.xml',
        'method': 'GET',
        },

    'getFriendsTimeline': {
        'url': 'statuses/friends_timeline.xml',
        'method': 'GET',
        },

    'getMentions': {
        'url': 'statuses/mentions.xml',
        'method': 'GET',
        },

    'getReplies': {
        'url': 'statuses/replies.xml',
        'method': 'GET',
        },

    'getUserTimeline': {
        'url': 'statuses/user_timeline.xml',
        'method': 'GET',
        },

    'getRetweetsOfMe': {
        'url': 'statuses/retweets_of_me.xml',
        'method': 'GET',
        },

    # Status resources 
    'showStatus': {
        'url': 'statuses/show/{{id}}.xml',
        'method': 'GET',
        },

    'updateStatus': {
        'url': 'statuses/update.xml',
        'method': 'POST',
        },

    'destroyStatus': {
        'url': 'statuses/destroy/{{id}}.xml',
        'method': 'POST'
        },

    'retweetStatus': {
        'url': 'statuses/retweet/{{id}}.xml',
        'method': 'POST'
        },

    'getFriendsStatus': {
        'url': 'statuses/friends.xml',
        'method': 'GET'
        },

    'getFollowersStatus': {
        'url': 'statuses/followers.xml',
        'method': 'GET'
        },

    'getDirectMessages' : {
        'url': 'statuses/direct_messages.xml',
        'method': 'GET'
        },

    'getSentMessages': {
        'url': '/direct_messages/sent.xml',
        'method': 'GET',
        },

    'sendDirectMessage': {
        'url': '/direct_messages/new.xml',
        'method': 'POST',
        },

    'createFriendship': {
        'url': '/friendships/create.xml',
        'method': 'POST',
        },

    'destroyFriendship': {
        'url': '/friendships/destroy.xml',
        'method': 'POST',
        },

    'checkIfFriendshipExists': {
        'url': '/friendships/exists.xml',
        'method': 'GET',
        },

    'showFriendship': {
        'url': '/friendships/show.xml',
        'method': 'GET',
        },

    'getFriendsIDs': {
        'url': '/friends/ids.xml',
        'method': 'GET',
        },

    'getFollowersIDs': {
        'url': '/followers/ids.xml',
        'method': 'GET',
        },

    'verifyCredentials': {
        'url': '/account/verify_credentials.xml',
        'method': 'GET',
        },

    'getFavorites': {
        'url': '/favorites.xml',
        'method': 'GET',
        },
    
    'createFavorite': {
        'url': '/favorites/create/{{id}}.xml',
        'method': 'POST',
        },

    'destroyFavorite': {
        'url': '/favorites/destroy/{{id}}.xml',
        'method': 'POST',
        },

    'createBlock': {
        'url': '/blocks/create/{{id}}.xml',
        'method': 'POST',
        },

    'destroyBlock': {
        'url': '/blocks/destroy/{{id}}.xml',
        'method': 'POST',
        },

    'showGroupTimeline': {
        'url': 'statusnet/groups/timeline.xml',
        'method': 'GET',
        },

    'getGroupLists': {
        'url': 'statusnet/groups/list.xml',
        'method': 'GET',
        },

    'createGroup': {
        'url': 'statusnet/groups/create.xml',
        'method': 'POST',
        },

    'joinGroup': {
        'url': 'statusnet/groups/join.xml',
        'method': 'POST',
        },

    'leaveGroup': {
        'url': 'statusnet/groups/leave.xml',
        'method': 'POST',
        },

    'getAllList': {
        'url': 'statusnet/groups/list_all.xml',
        'method': 'GET',
        },

    'getMembers': {
        'url': 'statusnet/groups/membership.xml',
        'method': 'GET',
        },

    'isMember': {
        'url': 'statusnet/group/is_member.xml',
        'method': 'GET',
        },

    'getTagTimeline': {
        'url': 'statusnet/tags/timeline.xml',
        'method': 'GET',
        }
}


