#datetimeutc

## Because why are we dealing with timezones?

A lightweight datetime utility library which wraps around the standard datetime module, with features from dateutil, and pytz.

Its purpose is to minimize the effort to convert datetime to/from UTC, a task I found myself doing too often internationalizing web services and apps.

This wrapper is designed under these datetime philosophy:

1. datetime should always be timezone aware
2. datetime should always be handled and stored in UTC time
3. datetime should always default to UTC time
4. datetime should not communicate in server local time, in order to secure server location
5. timezone conversions should be done on client side

## Install

```shell
pip install datetimeutc
```

## Usage

```python

```

## Utilities

