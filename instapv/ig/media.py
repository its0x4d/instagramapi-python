import json
from instapv.response.media_info import MediaInfoResponse
from instapv.response.send_comment import SendCommentInfoResponse
from instapv.response.generic import GenericResponse
from instapv.response.comments import MediaCommentsResponse
from requests_toolbelt import MultipartEncoder
from time import time

# Fix Python3 Import Error.
try:
    from ImageUtils import getImageSize
except:
    from instapv.utils.ImageUtils import getImageSize


class Media:

    def __init__(self, bot):
        self.bot = bot

    def info(self, media_id: str):
        query = self.bot.request(f'media/{media_id}/info/?')
        return MediaInfoResponse(query)

    def likers(self, media_id: str):
        query = self.bot.request(f'media/{media_id}/likers/?')
        return query

    def comment(self, media_id, comment_text, reply_comment_id = None, module = 'comments_v2', carousel_index = 0, feed_position = 0, feed_bumped = False):
        data = {
            'user_breadcrumb': comment_text,
            'idempotence_token': self.bot.tools.generate_uuid(True),
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'comment_text': comment_text,
            'container_module': module,
            'radio_type': 'wifi-none',
            'device_id': self.bot.device_id,
            'carousel_index': carousel_index,
            'feed_position': feed_position,
            'is_carousel_bumped_post': feed_bumped
        }
        if reply_comment_id != None:
            data.update({
                'replied_to_comment_id': reply_comment_id
            })
        
        query = self.bot.request(f'media/{media_id}/comment/', params=data, signed_post=False)
        return SendCommentInfoResponse(query)

    def get_comment_infos(self, media_ids):
        if isinstance(media_ids, list):
            media_ids = ','.join(media_ids)

        query = self.bot.request(f'media/comment_infos?media_ids={media_ids}')
        return query

    def delete_comment(self, media_id, comment_id):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            
        }
        query = self.bot.request(f'media/{media_id}/comment/{comment_id}/delete/', params=data, signed_post=False)
        return query

    def enable_comments(self, media_id):
        data = {
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid,
        }
        query = self.bot.request(
            f'media/{media_id}/enable_comments/', params=data, signed_post=False)
        return query

    def disable_comments(self, media_id):
        data = {
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid,
        }
        query = self.bot.request(
            f'media/{media_id}/disable_comments/', params=data, signed_post=False)
        return query

    def edit(self, media_id: str, caption_text):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'caption_text': caption_text
        }
        query = self.bot.request(f'media/{media_id}_{self.bot.account_id}/edit_media/', params=data)
        return query

    def delete(self, media_id: str, media_type: str = 'PHOTO'):
        data = {
            'media_type': media_type,
            'igtv_feed_preview': False,
            '_csrftoken': self.bot.token,
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            'media_id': media_id
        }
        return self.bot.request(f'media/{media_id}/delete/', params=data)

    def like(self, media_id: str):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'media_id': media_id
        }
        query = self.bot.request(f'media/{media_id}/like/', params=data)
        return GenericResponse(query)

    def unlike(self, media_id: str):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'media_id': media_id
        }
        query = self.bot.request(f'media/{media_id}/unlike/', params=data)
        return GenericResponse(query)

    def save(self, media_id: str):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'media_id': media_id
        }
        query = self.bot.request(f'media/{media_id}/save/', params=data)
        return GenericResponse(query)

    def unsave(self, media_id: str):
        data = {
            '_uuid': self.bot.uuid,
            '_uid': self.bot.account_id,
            '_csrftoken': self.bot.token,
            'media_id': media_id
        }
        query = self.bot.request(f'media/{media_id}/unsave/', params=data)
        return GenericResponse(query)

    def get_comments(self, media_id, max_id=''):
        data = {
            'can_support_threading': True,
            'max_id': max_id
        }
        query = self.bot.request(f'media/{media_id}/comments/', params=data)
        return MediaCommentsResponse(query)

    def get_comment_replais(self, media_id, comment_id):
        if not isinstance(comment_id, int):
            raise ValueError('comment_id must be integers.')
        query = self.bot.request(
            f'media/{media_id}/comments/{comment_id}/inline_child_comments/')
        return query


    # def upload_photo(self, photo, caption=None, upload_id=None, is_sidecar=None):
    #     if upload_id is None:
    #         upload_id = str(int(time() * 1000))
    #     data = {
    #         'upload_id': upload_id,
    #         '_uuid': self.bot.uuid,
    #         '_csrftoken': self.bot.token,
    #         'image_compression': '{"lib_name":"jt","lib_version":"1.3.0","quality":"87"}',
    #         'photo': ('pending_media_%s.jpg' % upload_id, open(photo, 'rb'), 'application/octet-stream', {'Content-Transfer-Encoding': 'binary'})
    #     }
    #     if is_sidecar:
    #         data['is_sidecar'] = '1'
    #     m = MultipartEncoder(data, boundary=self.bot.uuid)
    #     self.bot.req.headers.update({
    #         'X-IG-Capabilities': '3Q4=',
    #         'X-IG-Connection-Type': 'WIFI',
    #         'Cookie2': '$Version=1',
    #         'Accept-Language': 'en-US',
    #         'Accept-Encoding': 'gzip, deflate',
    #         'Content-type': m.content_type,
    #         'Connection': 'close',
    #         'User-Agent': self.bot.device.build_user_agent()
    #     })
    #     response = self.bot.request(
    #         "upload/photo/", params=m.to_string())
    #     if response.status_code == 200:
    #         if self.bot.configure(upload_id, photo, caption):
    #             self.bot.expose()
    #     return False

    # def configure(self, upload_id, photo, caption=''):
    #     (w, h) = getImageSize(photo)
    #     data = json.dumps({
    #         '_csrftoken': self.bot.token,
    #         'media_folder': 'Instagram',
    #         'source_type': 4,
    #         '_uid': self.bot.account_id,
    #         '_uuid': self.bot.uuid,
    #         'caption': caption,
    #         'upload_id': upload_id,
    #         'device': self.bot.device.generate_device(),
    #         'edits': {
    #             'crop_original_size': [w * 1.0, h * 1.0],
    #             'crop_center': [0.0, 0.0],
    #             'crop_zoom': 1.0
    #         },
    #         'extra': {
    #             'source_width': w,
    #             'source_height': h
    #         }
    #     })
    #     return self.bot.request('media/configure/?', params=data)

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
