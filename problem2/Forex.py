# -*- coding: utf-8 -*-

import requests
import operator
import multiprocessing.pool
from datetime import datetime
from calendar import monthrange


class ForexRates(object):

    def __init__(self, currency='AUD', host='https://api.exchangeratesapi.io/'):
        """
        Base class to get forex rates.
        :param currency: Currency to return (string)
        :param host: URL to get exchange rates from (string)
        """
        self.currency = currency
        self.host = host
        self.session = requests.session()

    # API request
    def _request(self, date, params=None):
        url = self.host + date
        resp = self.session.request('GET', url, params=params)

        if resp.status_code >= 400:
            print(resp)
            raise RuntimeError("Failed getting valid response, check request")

        return resp.json()

    def get_day_rate(self, date):
        """
        Make and api request to get exchanges rates for the specified date.
        :param date: date in format YYYY-MM-DD
        :return: Exchange rates for currency specified in the class.
        """
        return date, self._request(date)['rates'][self.currency]

    def best_rate(self, date=None):
        """
        Retrun the best rate during all days in the previous month if date not given else for the given month.
        :param date: date in format YYYY-MM-DD
        :return: Tuple of date and best rate from the previous month
        """
        if not date:
            now = datetime.now()
            _date = now.replace(month=now.month - 1)
        else:
            if date != datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError
            _date = datetime.strptime(date, '%Y-%m-%d')

        date_range = [f'{_date.year}-{_date.month:02}-{day:02}'
                      for day in range(1, monthrange(_date.year, _date.month)[1] + 1)]

        pool = multiprocessing.pool.ThreadPool(processes=32)
        result = pool.map(self.get_day_rate, date_range, chunksize=2)
        pool.close()

        # In the tuple of date, rate get a list of tuples only with the highest rate then return only the latest date.
        best_rates = [x for x in result if x[1] == max(result, key=operator.itemgetter(1))[1]]
        return max(best_rates, key=operator.itemgetter(0))
