import json
from tabulate import tabulate

# Input file containing the JSON data
input_file = "automatedoverlays.txt"

def read_data_from_file(file_path):
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print(f"Error decoding JSON data in {file_path}")
            return None

# Read data from the input file
data = read_data_from_file(input_file)

if data:
    # Display each dictionary as a table
    for item in data:
        for key, value in item.items():
            print(f"Table for {key}:")
            if isinstance(value, list):
                headers = value[0].keys() if value else []
                rows = [list(item.values()) for item in value]
                print(tabulate(rows, headers, tablefmt="pretty"))
            else:
                print(tabulate(value.items(), tablefmt="pretty"))
            print("\n" + "-" * 40 + "\n")
else:
    print("No data to display.")
