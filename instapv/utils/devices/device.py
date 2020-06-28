import random
import hashlib
from packaging import version
from instapv.config import Config

_config = Config() 

class DeviceGenerator:
    
    def __init__(self):
        # All Good Devices
        self.DEVICES = [
            '24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom',
            '23/6.0.1; 640dpi; 1440x2392; LGE/lge; RS988; h1; h1',
            '24/7.0; 640dpi; 1440x2560; HUAWEI; LON-L29; HWLON; hi3660',
            '23/6.0.1; 640dpi; 1440x2560; ZTE; ZTE A2017U; ailsa_ii; qcom',
            '23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935F; hero2lte; samsungexynos8890',
            '23/6.0.1; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890',
        ]

        self.REQUIRED_ANDROID_VERSION = '2.2'
        self.USER_AGENT_FORMAT = 'Instagram %s Android (%s/%s; %s; %s; %s; %s; %s; %s; %s)'

        self._userAgent = None

        self._androidVersion = None
        self._androidRelease = None
        self._dpi = None
        self._resolution = None
        self._manufacturer = None
        self._brand = None
        self._model = None
        self._device = None
        self._cpu = None

        self.generate_device()

    def generate_device_id(self, seed):
        volatile_seed = "12345"
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]


    def get_random_device(self):
        return random.choice(self.DEVICES)

    def get_all_good_devices(self):
        return self.DEVICES

    def is_good_device(self, device: str):
        return True if device in self.DEVICES else False

    def generate_device(self):
        device = self.get_random_device()

        parts = device.split('; ')
        if len(parts) != 7:
            raise RuntimeError('Invalid Device: %s' % device)

        andriodOS = str(parts[0]).split('/', 2)
        if version.parse(andriodOS[1]) < version.parse(self.REQUIRED_ANDROID_VERSION):
            raise RuntimeError('Device %s required Andriod version %s for instagram' % (device, self.REQUIRED_ANDROID_VERSION))

        resolution = str(parts[2]).split('x', 2)
        pixelCount = int(resolution[0]) * int(resolution[1])
        if pixelCount < 2073600:
            raise RuntimeError('Invalid Resolution: %s minimum resolution is 1920x1080' % resolution)
        
        manufacturerAndBrand = str(parts[3]).split('/', 2)

        self._device = device
        self._androidVersion = andriodOS[0]
        self._androidRelease = andriodOS[1]
        self._dpi = parts[1]
        self._resolution = parts[2]
        self._manufacturer = manufacturerAndBrand[0]
        try:
            self._brand = manufacturerAndBrand[1] if manufacturerAndBrand[1] else None
        except IndexError:
            pass
        self._model = parts[4]
        self._device = parts[5]
        self._cpu = parts[6]

        self._userAgent = self.build_user_agent()


    def build_user_agent(self):
        manufacturer = self._manufacturer
        if self._brand != None:
            manufacturer = '/' + self._brand

        device = self.USER_AGENT_FORMAT % (
            _config.IG_VERSION,
            self._androidVersion,
            self._androidRelease,
            self._dpi,
            self._resolution,
            manufacturer,
            self._model,
            self._device,
            self._cpu,
            _config.USER_AGENT_LOCALE,
        )
        return device

        
    
    
