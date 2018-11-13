#!/usr/bin/env python
# Name: Jasper Lankhorst
# Student number: 10885803
"""
This script analyzes and visualizes some data.
"""

import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from contextlib import closing
from requests import get
from requests.exceptions import RequestException


INPUT_CSV = "input.csv"

def parsing_data():
    """
    Reading and refining the data from an input file.
    """

    data_dict = {}

    with open(INPUT_CSV, 'r') as f:
        # Start reading, skip first line
        reader = csv.reader(f)
        next(f)
        n = 0
        for row in reader:
            print(row[0])
            n += 1
            data_dict[row[0]] = [row[1]]
            data_dict[row[0]].append(row[4])
            data_dict[row[0]].append(row[7])
            data_dict[row[0]].append(row[8])
    print(data_dict)

if __name__ == "__main__":
    parsing_data()
