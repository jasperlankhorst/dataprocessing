#!/usr/bin/env python
# Name: Jasper Lankhorst
# Student number: 10885803
"""
This script analyzes and visualizes some data.
"""

import csv
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from contextlib import closing
from scipy import stats
from requests import get
from requests.exceptions import RequestException


INPUT_CSV = "input.csv"
OUTPUT_CSV = "output.csv"

def isolate_digit(some_string):
    """
    Takes a float or int from a string and isolates it, cutting off all text
    and replacing commas with dots. If no digits found, output is 0.
    """

    is_float = False
    output = ""
    for i in some_string:
        if i.isdigit():
            output += i
        if i == ',' or i == '.':
            output += '.'
            is_float = True

    if len(output) == 0:
        return 0
    if is_float == True:
        return float(output)
    if is_float == False:
        return int(output)


def parsing_data():
    """
    Reading and refining the data from an input file.
    Saving to OUTPUT_CSV.
    """

    countries_list = []

    with open(INPUT_CSV, 'r') as f:
        # Start reading, skip first line
        reader = csv.reader(f)
        next(f)
        for row in reader:
            # Add relevant info to list per country
            if len(row) > 1:
                country = row[0].strip()
                # Check country name for commas and such and fix
                if ',' in country:
                    for i in range(len(country) - 3):
                        if country[i] == ',':
                            country = (country[(i + 1):] + ' ' +
                                       country[:(i)]).strip()
                # Get other relevant variables
                region = row[1].strip()
                inf_mortality = isolate_digit(row[4])
                pop_density = isolate_digit(row[7])
                gdp = isolate_digit(row[8])

                # Adding list to list
                country_list = [country, region, pop_density, inf_mortality,
                                gdp]
                countries_list.append(country_list)

    with open(OUTPUT_CSV, 'w') as g:
        save_csv(g, countries_list)


def save_csv(outfile, csv_countries):
    """
    Output a CSV file containing countries and some info about it.
    """
    writer = csv.writer(outfile)
    writer.writerow(['Country', 'Region', 'Population Density', 'Infant Mortality',
                     'GDP ($ per capita)'])

    # Iterate through countries file and write rows
    for row in csv_countries:
        writer.writerow(row)


if __name__ == "__main__":
    parsing_data()
    countries_frame = pd.read_csv(OUTPUT_CSV)
    a = countries_frame['GDP ($ per capita)']
    print(a[~((a - a.mean()).abs() > 3 * a.std())])
    a = a[~((a - a.mean()).abs() > 3 * a.std())]
    a.plot.hist(bins=100)
    plt.show()
    print(f"Standard deviation in GDP: {countries_frame['GDP ($ per capita)'].std()}")
