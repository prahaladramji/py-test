#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Forex import ForexRates

if __name__ == '__main__':
    forex = ForexRates(currency='AUD')
    print(forex.best_rate())
