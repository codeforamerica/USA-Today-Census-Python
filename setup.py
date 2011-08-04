#!/usr/bin/env python
"""
Author: Zach Williams, <zach AT codeforamerica DOT org>

Copyright (c) 2011, Code for America. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer. Redistributions in binary form
must reproduce the above copyright notice, this list of conditions and the
following disclaimer in the documentation and/or other materials provided with
the distribution. Neither the name of Code for America nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission. THIS SOFTWARE IS PROVIDED
BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
USA Today Python API Wrapper
============================

This is a Python wrapper for [USA Today's Census
API](http://developer.usatoday.com/docs/read/Census).

Note that usage of the USA Today Census API requires a developer key,
and that usage is contingent upon agreement with USA Today's [Terms of
Use](http://developer.usatoday.com/API_Terms_of_Use).

Also, note that this library is in no way associated or endorsed by [USA
Today](http://www.usatoday.com/).


Usage
-----

It's recommended that you save your USA Today Census API Key to the
`usa_today_api_key.py` file.

Without your API Key saved:

    >>> from usa_today import Census
    >>> Census('my_api_key').population()


With your API Key saved:

    >>> from usa_today import Census
    >>> Census().population()


### Methods ###

* `locations` -- Returns all available ethnicity, housing, population and race information for specified area.
<pre><code>
    >>> Census().locations()

    >>> Census().locations('NY')
</code></pre>

* `ethnicity` -- Returns an area's ethnic data. Information includes how much of the population identifies as Hispanic or non-Hispanic white, and the USA TODAY Diversity Index.
<pre><code>
    >>> Census().ethnicity()

    >>> # California ethnicity by county
    ... Census().ethnicity('CA', sumlevid=3)
</code></pre>

* `housing` -- Returns an area's housing data. Information includes the number of housing units, and the percentage of those that are vacant.
<pre><code>
    >>> c = Census()

    >>> c.housing()

    >>> c.housing('TX')

    >>> # Lookup Texas housing by FIPS for counties
    ... c.housing('48~', keyname='FIPS', sumlevid=3)
</code></pre>


* `population` -- Returns an area's population data. Information includes the total population of an area, average population per square mile, and the percent by which that population has changed since the last census.
<pre><code>
    >>> c = Census()

    >>> c.population()

    >>> # Texas population by town level.
    ... c.population('TX', sumlevid=6)
</code></pre>

* `race` -- Returns an area's racial data. Information includes the percentage of an area's population that identifies as White, Black, American Indian, Asian, native Hawaiian/Pacific Islander, or mixed race.
<pre><code>
    >>> c = Census()

    >>> c.race()

    >>> c.race('RI')

    >>> # Race data for Rhode Island by county.
    ... c.race('RI', sumlevid=3)
</code></pre>


Copyright
---------

Copyright (c) 2011 Code for America Laboratories

See LICENSE for details.
"""

setup(name="usa_today",
      version="1.0",
      description="Python wrapper for the USA Today Census API.",
      long_description=long_description,
      keywords="usa_today, USA Today, census, usa today census, census api",
      author="Zach Williams",
      author_email="zach@codeforamerica.org",
      url="https://github.com/codeforamerica/USA-Today-Census-Python",
      license="BSD",
      packages=["usa_today"],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                  ],
      test_suite="test.py",
      tests_require=["mock", "Mock"])
