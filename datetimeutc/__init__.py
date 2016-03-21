import datetime
import pytz

import utils
from utils import to_utc

def _get_naive_datetime(*args, **kwargs):
    now = datetime.datetime.now()
    return now.replace(*args, **kwargs)
    
class Datetime(datetime.datetime, utils.datetimeutils):
    'A subclass of datetime.datetime that autoconvert into UTC time'
    
    def __new__(cls, year, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC):
        return cls.from_datetime(datetime.datetime(year, month, day,
                                                   hour, minute, second, microsecond,
                                                   tzinfo))
    
    @classmethod
    def from_datetime(cls, dt):
        dt = to_utc(dt)
        return datetime.datetime.__new__(cls, dt.year, dt.month, dt.day, 
                                         dt.hour, dt.minute, dt.second, dt.microsecond,
                                         tzinfo=pytz.UTC)
    
    def __cmp(self, other):
        return super(Datetime, self).__cmp(to_utc(other))
    
    @classmethod
    def utcnow(cls):
        return cls.now().replace(tzinfo=None)
    
    def date(self):
        'Returns datetimeutc.Date, with timezone awareness'
        return Date.from_datetime(self)
    
    def time(self):
        'Returns datetimeutc.Time, with timezone awareness'
        return Time.from_datetime(self)
    
    
class Date(datetime.date, utils.datetimeutils):
    'A subclass of datetime.date that autoconvert into UTC time'
    
    def __new__(cls, year, month=1, day=1, tzinfo=None):
        ""
        dt = to_utc(_get_naive_datetime(year=year, month=month, day=day, tzinfo=tzinfo))
        self = datetime.date.__new__(cls, dt.year, dt.month, dt.day)
        self.tzinfo = pytz.UTC
        return self
    
    @classmethod
    def from_datetime(cls, dt):
        return cls(dt.year, dt.month, dt.day, tzinfo=dt.tzinfo)
    
    def __repr__(self):
        'Convert to formal string, for repr().'
        return '{}({}, {}, {}, tzinfo={})'.format(self.__class__.__name__,
                                                    self.year, self.month, self.day,
                                                    self.tzinfo)
    
    
class Time(datetime.time, utils.datetimeutils):
    'A subclass of datetime.time that autoconvert into UTC time'
    
    def __new__(cls, hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC):
        dt = to_utc(_get_naive_datetime(hour=hour, minute=minute,
                                        second=second, microsecond=microsecond,
                                        tzinfo=tzinfo))
        return datetime.time.__new__(cls, dt.hour, dt.minute, dt.second, dt.microsecond, tzinfo=pytz.UTC)
    
    @classmethod
    def from_datetime(cls, dt):
        return cls(dt.hour, dt.minute, dt.second, dt.microsecond, tzinfo=dt.tzinfo)
    
    @classmethod
    def now(cls):
        return cls.from_datetime(datetime.datetime.now())
    
