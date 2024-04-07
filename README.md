# Temperature and Distance Converter

This project contains a Python script that reads a CSV file containing distance and temperature readings and converts them to the desired units.

## Description

The main function, `convert_temperatures`, takes in a filename, target distance unit, and target temperature unit. It reads the CSV file, skips the header, and stores the data in a list. For each row in the data, it extracts the date, distance, and temperature reading. It then uses regular expressions to separate the numerical part and the unit part of the distance and temperature. Depending on the target units specified, it converts the distance and temperature using the appropriate conversion functions. The converted data is then written to a new CSV file named `output.csv`.

## Installation

Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/polinaya777/Git_Converter
cd git_converter
```

## Usage

Run the script with Python.

```bash
python main.py
```
By default, the script will convert all distances to meters and temperatures to Celsius. You can modify the convert_temperatures function call in the `if __name__ == "__main__"` block to convert to different units.

## Contributing

Contributions are always welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the terms of the MIT license.