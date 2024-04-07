# Module main
# Description: This module contains the main function which reads a CSV file
# containing distance and temperature readings and converts them to the desired units.


import csv
import re
from convertor.distance import meters_to_feet, feet_to_meters
from convertor.temperature import fahrenheit_to_celsius, celsius_to_fahrenheit

def convert_temperatures(filename, target_dist_unit, target_temp_unit):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        data = list(reader)

    with open('output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Distance', 'Reading'])  # Write the header

        for row in data:
            date, distance, reading = row
            dist, dist_unit = float(re.search(r'\d+\.?\d*', distance)[0]), re.search(r'[a-zA-Z]+', distance)[0]
            temp, temp_unit = float(re.search(r'\d+\.?\d*', reading)[0]), re.search(r'°[CF]', reading)[0]

            if dist_unit == 'ft' and target_dist_unit == 'm':
                dist = feet_to_meters(dist)
                dist_unit = 'm'
            elif dist_unit == 'm' and target_dist_unit == 'ft':
                dist = meters_to_feet(dist)
                dist_unit = 'ft'

            if temp_unit == '°F' and target_temp_unit == 'C':
                temp = fahrenheit_to_celsius(temp)
                temp_unit = '°C'
            elif temp_unit == '°C' and target_temp_unit == 'F':
                temp = celsius_to_fahrenheit(temp)
                temp_unit = '°F'

            writer.writerow([date, f'{dist:.2f}{dist_unit}', f'{temp:.2f}{temp_unit}'])

if __name__ == "__main__":
    # Convert all temperatures to Celsius and distances to meters
    convert_temperatures('input.csv', 'm', 'C')