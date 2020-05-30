import json
from datetime import datetime

from ..response.live_info import LiveInfoResponse


class Live:

    def __init__(self, bot):
        self.bot = bot

    def create(self, preview_height: int = 1080, preview_width: int = 1920):
        data = {
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid,
            'preview_height': preview_height,
            'preview_width': preview_width,
            'broadcast_type': 'RTMP_SWAP_ENABLED',
            'internal_only': 0
        }
        query = self.bot.request(
            'live/create/', params=data, signed_post=False)
        return LiveInfoResponse(query)

    def start(self, boardcast_id: int):
        data = {
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid
        }
        query = self.bot.request(
            f'live/{boardcast_id}/start/', params=data, signed_post=False)
        return query

    def end(self, boardcast_id: int, copyright_warning: bool = False):
        data = {
            '_uid': self.bot.account_id,
            '_uuid': self.bot.uuid,
            '_csrftoken': self.bot.token,
            'end_after_copyright_warning': copyright_warning
        }
        query = self.bot.request(
            f'live/{boardcast_id}/end_broadcast/', params=data)
        return query

    def save_live(self, boardcast_id: int):
        data = {
            '_uid': self.bot.account_id,
            '_uuid': self.bot.uuid,
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request(
            f'live/{boardcast_id}/add_to_post_live/', params=data)
        return query

    def get_post_live_likes(self, boardcast_id: int, starting_offset: int = 0, encoding_tag: str = 'instagram_dash_remuxed'):
        data = {
            'starting_offset': starting_offset,
            'encoding_tag': encoding_tag,
        }
        query = self.bot.request(
            f'live/{boardcast_id}/get_post_live_likes/')
        return query
    
    def get_like_count(self, boardcast_id: int, like_ts: int = 0):
        data = {
            'like_ts': like_ts,
        }
        query = self.bot.request(
            f'live/{boardcast_id}/get_like_count/', params=data)
        return query
    
    def get_comments(self, boardcast_id: int, last_comment_ts: int = 0):
        data = {
            'last_comment_ts': last_comment_ts,
        }
        query = self.bot.request(
            f'live/{boardcast_id}/get_comment/', params=data, signed_post=True)
        return query

    def enable_comments(self, boardcast_id: int):
        data = {
            '_uid': self.bot.account_id,
            '_uuid': self.bot.uuid,
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request(
            f'live/{boardcast_id}/unmute_comment/', params=data)
        return query
    
    def disable_comments(self, boardcast_id: int):
        data = {
            '_uid': self.bot.account_id,
            '_uuid': self.bot.uuid,
            '_csrftoken': self.bot.token,
        }
        query = self.bot.request(
            f'live/{boardcast_id}/mute_comment/', params=data)
        return query
        
    def get_live_info(self, boardcast_id: int):
        query = self.bot.request(
            f'live/{boardcast_id}/info/')
        return query