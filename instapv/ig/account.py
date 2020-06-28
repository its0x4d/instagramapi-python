import json
from datetime import datetime

from instapv.response.self_user_feed import SelfUserFeedResponse
from instapv.response.generic import GenericResponse
from instapv.exceptions import InternalException

class Account:

    def __init__(self, bot):
        self.bot = bot

    def set_private(self):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request('accounts/set_private/', data)
        return GenericResponse(query)

    def set_public(self):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request('accounts/set_public/', data)
        return GenericResponse(query)

    def get_current_user(self):
        query = self.bot.request('accounts/current_user/?edit=true')
        return SelfUserFeedResponse(query)

    def set_biography(self, biography: str):
        if not isinstance(biography, str) or len(biography) > 150:
            raise Exception('Please provide a 0 to 150 character string as biography.')
        else:
            data = {
                'raw_text': biography,
                '_uuid': self.bot.uuid,
                '_uid': self.bot.account_id,
                'device_id': self.bot.device_id,
                '_csrftoken': self.bot.token
            }
            query = self.bot.request('accounts/set_biography/', params=data)
            return query
    
    def set_gender(self, gender: str = ''):
        switcher = { 
            "male": 1, 
            "female": 2, 
            " ": 3 
        }
        gender_id = switcher.get(gender, 4)
        custom_gender = gender if gender_id == 4 else '' 
        data = {
            'gender': gender_id,
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid,
            'custom_gender': custom_gender
        }
        query = self.bot.request('accounts/set_gender/', params=data, signed_post=False)
        return query

    def edit_profile(self, url: str, phone_number: str, name: str, biography: str, email: str, gender: str, new_username = None):
        user_respone = self.get_current_user()
        current_user = user_respone
        if not current_user or not isinstance(current_user.username, str):
            raise InternalException('Unable to find current account username while preparing profile edit.')
        
        old_username = current_user.username
        if isinstance(new_username, str) and len(new_username) > 0:
            username = new_username
        else:
            username = old_username

        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'external_url': url,
            'phone_number': phone_number,
            'username': username,
            'first_name': name,
            'biography': biography,
            'email': email,
            'gender': gender,
            'device_id': self.bot.device_id
        }
        query = self.bot.request('accounts/edit_profile/', params=data)
        return query


    def change_profile_picture(self, photo_filename):
        """
        TODO: FIX FILE UPLOAD
        """
        data = {
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
        }
        _photo = {
            'profile_pic': (photo_filename, open(photo_filename, 'rb'), 'application/octet-stream')
        }
        query = self.bot.request('accounts/change_profile_picture/', params=data, files=_photo, signed_post=False)
        return query
    
    def remove_profile_picture(self):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request('accounts/remove_profile_picture/', params=data)
        return query

    def switch_to_business_profile(self):
        """
        Switches your account to business profile.
        In order to switch your account to Business profile you MUST call self.set_business_info
        """
        return self.bot.request('business_conversion/get_business_convert_social_context/')

    def switch_to_personal_profile(self):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request('accounts/convert_to_personal/', params=data)
        return query
    
    def set_business_info(self, phone_number, email, category_id):
        data = {
            'set_public': 'true',
            'entry_point': 'setting',
            'public_phone_contact': json.dumps({
                'public_phone_number': phone_number,
                'business_contact_method': 'CALL'
            }),
            'public_email': email,
            'category_id': category_id,
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request('accounts/create_business_info/', params=data)
        return query

    def check_username(self, username):
        data = {
            '_uuid': self.bot.uuid,
            'username': username,
            '_csrftoken': self.bot.token,
            '_uid': self.bot.account_id,
        }
        query = self.bot.request('users/check_username/', params=data)
        return query

    def get_comment_filter(self):
        return self.bot.request('accounts/get_comment_filter/')
    
    def set_comment_filter(self, config_value: int):
        if not isinstance(config_value, int):
            raise ValueError('config_value must be 1 for on or 0 for off.')
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'config_value': config_value,
        }
        query = self.bot.request('accounts/set_comment_filter/', params=data)
        return query
    
    def get_comment_category_filter_disabled(self):
        return self.bot.request('accounts/get_comment_category_filter_disabled/')
    
    def get_comment_filter_keywords(self):
        return self.bot.request('accounts/get_comment_filter_keywords/')
    
    def set_comment_filter_keywords(self, keywords: list):
        if not isinstance(keywords, list):
            raise ValueError('Keywords must be instance of list')
        keywords = ','.join(keywords)
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'keywords': keywords,
        }
        query = self.bot.request('accounts/set_comment_filter_keywords/', params=data)
        return query

    def change_password(self, old_password, new_password):
        """
        WARRNING: You should call bot.login(relogin=True) to relogin with new password!
        """
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'old_password': old_password,
            'new_password1': new_password,
            'new_password2': new_password,
        }
        query = self.bot.request('accounts/change_password/', params=data)
        return query
    
    def get_security_info(self):
        """
        WARNING: STORE AND KEEP BACKUP CODES IN A SAFE PLACE. THEY ARE EXTREMELY
        IMPORTANT! YOU WILL GET THE CODES IN THE RESPONSE. THE BACKUP
        CODES LET YOU REGAIN CONTROL OF YOUR ACCOUNT IF YOU LOSE THE
        PHONE NUMBER! WITHOUT THE CODES, YOU RISK LOSING YOUR ACCOUNT!
        """
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request('accounts/account_security_info/', params=data)
        return query
    
    def send_two_factor_enable_sms(self, phone_number: str):
        clean_number = phone_number.replace(r"[^0-9]", "")
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'device_id': self.bot.device_id,
            'phone_number': clean_number
        }
        query = self.bot.request('accounts/send_two_factor_enable_sms/', params=data)
        return query

    def enable_sms_two_factor(self, phone_number: str, verification_code):
        clean_number = phone_number.replace(r"[^0-9]", "")
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'device_id': self.bot.device_id,
            'phone_number': clean_number,
            'verification_code': verification_code
        }
        query = self.bot.request('accounts/enable_sms_two_factor/', params=data)
        return query
    
    def disable_sms_two_factor(self):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request('accounts/disable_sms_two_factor/', params=data)
        return query
    
    def get_presence_status(self):
        return self.bot.request('accounts/get_presence_disabled/')
    
    def enable_presence(self):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'disabled': '0',
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request('accounts/set_presence_disabled/', params=data)
        return query
    
    def disable_presence(self):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'disabled': '1',
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request('accounts/set_presence_disabled/', params=data)
        return query
    
    def send_confirm_email(self):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'send_source': 'edit_profile',
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request('accounts/send_confirm_email/', params=data)
        return query
    
    def send_sms_code(self, phone_number: str):
        clean_number = phone_number.replace(r"[^0-9]", "")
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'phone_number': clean_number,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request('accounts/send_sms_code/', params=data)
        return query
    
    def verify_sms_code(self, phone_number: str, verification_code):
        clean_number = phone_number.replace(r"[^0-9]", "")
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'phone_number': clean_number,
            'verification_code': verification_code
        }
        query = self.bot.request('accounts/verify_sms_code/', params=data)
        return query
    
    def set_contact_point_prefill(self, usage):
        data = {
            'phone_id': self.bot.phone_id,
            '_csrftoken': self.bot.token,
            'usage': usage,
        }
        query = self.bot.request('accounts/contact_point_prefill/', params=data)
        return query
    
    def get_badge_notifications(self):
        data = {
            '_uuid': self.bot.phone_id,
            '_csrftoken': self.bot.token,
            'user_ids': self.bot.account_id,
            'phone_id': self.bot.phone_id,
        }
        query = self.bot.request('notifications/badge/', params=data, signed_post=False)
        return query
    
    def get_process_contact_point_signals(self):
        data = {
            'google_tokens': '[]',
            'phone_id': self.bot.token,
            '_uid': self.bot.account_id,
            '_uuid': self.bot.uuid,
            'device_id': self.bot.device_id,
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request('accounts/process_contact_point_signals/', params=data)
        return query
    
    def get_prefill_candidates(self):
        data = {
            'android_device_id': self.bot.device_id,
            'device_id': self.bot.uuid,
            'usages': '["account_recovery_omnibox"]',
        }
        query = self.bot.request('accounts/get_prefill_candidates/', params=data)
        return query
    
    def get_account_family(self):
        return self.bot.request('multiple_accounts/get_account_family/')
    
    def get_linkage_status(self):
        return self.bot.request('linked_accounts/get_linkage_status/')
