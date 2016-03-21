#datetimeutc

## Because why are we dealing with timezones?

A lightweight datetime utility library which wraps around the standard `datetime` module, with features from dateutil and pytz.

Its purpose is to minimize the effort to convert datetime to/from UTC, a task I found myself doing too often while internationalizing web services and apps.

This wrapper is designed under these datetime philosophy:

1. datetime should always be timezone aware
2. datetime should always be handled and stored in UTC time
3. datetime should always default to UTC time
4. datetime should not contain server local time
5. timezone conversions should be done on client side

## Install

```shell
pip install datetimeutc
```

## Usage

The library provides thinly wrappers of datetime classes, e.g. datetime, date, and time.

Instances of these class are created with timezone awareness in UTC time. Users can also pass in `None` or other timezone, which the library will automatically converts into UTC time.

```python
>>> from datetimeutc import Datetime, Date, Time
>>> import pytz
>>> d = Datetime(2016, 3, 21, 9, 20, 40)
Datetime(2016, 3, 21, 9, 20, 40, tzinfo=<UTC>)
>>> Datetime(2016, 3, 21, 9, 20, 40, tzinfo=pytz.timezone('US/Eastern'))
Datetime(2016, 3, 21, 14, 16, 40, tzinfo=<UTC>)
```

Functions of datetime are all supported.

```python
>>> from datetimeutc import Datetime, Date, Time
>>> Datetime.now()
Datetime(2016, 3, 21, 9, 20, 40, 816025, tzinfo=<UTC>)
>>> Datetime.now().dst()      
datetime.timedelta(0)
>>> Datetime.now().timetuple()
time.struct_time(tm_year=2016, tm_mon=3, tm_mday=21, tm_hour=9, tm_min=7, tm_sec=47, tm_wday=0, tm_yday=81, tm_isdst=0)
>>> Datetime.now().toordinal()
736044
>>> Datetime.now().isoweekday()
1
>>> Datetime.now().isoformat()
'2016-03-21T09:08:17.488494+00:00'
>>> Datetime.strptime('2016-03-21','%Y-%m-%d')
Datetime(2016, 3, 21, 0, 0, tzinfo=<UTC>)
>>> datetimeutc.Datetime(2016, 3, 21, 9, 20, 40).astimezone(pytz.timezone('US/Eastern'))
datetime.datetime(2016, 3, 21, 5, 20, 40, tzinfo=<DstTzInfo 'US/Eastern' EDT-1 day, 20:00:00 DST>)
```

## Utilities

Other datetime functions are available for common tasks, e.g. converting to/from javascript timestamp

```python
>>> import datetimeutc, datetime
>>> datetimeutc.to_utc(datetime.datetime.now())
datetime.datetime(2016, 3, 21, 9, 31, 8, 455166, tzinfo=<UTC>)
>>> d = datetimeutc.Datetime(2016, 3, 21, 9, 20, 40)
>>> d
Datetime(2016, 3, 21, 9, 20, 40, tzinfo=<UTC>)
>>> d.timestamp
1458552040
>>> d.jstimestamp 
1458552040000.0
>>> datetimeutc.Datetime.from_jstimestamp(d.jstimestamp)
Datetime(2016, 3, 21, 9, 20, 40, tzinfo=<UTC>)
```
