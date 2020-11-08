#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from Forex import ForexRates

forex = ForexRates(currency='AUD')


class TestForex(unittest.TestCase):

    def test_best_rate_in_may(self):
        self.assertTupleEqual(forex.best_rate('2019-05-15'), ('2019-05-19', 1.6239))

    def test_date_input(self):
        with self.assertRaises(ValueError):
            forex.best_rate('15-05-2019')


if __name__ == '__main__':
    unittest.main()
