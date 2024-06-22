import json
import os

input_directory = "/home/blackarch/syste/desk/local_interactables"  

output_file = "local.txt"

def read_json_files(directory):
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            name = os.path.splitext(filename)[0]
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                try:
                    file_data = json.load(file)
                    data_list.append({name: file_data})
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in {filename}")
    return data_list

result_data = read_json_files(input_directory)

with open(output_file, "w") as output:
    output.write(json.dumps(result_data, indent=4))

print(f"Data from JSON files written to {output_file}")