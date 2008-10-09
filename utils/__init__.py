from django.conf import settings


class BloomSettingsException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)



def get_setting(setting, override=None, exception_text=None):
    "Custom settings for the Bloom project."
    if hasattr(settings, 'BLOOM_%s' % setting):
        #print 'Returning ... BLOOM_%s' % setting
        return getattr(settings, 'BLOOM_%s' % setting)
	
    if override is not None:
        return override

    if exception_text is None:
        raise BloomSettingsException('BLOOM_%s is not defined!' % setting)
    else:
        raise BloomSettingsException(exception_text)
        