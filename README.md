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

Copyright (c) 2010 Code for America Laboratories
See LICENSE for details.
