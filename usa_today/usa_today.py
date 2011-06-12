#!/usr/bin/env python

"""
Python wrapper for USA Today's Census API.

USA Today Documentation:  http://developer.usatoday.com/docs/read/Census
"""

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

    def call_api(self, name, **kwargs):
        """
        Semi-internal method for calling USA Today's Census API. Most of the
        other methods rely on this method.

        >>> Census().api('locations', keypat='KY')
        """
        url = [self.base_url]
        url.append('/%s' % name)
        kwargs.update({'api_key': self.api_key})
        url.extend(['?', urlencode(kwargs)])
        api_url = ''.join(url)
        json_data = urlopen(api_url).read()
        return json.loads(json_data)

    def _resolve_url(self, directory, keypat=None, **kwargs):
        """Internal method to resolve URL structure."""
        if keypat:
            kwargs.update({'keypat': keypat})
        return self.call_api(directory, **kwargs)

    def locations(self, keypat=None, **kwargs):
        """
        Returns all available ethnicity, housing, population and race
        information for specified area.

        >>> Census().locations()
        """
        self._resolve_url('locations', keypat, **kwargs)

    def ethnicity(self, keypat=None, **kwargs):
        """
        Returns an area's ethnic data. Information includes how much of the
        population identifies as Hispanic or non-Hispanic white, and the USA
        TODAY Diversity Index.

        >>> Census().ethnicity('CA')

        >>> Census().ethnicity('CA', sumlevid=6)
        """
        self._resolve_url('ethnicity', keypat, **kwargs)

    def housing(self, keypat=None, **kwargs):
        """
        Returns an area's housing data. Information includes the number of
        housing units, and the percentage of those that are vacant.

        >>> Census().housing('TX')

        >>> Census().housing('TX', sumlevid=3)
        """
        self._resolve_url('housing', keypat, **kwargs)

    def population(self, keypat=None, **kwargs):
        """
        Returns an area's population data. Information includes the total
        population of an area, average population per square mile, and the
        percent by which that population has changed since the last census.

        >>> Census().population()

        >>> Census().population('RI')
        """
        self._resolve_url('population', keypat, **kwargs)

    def race(self, keypat=None, **kwargs):
        """
        Returns an area's racial data. Information includes the percentage
        of an area's population that identifies as White, Black, American
        Indian, Asian, native Hawaiian/Pacific Islander, or mixed race.

        >>> Census().race()

        >>> Census().race('NY', sumlevid=3)
        """
        self._resolve_url('race', keypat, **kwargs)
