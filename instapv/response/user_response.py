import json
from instapv.logger import Logger
from instapv.exceptions import UserNotFoundException

log = Logger()

class UserResponse(object):
    
    def __init__(self, data):
        try:
            self.data = data
            if type(data) == dict:
                if data['status'] == 'ok':
                    if 'items' in data:
                        self.data = data['items'][0]['user']
                    else:
                        self.data = data['user']
                    # Defualt data
                    self.biography = None
                    self.is_private = None
                    self.is_business = None
                    self.account_type = None
                    self.full_name = None
                    self.external_lynx_url = None
                    self.external_url = None
                    self.pk = None
                    self.follower_count = None
                    self.following_count = None
                    self.following_tag_count = None
                    self.mutual_followers_count = None
                    self.full_name = None
                    self.geo_media_count = None
                    self.has_anonymous_profile_picture = None
                    self.has_biography_translation = None
                    self.has_chaining = None
                    self.hd_profile_pic_url = None
                    self.is_favorite = None
                    self.is_verified = None
                    self.media_count = None
                    self.profile_context = None
                    self.profile_pic_url = None
                    self.total_igtv_videos = None
                    self.username = None
                    self.usertags_count = None

                    if 'is_private' in self.data:
                        self.is_private = self.data['is_private']
                    if 'pk' in self.data:
                        self.pk = self.data['pk']
                    if 'full_name' in self.data:
                        self.full_name = self.data['full_name']
                    if 'profile_pic_url' in self.data:
                        self.profile_pic_url = self.data['profile_pic_url']
                    if 'username' in self.data:
                        self.username = self.data['username']
                    if 'is_verified' in self.data:
                        self.is_verified = self.data['is_verified']
                    if 'has_anonymous_profile_picture' in self.data:
                        self.has_anonymous_profile_picture = self.data['has_anonymous_profile_picture']
                    if 'media_count' in self.data:
                        self.media_count = self.data['media_count']
                    if 'geo_media_count' in self.data:
                        self.geo_media_count = self.data['geo_media_count']
                    if 'follower_count' in self.data:
                        self.follower_count = self.data['follower_count']
                    if 'following_count' in self.data:
                        self.following_count = self.data['following_count']
                    if 'following_tag_count' in self.data:
                        self.following_tag_count = self.data['following_tag_count']
                    if 'biography' in self.data:
                        self.biography = self.data['biography']
                    if 'external_url' in self.data:
                        self.external_url = self.data['external_url']
                    if 'external_lynx_url' in self.data:
                        self.external_lynx_url = self.data['external_lynx_url']
                    if 'has_biography_translation' in self.data:
                        self.has_biography_translation = self.data['has_biography_translation']
                    if 'total_igtv_videos' in self.data:
                        self.total_igtv_videos = self.data['total_igtv_videos']
                    if 'usertags_count' in self.data:
                        self.usertags_count = self.data['usertags_count']
                    if 'is_favorite' in self.data:
                        self.is_favorite = self.data['is_favorite']
                    if 'has_chaining' in self.data:
                        self.has_chaining = self.data['has_chaining']
                    if 'hd_profile_pic_url' in self.data:
                        self.hd_profile_pic_url = self.data['hd_profile_pic_versions'][0]['url']
                    if 'mutual_followers_count' in self.data:
                        self.mutual_followers_count = self.data['mutual_followers_count']
                    if 'profile_context' in self.data:
                        self.profile_context = self.data['profile_context']
                    if 'is_business' in self.data:
                        self.is_business = self.data['is_business']
                    if 'account_type' in self.data:
                        self.account_type = self.data['account_type']
                    if 'status' in self.data:
                        self.status = self.data['status']
                else:
                    raise UserNotFoundException('User not found')
            elif not data:
                print(data)
                raise UserNotFoundException('User not found')
        except KeyError as e:
            log.error(f'ERROR: {e}')
            pass