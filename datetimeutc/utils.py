import datetime
import dateutil.tz
import pytz
import calendar

LOCAL_TIMEZONE = dateutil.tz.tzlocal()

def to_utc(dt):
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=LOCAL_TIMEZONE)
    if dt.tzinfo != pytz.UTC:
        return dt.astimezone(tz=pytz.UTC)
    return dt

def to_timestamp(dt):
    return calendar.timegm(to_utc(dt).timetuple())

def to_jstimestamp(dt):
    jstimestamp = to_timestamp(dt) * 1000.0
    if hasattr(dt,'microsecond'):
        jstimestamp += dt.microsecond / 1000.0
    return jstimestamp

class datetimeutils(object):
    'An util class for adding useful methods, e.g. to/from timestamp'
    
    @property
    def timestamp(self):
        return to_timestamp(self)
    
    @property
    def jstimestamp(self):
        return to_jstimestamp(self)
    
    @classmethod
    def from_jstimestamp(cls, jstimestamp):
        return cls.fromtimestamp(jstimestamp / 1000.0)
