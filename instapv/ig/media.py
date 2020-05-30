import json
from instapv.response.media_info import MediaInfoResponse


class Media:

    def __init__(self, bot):
        self.bot = bot

    def info(self, media_id: str):
        query = self.bot.request(f'media/{media_id}/info/?')
        return MediaInfoResponse(query)

    def likers(self, media_id: str):
        query = self.bot.request(f'media/{media_id}/likers/?')
        return query

    def enable_comments(self, media_id):
        data = {
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid,
        }
        query = self.bot.request(f'media/{media_id}/enable_comments', params=data)
        return query

    def disable_comments(self, media_id):
        data = {
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'media_id': media_id
        }
        query = self.bot.request(f'media/{media_id}/disable_comments', params=data)
        return query

    def edit(self, media_id: str, caption_text):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'caption_text': caption_text
        }
        query = self.bot.request(f'media/{media_id}/edit_media/', params=data)

    def delete(self, media_id: str, media_type: str = 'PHOTO'):
        data = {
            'media_type': media_type,
            'igtv_feed_preview': False,
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'media_id': media_id
        }
        return self.bot.request(f'media/{media_id}/delete', params=data)

    def like(self, media_id: str):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'media_id': media_id
        }
        return self.bot.request(f'media/{media_id}/like/', params=data)

    def unlike(self, media_id: str):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'media_id': media_id
        }
        return self.bot.request(f'media/{media_id}/unlike/', params=data)

    def save(self, media_id: str):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'media_id': media_id
        }
        return self.bot.request(f'media/{media_id}/save/', params=data)

    def unsave(self, media_id: str):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'media_id': media_id
        }
        return self.bot.request(f'media/{media_id}/unsave/', params=data)

    def get_comments(self, media_id, max_id=''):
        data = {
            'can_support_threading': True,
            'max_id': max_id
        }
        query = self.bot.request(f'media/{media_id}/comments/', params=data)
        return query

    def get_comment_replais(self, media_id, comment_id):
        query = self.bot.request(
            f'media/{media_id}/comments/{comment_id}/inline_child_comments/')
        return query

    def delete_comment(self, media_id, comment_id):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token
        }
        query = self.bot.request(
            f'media/{media_id}/comment/{comment_id}/delete/', params=data)
        return query

    def code_to_media_id(self, short_code: str):
        media_id = 0
        for i in short_code:
            media_id = (media_id*64) + self.bot.config.ALPHABET.index(i)
        return media_id

    def media_id_to_code(self, media_id: int):
        short_code = ''
        while media_id > 0:
            remainder = media_id % 64
            media_id = (media_id-remainder)/64
            short_code = self.bot.config.ALPHABET[remainder] + short_code
        return short_code