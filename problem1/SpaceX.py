import requests
from urllib.parse import urljoin


class SpaceXData(object):

    def __init__(self, host='https://api.spacexdata.com', version='v3'):
        """
        Instantiate a new API client.
        Args:
            host (str): Hostname of the factomd instance.
            version (str): API version to use. This should remain 'v3'.
        """
        self.version = version
        self.host = host

        # Initialize the session.
        self.session = requests.Session()

    # Convenience method for building request URLs.
    @property
    def url(self):
        return urljoin(self.host, self.version)

    def handle_error_response(self, resp):
        print(resp)
        raise RuntimeError("Response code not 200 go check code")

    # Perform an API request.
    def _request(self, path, params=None):
        fullpath = self.url + '/' + path
        resp = self.session.request('GET', fullpath, params=params)

        # If something goes wrong, we'll pass the response
        # off to the error-handling code
        if resp.status_code >= 400:
            self.handle_error_response(resp)

        # Otherwise return the result dictionary.
        return resp.json()

    # API methods
    def get_launches(self, **kwargs):
        return self._request('launches/'.format(kwargs.get('path', '')), kwargs)

    def get_payloads(self, flight_number):
        """ Fetch Payloads """
        flight = self.get_launches(path='upcoming', flight_number=flight_number)[0]
        payloads = flight.get('rocket').get('second_stage').get('payloads')
        return payloads

    def get_launch_date_range(self, start, end):
        """
        An api exists to get past launches `/past?start=YYYY-MM-DD&end=YYYY-MM-DD`
        :param start: Start date in format YYYY-MM-DD (string)
        :param end: End date in format YYYY-MM-DD (string)
        """
        launches = self.get_launches(path='past', start=start, end=end)
        return launches

    def get_heaviest_launch(self, start, end):
        """
        Api responses have the weight of the payload in `rocket.second_stage.payloads.[*].payload_mass_kg`
        :param start: Start date in format YYYY-MM-DD (string)
        :param end: End date in format YYYY-MM-DD (string)
        """
        launches = self.get_launch_date_range(start=start, end=end)
        heaviest_launch = max(launches, key=lambda x: [y['payload_mass_kg']
                                                       for y in x['rocket']['second_stage']['payloads']])
        return heaviest_launch
