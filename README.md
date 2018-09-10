moment
======

[![Build Status](https://travis-ci.org/zachwill/moment.svg?branch=master)](https://travis-ci.org/zachwill/moment)

A Python library for dealing with dates/times. Inspired by both
[**Moment.js**][moment] and the simplicity of Kenneth Reitz's
[**Requests**][requests] library. Ideas were also taken from the
[**Times**][times] Python module.

[moment]: http://momentjs.com/docs/
[requests]: http://docs.python-requests.org/
[times]: https://github.com/nvie/times


Installation
------------

I would advise that this is alpha-quality software. You might also be interested in the [Python `arrow` package][arrow].

[arrow]: https://github.com/crsmithdev/arrow/

`pip install moment`


Usage
-----

```python
import moment
from datetime import datetime

# Create a moment from a string
moment.date("12-18-2012")

# Create a moment with a specified strftime format
moment.date("12-18-2012", "%m-%d-%Y")

# Moment uses the awesome dateparser library behind the scenes
moment.date("2012-12-18")

# Create a moment with words in it
moment.date("December 18, 2012")

# Create a moment that would normally be pretty hard to do
moment.date("2 weeks ago")

# Create a future moment that would otherwise be really difficult
moment.date("2 weeks from now")

# Create a moment from the current datetime
moment.now()

# The moment can also be UTC-based
moment.utcnow()

# Create a moment with the UTC time zone
moment.utc("2012-12-18")

# Create a moment from a Unix timestamp
moment.unix(1355875153626)

# Create a moment from a Unix UTC timestamp
moment.unix(1355875153626, utc=True)

# Return a datetime instance
moment.date(2012, 12, 18).date

# We can do the same thing with the UTC method
moment.utc(2012, 12, 18).date

# Create and format a moment using Moment.js semantics
moment.now().format("YYYY-M-D")

# Create and format a moment with strftime semantics
moment.date(2012, 12, 18).strftime("%Y-%m-%d")

# Update your moment's time zone
moment.date(datetime(2012, 12, 18)).locale("US/Central").date

# Alter the moment's UTC time zone to a different time zone
moment.utcnow().timezone("US/Eastern").date

# Set and update your moment's time zone. For instance, I'm on the
# west coast, but want NYC's current time.
moment.now().locale("US/Pacific").timezone("US/Eastern")

# In order to manipulate time zones, a locale must always be set or
# you must be using UTC.
moment.utcnow().timezone("US/Eastern").date

# You can also clone a moment, so the original stays unaltered
now = moment.utcnow().timezone("US/Pacific")
future = now.clone().add(weeks=2)
```

Chaining
--------

Moment allows you to chain commands, which turns out to be super useful.

```python
# Customize your moment by chaining commands
moment.date(2012, 12, 18).add(days=2).subtract(weeks=3).date

# Imagine trying to do this with datetime, right?
moment.utcnow().add(years=3, months=2).format("YYYY-M-D h:m A")

# You can use multiple keyword arguments
moment.date(2012, 12, 19).add(hours=1, minutes=2, seconds=3)

# And, a similar subtract example...
moment.date(2012, 12, 19, 1, 2, 3).subtract(hours=1, minutes=2, seconds=3)

# In addition to adding/subtracting, we can also replace values
moment.now().replace(hours=5, minutes=15, seconds=0).epoch()

# And, if you'd prefer to keep the microseconds on your epoch value
moment.now().replace(hours=5, minutes=15, seconds=0).epoch(rounding=False)

# Years, months, and days can also be set
moment.now().replace(years=1984, months=1, days=1, hours=0, minutes=0, seconds=0)

# Also, datetime properties are available
moment.utc(2012, 12, 19).year == 2012

# Including plural ones (since I'm bad at remembering)
moment.now().seconds

# We can also manipulate to preferred weekdays, such as Monday
moment.date(2012, 12, 19).replace(weekday=1).strftime("%Y-%m-%d")

# Or, this upcoming Sunday
moment.date("2012-12-19").replace(weekday=7).date

# We can even go back to two Sundays ago
moment.date(2012, 12, 19).replace(weekday=-7).format("YYYY-MM-DD")

# It's also available as a property
moment.utcnow().weekday

# And, there's an easy way to zero out the hours, minutes, and seconds
moment.utcnow().zero
```

Optional: Use [duckling](https://github.com/facebook/duckling)
--------

- [Duckling](https://github.com/facebook/duckling) is a library from Facebook to parse text (time expressions and others) into structured data.

- It is a Haskell library, so to use this you ll need a duckling server running on 0.0.0.0:8000 ([see the installation instructions](https://github.com/facebook/duckling#quickstart))

- Integrating with duckling allows to parse fairly complex time expressions such as `day after tomorrow`, `next Saturday` that are not covered by moment atm.

- However, this is completely optional, this behavior only triggers if moment fails to get the date (returns None) and duckling is installed. Else reverts back to the usual moment output.        

With duckling:

```python
>>> moment.date('day after tomorrow')
<Moment(2018-09-12T00:00:00)>
>>> moment.date('next saturday')
<Moment(2018-09-15T00:00:00)>
>>> 

```

W/o duckling:

```python
>>> import moment
>>> moment.date('day after tomorrow')
<Moment>
>>> moment.date('next saturday')
<Moment>
```