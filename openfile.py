import json
def read_file_int(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        row = list(map(int,line.strip().split(',')))
        data.append(row)
    return data
import json

import json

import json

import json

def text_to_json(file_path):
    # Open the text file
    with open(file_path, 'r') as file:
        # Read the contents of the file
        contents = file.read()

    # Split the contents into lines
    lines = contents.split('\n')

    # Create a dictionary to store the data
    data = {}

    # Loop through the lines and add them to the dictionary
    for line in lines:
        if ':' in line:
            key, value = line.split(':')
            data[key.strip()] = value.strip()

    # Convert the dictionary to a JSON object
    json_data = json.dumps(data)

    # Return the JSON object
    return json_data
# l = read_file('blocks_population.txt')
l = text_to_json('problem_config.txt')
print(l)