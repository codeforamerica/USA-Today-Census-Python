#!/usr/bin/env python

try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import simplejson as json

try:
    from urllib import urlencode
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import urlencode

try:
    from urllib2 import urlopen
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen

from usa_today_api_key import API_KEY


class Census(object):
    """Wrapper for USA Today's Census API."""

    def __init__(self, api_key=''):
        if not api_key:
            self.api_key = API_KEY
        else:
            self.api_key = api_key
        self.base_url = 'http://api.usatoday.com/open/census'

    def api(self, parent, **kwargs):
        """Wrapper for USA Today's Census API calls."""
        url = [self.base_url]
        url.append('/%s' % parent)
        kwargs.update({'api_key': self.api_key})
        url.extend(['?', urlencode(kwargs)])
        api_url = ''.join(url)
        json_data = urlopen(api_url).read()
        return json.loads(json_data)

    def locations(self, **kwargs):
        """
        Returns all available ethnicity, housing, population and race
        information for specified area.

        >>> Census().locations()
        """
        return self.api('locations', **kwargs)

    def ethnicity(self, **kwargs):
        """
        Returns an area's ethnic data. Information includes how much of the
        population identifies as Hispanic or non-Hispanic white, and the USA
        TODAY Diversity Index.

        >>> Census().ethnicity()
        """
        return self.api('ethnicity', **kwargs)

    def housing(self, **kwargs):
        """
        Returns an area's housing data. Information includes the number of
        housing units, and the percentage of those that are vacant.

        >>> Census().housing()
        """
        return self.api('ethnicity', **kwargs)

    def population(self, **kwargs):
        """
        Returns an area's population data. Information includes the total
        population of an area, average population per square mile, and the
        percent by which that population has changed since the last census.

        >>> Census().population()
        """
        return self.api('population', **kwargs)

    def race(self, **kwargs):
        """
        Returns an area's racial data. Information includes the percentage
        of an area's population that identifies as White, Black, American
        Indian, Asian, native Hawaiian/Pacific Islander, or mixed race.

        >>> Census().race()
        """
        return self.api('race', **kwargs)
