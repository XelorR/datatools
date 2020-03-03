#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Run it as python -i FILEPATH
or ipython -i FILEPATH

you can use alias function in your OS to map it

to interactively explore data
"""


import sys
import pandas as pd
from lib.iodata.iodata import load_data, save_data

df = load_data(sys.argv[1])
