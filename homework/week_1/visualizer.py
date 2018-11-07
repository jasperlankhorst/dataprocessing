#!/usr/bin/env python
# Name: Jasper Lankhorst
# Student number: 10885803
"""
This script visualizes data obtained from a .csv file
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

# Global constants for the input file, first and last year
INPUT_CSV = "movies.csv"
START_YEAR = 2008
END_YEAR = 2018

# Global dictionary for the data
data_dict = {str(key): [] for key in range(START_YEAR, END_YEAR)}

def add_dict():
    """
    Adds the ratings for movies from a csv file to a dict with the year as key.
    """
    with open(INPUT_CSV, 'r') as f:
        # Start reading, skip first line
        reader = csv.reader(f)
        next(f)
        for row in reader:
            data_dict[row[2]].append(row[1])


def make_plot(dict_values):
    """
    Creates plot of key and the average of the values belonging to key.
    """
    # Calculate average every year and replace list of values by it
    for i in range(START_YEAR, END_YEAR):
        total = 0.
        for j in range(len(dict_values[str(i)])):
            total += float(dict_values[str(i)][j])
        avg_rating = total / len(dict_values[str(i)])
        dict_values[str(i)] = avg_rating

    # Sort, make list, plot list
    sorted_dict = sorted(dict_values.items())
    xlist, ylist = zip(*sorted_dict)

    plt.plot(xlist, ylist, 'g')
    plt.ylim(0, 10)
    plt.xlabel("Year")
    plt.ylabel("Average rating (out of 10)")
    plt.title("Average rating over years in IMDB top 50")
    plt.show()


if __name__ == "__main__":
    add_dict()
    make_plot(data_dict)
