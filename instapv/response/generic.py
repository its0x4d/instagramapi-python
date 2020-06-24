import json

class GenericResponse:

    def __init__(self, data: dict):
        if data:
            self.message = None
            self.status = None
            self.as_json = data
            
            if 'message' in data:
                self.message = data['message']
            if 'status' in data:
                self.status = data['status']
