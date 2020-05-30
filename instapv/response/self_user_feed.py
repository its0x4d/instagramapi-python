import json
from instapv.exceptions import UserNotFoundException


class SelfUserFeedResponse:
    
    def __init__(self, data):
        if data:
            self.pk = None
            self.username = None
            self.full_name = None
            self.profile_pic_url = None
            self.is_verified = None
            self.is_private = None
            self.has_anonymous_profile_picture = None
            self.can_boost_post = None
            self.can_see_organic_insights = None
            self.show_insights_terms = None
            self.reel_auto_archive = None
            self.is_unpublished = None
            self.latest_reel_media = None

            if type(data) == dict:
                if 'items' in data:
                    self.data = data['items'][0]['user']
                else:
                    self.data = data['user']
            # Check request status 
            if 'pk' in self.data:
                self.pk = self.data['pk']
            if 'username' in self.data:
                self.username = self.data['username']
            if 'full_name' in self.data:
                self.full_name = self.data['full_name']
            if 'is_private' in self.data:
                self.is_private = self.data['is_private']
            if 'profile_pic_url' in self.data:
                self.profile_pic_url = self.data['profile_pic_url']
            if 'is_verified' in self.data:
                self.is_verified = self.data['is_verified']
            if 'has_anonymous_profile_picture' in self.data:
                self.has_anonymous_profile_picture = self.data['has_anonymous_profile_picture']
            if 'can_boost_post' in self.data:
                self.can_boost_post = self.data['can_boost_post']
            if 'can_see_organic_insights' in self.data:
                self.can_see_organic_insights = self.data['can_see_organic_insights']
            if 'show_insights_terms' in self.data:
                self.show_insights_terms = self.data['show_insights_terms']
            if 'reel_auto_archive' in self.data:
                self.reel_auto_archive = self.data['reel_auto_archive']
            if 'is_unpublished' in self.data:
                self.is_unpublished = self.data['is_unpublished']
            if 'allowed_commenter_type' in self.data:
                self.allowed_commenter_type = self.data['allowed_commenter_type']
            if 'latest_reel_media' in self.data:
                self.latest_reel_media = self.data['latest_reel_media']