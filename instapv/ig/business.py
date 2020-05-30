import json
from datetime import datetime

class Business:
    
    def __init__(self, bot):
        self.bot = bot

    def get_insights(self, media_id: str):
        query = self.bot.request(f'insights/media_organic_insights/{media_id}/')
        return query