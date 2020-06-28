import json
from instapv.response.user_response import UserResponse

class UserFollowersResponse:

    def __init__(self, data: dict):
        self.as_json = data

        _new = []
        for i in data['users']:
            _new.append(
                UserResponse(i)
            )
        data.update({'users': _new})

        self.users = _new if 'users' in data else None
        self.status = data['status'] if 'status' in data else None
        self.sections = data['sections'] if 'sections' in data else None
        self.global_blacklist_sample = data['global_blacklist_sample'] if 'global_blacklist_sample' in data else None
        self.big_list = data['big_list'] if 'big_list' in data else None
        self.next_max_id = data['next_max_id'] if 'next_max_id' in data else None
        self.page_size = data['page_size'] if 'page_size' in data else None
        self.status = data['status'] if 'status' in data else None