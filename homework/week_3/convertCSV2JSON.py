#!/usr/bin/env python
# Name: Jasper Lankhorst
# Student number: 10885803


import csv
import json
from io import StringIO

INPUT = "KNMI_20181119.txt"
OUTPUT = "data.json"
BILT = "260"

def tojson(input_csv, output_json):
    """
    Converts a CSV (or .txt, as long as it's comma separated) to a JSON file,
    with in and output files given.
    """
    with open(input_csv, 'r') as f:
        list_of_measurements = []
        for line in f:
            # Search for De Bilt
            if line[:5].strip() == BILT:
                fields = list(map(lambda x: x.strip(), line.split(',')))
                # Make list of dicts of date: wind speed
                measurement = {fields[1]: int(fields[2])}
                list_of_measurements.append(measurement)
    # Add to json
    with open(output_json, 'w') as g:
        json.dump(list_of_measurements, g)

if __name__ == "__main__":
    tojson(INPUT, OUTPUT)
