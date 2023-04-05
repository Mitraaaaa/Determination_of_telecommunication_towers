import json

def read_file_int(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        row = list(map(int,line.strip().split(',')))
        for number in row:
            data.append(number)
    return data

def text_to_json(file_path):
    json_data = None
    with open(file_path) as f:
        json_data = json.load(f)
    # Return the JSON object
    return json_data

def read_files():
    blocks_population = read_file_int('blocks_population.txt')
    problem_config = text_to_json('problem_config.txt')    
    return blocks_population, problem_config