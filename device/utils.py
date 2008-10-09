# Bloom Framework
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca

"""
Might want to look at hardcaching the device_atlas object somewhere.
It takes ~3s to start it up so it's something you don't want to lose!

http://www.b-list.org/weblog/2007/nov/05/server-startup/

>>> from deviceatlas.api import DaApi
>>> da = DaApi()
>>> path_to_device_atlas_json = '/Users/johnboxall/djcode/deviceatlas/DeviceAtlas.json'
>>> tree = da.getTreeFromFile(path_to_device_atlas_json)
>>> da.getTreeRevision(tree)
2590
>>> ua = 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3'
>>> da.getProperties(tree, ua)
{u'gprs': '1', u'memoryLimitDownload': '0', u'mpeg4': '1', u'image.Png': '1', u'memoryLimitEmbeddedMedia': '0', u'umts': '0', u'displayWidth': '320', u'mp3': '1', u'usableDisplayHeight': '360', u'markup.xhtmlMp10': '1', u'cookieSupport': '0', u'markup.xhtmlMp12': '1', u'isSpam': '0', u'image.Gif89a': '1', u'h263Type3InVideo': '0', u'midiPolyphonic': '0', u'image.Gif87': '1', u'isChecker': '0', u'markup.xhtmlMp11': '1', u'csd': '0', u'3gpp': '0', u'drmOmaForwardLock': '0', u'qcelp': '0', u'wmv': '0', u'id': '205202', u'markup.xhtmlBasic10': '1', u'aacLtpInVideo': '0', u'amrInVideo': '0', u'qcelpInVideo': '0', u'https': '1', u'memoryLimitMarkup': '0', u'3gpp2': '0', u'hscsd': '0', u'aacInVideo': '1', u'drmOmaSeparateDelivery': '0', u'displayColorDepth': '8', u'vendor': 'Apple', u'image.Jpg': '1', u'uriSchemeTel': '1', u'isRobot': '1', u'mobileDevice': '1', u'isBrowser': '0', '_unmatched': 'one; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3', u'isFilter': '0', u'isDownloader': '0', u'hsdpa': '0', u'amr': '0', u'model': 'iPhone', u'drmOmaCombinedDelivery': '0', u'aac': '1', u'mpeg4InVideo': '1', u'awbInVideo': '0', u'edge': '1', u'usableDisplayWidth': '320', u'h263Type0InVideo': '0', u'displayHeight': '480', u'midiMonophonic': '0', '_matched': 'Mozilla/5.0 (iPh'}

"""
import time
from distutils.sysconfig import get_python_lib	

from django.conf import settings

from deviceatlas.api import DaApi

from bloom.utils import get_setting

device_atlas = DaApi()
default_da_path = "%s/deviceatlas/DeviceAtlas.json" % get_python_lib()	
DEVICE_ATLAS_PATH = get_setting('DEVICE_ATLAS_PATH', override=default_da_path)
	
try:
	device_atlas_tree = device_atlas.getTreeFromFile(DEVICE_ATLAS_PATH)
except Exception:
	raise DeviceAtlasJSONNotFoundException("Couldn\'t find Device Atlas JSON Library. Check BLOOM_DEVICE_ATLAS_PATH")

def get_device(request):
	ua = request.META['HTTP_USER_AGENT']
	return device_atlas.getPropertiesAsTyped(device_atlas_tree, ua)			
