import json

class UserCommentResponse:

    def __init__(self, data: dict):
        self.pk = data['pk']
        self.username = data['username']
        self.full_name = data['full_name']
        self.is_private = data['is_private']
        self.profile_pic_url = data['profile_pic_url']
        self.is_verified = data['is_verified']
        self.has_anonymous_profile_picture = data['has_anonymous_profile_picture']
        self.reel_auto_archive = data['reel_auto_archive']
        self.allowed_commenter_type = data['allowed_commenter_type']

class SendCommentInfoResponse:

    def __init__(self, data: dict):
        self.as_json = data
        self.status = data['status']
        self.content_type = None
        self.user = None
        self.pk = None
        self.text = None
        self.type = None
        self.created_at = None
        self.created_at_utc = None
        self.media_id = None
        self.comment_status = None
        self.share_enabled = None

        if 'content_type' in data['comment']:
            self.content_type = data['comment']['content_type']
        if 'user' in data['comment']:
            self.user = UserCommentResponse(data['comment']['user'])
        if 'pk' in data['comment']:
            self.pk = data['comment']['pk']
        if 'text' in data['comment']:
            self.text = data['comment']['text']
        if 'type' in data['comment']:
            self.type = data['comment']['type']
        if 'created_at' in data['comment']:
            self.created_at = data['comment']['created_at']
        if 'created_at_utc' in data['comment']:
            self.created_at_utc = data['comment']['created_at_utc']
        if 'comment_status' in data['comment']:
            self.comment_status = data['comment']['status']
        if 'share_enabled' in data['comment']:
            self.share_enabled = data['comment']['share_enabled']
