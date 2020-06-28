import json
from datetime import datetime

class Business:
    
    def __init__(self, bot):
        self.bot = bot

    def get_insights(self, day = None):
        """
        Get insights.
        :param = day(1-31)
        """
        if not day:
            day = datetime.now().day
        data = {
            'show_promotions_in_landing_page': 'true',
            'first': day
        }
        query = self.bot.request('insights/account_organic_insights/', get_params=data)
        return query
    
    def get_media_insights(self, media_id):
        data = {
            'ig_sig_key_version': self.bot.config.SIG_KEY_VERSION
        }
        query = self.bot.request(f'insights/media_organic_insights/{media_id}/', get_params=data)
        return query
    
    def get_statistics(self):
        _params = {
            'locale': self.bot.config.USER_AGENT_LOCALE,
            'vc_policy': 'insights_policy',
            'surface': 'account',
        }

        data = {
            'access_token': 'undefined',
            'fb_api_caller_class': 'RelayModern',
            'variables': json.dumps({
                'IgInsightsGridMediaImage_SIZE': 240,
                'timezone': 'Atlantic/Canary',
                'activityTab': True,
                'audienceTab': True,
                'contentTab': True,
                'query_params': json.dumps({
                    'access_token': '',
                    'id': self.bot.account_id
                }),
            }),
            'doc_id': '1926322010754880'
        }

        query = self.bot.request('ads/graphql/', get_params=_params, params=data, signed_post=False)
        return query