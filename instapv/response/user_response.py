import json
from instapv.logger import Logger
from instapv.exceptions import UserNotFoundException

log = Logger()

class UserResponse(object):
    
    def __init__(self, data):
            if type(data) == dict:
                if 'items' in data:
                    data = data['items'][0]['user']
                elif 'user' in data:
                    data = data['user']
                else:
                    data = data
                        
                # Defualt data
                self.as_json = data
                self.biography = data['biography'] if 'biography' in data else None
                self.is_private = data['is_private'] if 'is_private' in data else None
                self.is_business = data['is_business'] if 'is_business' in data else None
                self.account_type = data['account_type'] if 'account_type' in data else None
                self.full_name = data['full_name'] if 'full_name' in data else None
                self.external_lynx_url = data['external_lynx_url'] if 'external_lynx_url' in data else None
                self.external_url = data['external_url'] if 'external_url' in data else None
                self.pk = data['pk'] if 'pk' in data else None
                self.follower_count = data['follower_count'] if 'follower_count' in data else None
                self.following_count = data['following_count'] if 'following_count' in data else None
                self.following_tag_count = data['following_tag_count'] if 'following_tag_count' in data else None
                self.mutual_followers_count = data['mutual_followers_count'] if 'mutual_followers_count' in data else None
                self.geo_media_count = data['geo_media_count'] if 'geo_media_count' in data else None
                self.has_anonymous_profile_picture = data['has_anonymous_profile_picture'] if 'has_anonymous_profile_picture' in data else None
                self.has_biography_translation = data['has_biography_translation'] if 'has_biography_translation' in data else None
                self.has_chaining = data['has_chaining'] if 'has_chaining' in data else None
                self.hd_profile_pic_url = data['hd_profile_pic_url'] if 'hd_profile_pic_url' in data else None
                self.is_favorite = data['is_favorite'] if 'is_favorite' in data else None
                self.is_verified = data['is_verified'] if 'is_verified' in data else None
                self.media_count = data['media_count'] if 'media_count' in data else None
                self.profile_context = data['profile_context'] if 'profile_context' in data else None
                self.profile_pic_url = data['profile_pic_url'] if 'profile_pic_url' in data else None
                self.total_igtv_videos = data['total_igtv_videos'] if 'total_igtv_videos' in data else None
                self.username = data['username'] if 'username' in data else None
                self.usertags_count = data['usertags_count'] if 'usertags_count' in data else None
                self.reel_auto_archive = data['reel_auto_archive'] if 'reel_auto_archive' in data else None
                self.allowed_commenter_type = data['allowed_commenter_type'] if 'allowed_commenter_type' in data else None
                self.professional_conversion_suggested_account_type = data['professional_conversion_suggested_account_type'] if 'professional_conversion_suggested_account_type' in data else None
                self.is_call_to_action_enabled = data['is_call_to_action_enabled'] if 'is_call_to_action_enabled' in data else None
                self.can_see_organic_insights = data['can_see_organic_insights'] if 'can_see_organic_insights' in data else None
                self.show_insights_terms = data['show_insights_terms'] if 'show_insights_terms' in data else None
                self.has_placed_orders = data['has_placed_orders'] if 'has_placed_orders' in data else None
                self.nametag = data['nametag'] if 'nametag' in data else None
                self.is_using_unified_inbox_for_direct = data['is_using_unified_inbox_for_direct'] if 'is_using_unified_inbox_for_direct' in data else None
                self.interop_messaging_user_fbid = data['interop_messaging_user_fbid'] if 'interop_messaging_user_fbid' in data else None
                self.can_see_primary_country_in_settings = data['can_see_primary_country_in_settings'] if 'can_see_primary_country_in_settings' in data else None
                self.allow_contacts_sync = data['allow_contacts_sync'] if 'allow_contacts_sync' in data else None
                self.phone_number = data['phone_number'] if 'phone_number' in data else None
            elif not data:
                raise UserNotFoundException('User not found')