import json

# Read JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Write JSON file
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
file_path = './data/test.json'

# Read JSON file
json_data = read_json_file(file_path)
print(json_data)

# Modify JSON data
json_data['key'] = 'value'

# Write JSON file
write_json_file(file_path, json_data)