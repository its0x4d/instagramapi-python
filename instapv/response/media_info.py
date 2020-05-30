import json
from ..response.media_items_info import MediaItemsInfoResponse

class MediaInfoResponse:


    def __init__(self, data: dict):
        if 'num_results' in data:
            if int(data['num_results']) > 0:
                if 'items' in data:
                    self.items: MediaItemsInfoResponse = MediaItemsInfoResponse(data['items'][0])
                    self.num_results: int = data['num_results']
                    self.more_available: bool = data['more_available']
                    self.auto_load_more_enabled: bool = data['auto_load_more_enabled']
                    self.status: str = data['status']
