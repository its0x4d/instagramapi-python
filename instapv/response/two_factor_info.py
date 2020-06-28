import json

class TwoFactorResponse:

    def __init__(self, data: dict):
        # Return all data as_json
        self.as_json = data
        
        self.username = data['username'] if 'username' in data else None
        self.sms_two_factor_on = data['sms_two_factor_on'] if 'sms_two_factor_on' in data else None
        self.totp_two_factor_on = data['totp_two_factor_on'] if 'totp_two_factor_on' in data else None
        self.obfuscated_phone_number = data['obfuscated_phone_number'] if 'obfuscated_phone_number' in data else None
        self.two_factor_identifier = data['two_factor_identifier'] if 'two_factor_identifier' in data else None
        self.show_messenger_code_option = data['show_messenger_code_option'] if 'show_messenger_code_option' in data else None
        self.show_new_login_screen = data['show_new_login_screen'] if 'show_new_login_screen' in data else None
        self.show_trusted_device_option = data['show_trusted_device_option'] if 'show_trusted_device_option' in data else None