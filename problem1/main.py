#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SpaceX import SpaceXData
from pprint import pprint
import sys


def decorator(msg):
    print(
        '\n'
        f'{"#" * (len(msg) + 12)}\n'
        f'{"#" * 5} {msg} {"#" * 5}\n'
        f'{"#" * (len(msg) + 12)}\n', file=sys.stderr
    )


if __name__ == '__main__':
    spacex = SpaceXData()
    decorator('Question 1 - Launches')
    pprint(spacex.get_launch_date_range(start='2019-01-01', end='2019-06-25'))

    decorator('Question 2 - Heaviest Launch')
    pprint(spacex.get_heaviest_launch(start='2019-04-01', end='2020-01-01'))
