import setuptools

setuptools.setup(name='datetimeutc',
                 version='0.1.1',
                 description='Because why are we dealing with timezones?',
                 url='http://github.com/whosken/datetimeutc',
                 author='Ken Hu',
                 author_email='whosbacon@gmail.com',
                 license='MIT',
                 packages=['datetimeutc'],
                 install_requires=['pytz','python-dateutil'],
                 keywords=['datetime','timezone','utc']
                 )
