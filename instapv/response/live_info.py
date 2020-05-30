import json

class LiveInfoResponse:

    def __init__(self, data: dict):
        if data:
            if data['status'] == 'ok':
                self.broadcast_id = None
                self.upload_url = None

                if 'broadcast_id' in data:
                    self.broadcast_id = data['broadcast_id']
                if 'upload_url' in data:
                    self.upload_url = data['upload_url']
