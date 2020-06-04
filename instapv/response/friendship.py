import json
from instapv.exceptions import UserNotFoundException


class FriendShipResponse:
    
    def __init__(self, data):
        if data:
            self.status = None
            self.following = None
            self.followed_by = None
            self.blocking = None
            self.muting = None
            self.is_private = None
            self.incoming_request = None
            self.outgoing_request = None
            self.is_bestie = None
            self.is_restricted = None

            # Check request status 
            if 'status' in data:
                if data['status'] != 'ok':
                    raise UserNotFoundException('UserNotFound')
                if 'friendship_status' in data:
                    data = data['friendship_status']
                if 'following' in data:
                    self.following = data['following']
                if 'followed_by' in data:
                    self.followed_by = data['followed_by']
                if 'blocking' in data:
                    self.blocking = data['blocking']
                if 'muting' in data:
                    self.muting = data['muting']
                if 'is_private' in data:
                    self.is_private = data['is_private']
                if 'incoming_request' in data:
                    self.incoming_request = data['incoming_request']
                if 'outgoing_request' in data:
                    self.outgoing_request = data['outgoing_request']
                if 'is_bestie' in data:
                    self.is_bestie = data['is_bestie']
                if 'is_restricted' in data:
                    self.is_restricted = data['is_restricted']
                if 'status' in data:
                    self.status = data['status']
            else:
                raise UserNotFoundException('UserNotFound')
