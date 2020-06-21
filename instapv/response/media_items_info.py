import json


class MediaItemsInfoResponse:
    
    def __init__(self, data: dict):

        self.taken_at = None
        self.as_json = data

        if 'taken_at' in data:
            self.taken_at: int = data['taken_at']
