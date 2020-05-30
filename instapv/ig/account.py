import json
from datetime import datetime


class Account:

    def __init__(self, bot):
        self.bot = bot

    def get_current_user(self):
        query = self.bot.request('accounts/current_user/?edit=true')
        return query

    def set_gender(self, biography: str):
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
            print(data)
            query = self.bot.request('accounts/set_gender/', params=data)
            return query
