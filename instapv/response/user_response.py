import json
from instapv.logger import Logger
from instapv.exceptions import UserNotFoundException

log = Logger()

class UserResponse(object):
    
    def __init__(self, data):
            if type(data) == dict:
                if 'items' in data:
                    data = data['items'][0]['user']
                else:
                    data = data['user']
                        
                # Defualt data
                self.as_json = data
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
                self.reel_auto_archive = None
                self.allowed_commenter_type = None

                if 'is_private' in data:
                    self.is_private = data['is_private']
                if 'pk' in data:
                    self.pk = data['pk']
                if 'full_name' in data:
                    self.full_name = data['full_name']
                if 'profile_pic_url' in data:
                    self.profile_pic_url = data['profile_pic_url']
                if 'username' in data:
                    self.username = data['username']
                if 'is_verified' in data:
                    self.is_verified = data['is_verified']
                if 'has_anonymous_profile_picture' in data:
                    self.has_anonymous_profile_picture = data['has_anonymous_profile_picture']
                if 'media_count' in data:
                    self.media_count = data['media_count']
                if 'geo_media_count' in data:
                    self.geo_media_count = data['geo_media_count']
                if 'follower_count' in data:
                    self.follower_count = data['follower_count']
                if 'following_count' in data:
                    self.following_count = data['following_count']
                if 'following_tag_count' in data:
                    self.following_tag_count = data['following_tag_count']
                if 'biography' in data:
                    self.biography = data['biography']
                if 'external_url' in data:
                    self.external_url = data['external_url']
                if 'external_lynx_url' in data:
                    self.external_lynx_url = data['external_lynx_url']
                if 'has_biography_translation' in data:
                    self.has_biography_translation = data['has_biography_translation']
                if 'total_igtv_videos' in data:
                    self.total_igtv_videos = data['total_igtv_videos']
                if 'usertags_count' in data:
                    self.usertags_count = data['usertags_count']
                if 'is_favorite' in data:
                    self.is_favorite = data['is_favorite']
                if 'has_chaining' in data:
                    self.has_chaining = data['has_chaining']
                if 'hd_profile_pic_url' in data:
                    self.hd_profile_pic_url = data['hd_profile_pic_versions'][0]['url']
                if 'mutual_followers_count' in data:
                    self.mutual_followers_count = data['mutual_followers_count']
                if 'profile_context' in data:
                    self.profile_context = data['profile_context']
                if 'is_business' in data:
                    self.is_business = data['is_business']
                if 'account_type' in data:
                    self.account_type = data['account_type']
                if 'reel_auto_archive' in data:
                    self.reel_auto_archive = data['reel_auto_archive']
                if 'allowed_commenter_type' in data:
                    self.allowed_commenter_type = data['allowed_commenter_type']
                if 'status' in data:
                    self.status = data['status']
            elif not data:
                raise UserNotFoundException('User not found')