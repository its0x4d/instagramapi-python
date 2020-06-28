import json

from instapv.response.two_factor_info import TwoFactorResponse
from instapv.response.user_response import UserResponse

class PhoneVerificationSettingsResponse:

    def __init__(self, data: dict):
        # Return all data as_json
        self.as_json = data
        
        self.max_sms_count = data['max_sms_count'] if 'max_sms_count' in data else None
        self.resend_sms_delay_sec = data['resend_sms_delay_sec'] if 'resend_sms_delay_sec' in data else None
        self.robocall_count_down_time_sec = data['robocall_count_down_time_sec'] if 'robocall_count_down_time_sec' in data else False
        self.robocall_after_max_sms = data['robocall_after_max_sms'] if 'robocall_after_max_sms' in data else None

class LoginResponse:

    def __init__(self, data: dict):
        # Return all data as_json
        self.as_json = data
        
        self.message = data['message'] if 'message' in data else None
        self.status = data['status'] if 'status' in data else None
        self.two_factor_required = data['two_factor_required'] if 'two_factor_required' in data else False
        self.two_factor_info = TwoFactorResponse(data['two_factor_info']) if 'two_factor_info' in data else None
        self.phone_verification_settings = PhoneVerificationSettingsResponse(data['phone_verification_settings']) if 'phone_verification_settings' in data else None
        self.logged_in_user = UserResponse(data['logged_in_user']) if 'logged_in_user' in data else False