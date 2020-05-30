from uuid import uuid4
import hmac
import urllib
import hashlib
from instapv.config import Config

class Tools:

    def __init__(self):
        self.config = Config()
        super().__init__()

    def generate_uuid(self, type):
        generated_uuid = str(uuid4())
        if (type):
            return generated_uuid
        else:
            return generated_uuid.replace('-', '')

    def generate_signature(self, data, skip_quote=False):
        if not skip_quote:
            try:
                parsedData = urllib.parse.quote(data)
            except AttributeError:
                parsedData = urllib.quote(data)
        else:
            parsedData = data
        return 'ig_sig_key_version=' + self.config.SIG_KEY_VERSION + '&signed_body=' + hmac.new(self.config.IG_SIG_KEY.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest() + '.' + parsedData

