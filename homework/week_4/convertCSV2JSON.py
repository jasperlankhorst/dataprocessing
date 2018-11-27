#!/usr/bin/env python
# Name: Jasper Lankhorst
# Student number: 10885803


import csv
import json
from io import StringIO

INPUT = "data.csv"
OUTPUT = "data.json"
INDEX = "AUS"
MEASURE = "KTOE"

def tojson(input_csv, output_json):
    """
    Converts a CSV (or .txt, as long as it's comma separated) to a JSON file,
    with in and output files given.
    """
    with open(input_csv, 'r') as f:
        list_of_measurements = []
        reader = csv.DictReader(f)
        for line in reader:
            fields = {}
            # Search for index
            if line["LOCATION"] == INDEX and line["MEASURE"] == MEASURE:

                fields["year"] = line["TIME"]
                fields["value"] = line["Value"]
                # Make list of dicts of date: wind speed
                list_of_measurements.append(fields)
    # Add to json
    with open(output_json, 'w') as g:
        json.dump(list_of_measurements, g)

if __name__ == "__main__":
    tojson(INPUT, OUTPUT)
