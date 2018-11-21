#!/usr/bin/env python
# Name: Jasper Lankhorst
# Student number: 10885803


import csv
import json

INPUT = "KNMI_20181119.txt"
OUTPUT = "weather_data.json"


def tojson(input_csv, output_json):
    """
    Converts a CSV (or .txt, as long as it's comma separated) to a JSON file,
    with in and output files given.
    """
    with open(input_csv, 'r') as f:
        with open(output_json, 'w') as g:
            reader = csv.reader(f)
            writer = json.load(g)
            index = 0
            for line in reader:
                # Skip comment or info lines
                if line[0][0] == '#':
                    next(f)
                else:
                    line_dict = {index: line}
                    writer.update(line_dict)
                    json.dump(writer, g)
                    index += 1


if __name__ == "__main__":
    tojson(INPUT, OUTPUT)
    print(OUTPUT)
