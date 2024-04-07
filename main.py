# Module main
# Description: This module contains the main function which reads a CSV file
# containing temperature readings and converts them to the desired unit


import csv
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

def convert_temperatures(filename, target_unit):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        data = list(reader)

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Reading'])  # Write the header

        for row in data:
            date, reading = row
            temp, unit = reading[:-2], reading[-2:]

            if unit == '°F' and target_unit == 'C':
                temp = fahrenheit_to_celsius(float(temp))
                unit = '°C'
            elif unit == '°C' and target_unit == 'F':
                temp = celsius_to_fahrenheit(float(temp))
                unit = '°F'

            writer.writerow([date, f'{temp:.2f}{unit}'])

if __name__ == "__main__":
    convert_temperatures('input.csv', 'C')  # Convert all temperatures to Celsius