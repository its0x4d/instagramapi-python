import json
from instapv.response.user_response import UserResponse
from instapv.response.friendship import FriendShipResponse
from instapv.response.self_user_feed import SelfUserFeedResponse

class User:

    def __init__(self, bot):
        self.bot = bot

    def get_user_feed(self, user_id: str, max_id: str = None, timestamp: str = None):
        data = {
            'max_id': max_id,
            'min_timestamp': timestamp,
            'rank_token': self.bot.tools.generate_uuid(True),
            'ranked_token': 'true'
        }

        query = self.bot.request('feed/user/%s/' % (user_id), params=data)
        return UserResponse(query)

    def get_self_user_feed(self, max_id: str = None, timestamp: str = None):
        data = {
            'max_id': max_id,
            'min_timestamp': timestamp,
            'rank_token': self.bot.tools.generate_uuid(True),
            'ranked_token': 'true'
        }

        query = self.bot.request(
            f'feed/user/{self.bot.account_id}/', params=data)
        return SelfUserFeedResponse(query)

    def get_info_by_name(self, username):
        query = self.bot.request(f'users/{username}/usernameinfo/')
        return UserResponse(query)

    def set_private(self, private=False):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request('accounts/set_private/')
        if query['status'] == 'ok':
            return True
        else:
            return False

    def set_public(self):
        query = self.bot.request('accounts/set_public/')
        if query['status'] == 'ok':
            return True
        else:
            return False

    def follow_request_approve(self, user_id):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'user_id': user_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request(
            'friendships/approve/' + str(user_id) + '/', params=True, signed_post=True)
        return FriendShipResponse(query)

    def follow_request_ignore(self, user_id):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'user_id': user_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request(
            'friendships/ignore/' + str(user_id) + '/', params=True, signed_post=True)
        return FriendShipResponse(query)

    def follow(self, user_id, media_id=None):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'user_id': user_id,
            'radio_type': 'wifi-none',
            'device_id': self.bot.device_id
        }
        if media_id:
            data.update({'media_id_attribution': media_id})
        query = self.bot.request(
            'friendships/create/' + str(user_id) + '/', params=True, signed_post=True)
        return FriendShipResponse(query)

    def unfollow(self, user_id):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'user_id': user_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request(
            'friendships/destroy/' + str(user_id) + '/', params=True, signed_post=True)
        return FriendShipResponse(query)

    def block(self, user_id):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'user_id': user_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request(
            'friendships/block/' + str(user_id) + '/', params=True, signed_post=True)
        return FriendShipResponse(query)

    def unblock(self, user_id):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'user_id': user_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request(
            'friendships/unblock/' + str(user_id) + '/', params=True, signed_post=True)
        return FriendShipResponse(query)

    def get_user_followers(self, user_id, max_id: str = None):
        if max_id == None:
            query = self.bot.request('friendships/' + str(user_id) +
                                     '/followers/?rank_token=' + self.bot.tools.generate_uuid(True))
            return UserResponse(query['users'])
        else:
            query = self.bot.request('friendships/' + str(user_id) + '/followers/?rank_token=' +
                                     self.bot.tools.generate_uuid(True) + '&max_id=' + str(max_id))
            return UserResponse(query['users'])

    def get_pending_follow_requests(self):
        query = self.bot.request('friendships/pending?')
        return UserResponse(query)

    def get_user_following(self, user_id, max_id: str = None):
        if max_id == None:
            query = self.bot.request('friendships/' + str(user_id) +
                                     '/following/?rank_token=' + self.bot.tools.generate_uuid(True))
            return UserResponse(query['users'])
        else:
            query = self.bot.request('friendships/' + str(user_id) + '/following/?rank_token=' +
                                     self.bot.tools.generate_uuid(True) + '&max_id=' + str(max_id))
            return UserResponse(query['users'])

    def get_all_followers(self, user_id):
        followers = []
        next_max_id: str = None
        while 1:
            self.get_user_followers(user_id, next_max_id)
            temp = self.bot.last_json_response

            for item in temp["users"]:
                followers.append(item)

            if temp["big_list"] is False:
                return followers
            next_max_id = temp["next_max_id"]
