import json
from instapv.response.user_response import UserResponse

class CommentInfoResponse:

    def __init__(self, data: list):
        self.as_json = data


class CommentUserInfoResponse:
    
    def __init__(self, data: list):
        self.user = data 



class MediaCommentsResponse:

    def __init__(self, data: dict):
        self.as_json = data

        _new = []
        for i in data['comments']:
            data.update({'user': UserResponse(i['user'])})


        self.comments = CommentUserInfoResponse(data['comments']) if 'comments' in data else None
        self.comment_likes_enabled = data['comment_likes_enabled'] if 'comment_likes_enabled' in data else None
        self.comment_count = data['comment_count'] if 'comment_count' in data else None
        self.caption = data['caption'] if 'caption' in data else None
        self.caption_is_edited = data['caption_is_edited'] if 'caption_is_edited' in data else None
        self.has_more_comments = data['has_more_comments'] if 'has_more_comments' in data else None
        self.has_more_headload_comments = data['has_more_headload_comments'] if 'has_more_headload_comments' in data else None
        self.threading_enabled = data['threading_enabled'] if 'threading_enabled' in data else None
        self.media_header_display = data['media_header_display'] if 'media_header_display' in data else None
        self.display_realtime_typing_indicator = data['display_realtime_typing_indicator'] if 'display_realtime_typing_indicator' in data else None
        self.quick_response_emojis = data['quick_response_emojis'] if 'quick_response_emojis' in data else None
        self.preview_comments = data['preview_comments'] if 'preview_comments' in data else None
        self.can_view_more_preview_comments = data['can_view_more_preview_comments'] if 'can_view_more_preview_comments' in data else None
        self.status = data['status'] if 'status' in data else None