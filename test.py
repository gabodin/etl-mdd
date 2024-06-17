import json

# Path to the JSON file
json_file_path = './utils/ufs.json'

# Open and read the JSON file directly into a dictionary
with open(json_file_path, 'r') as file:
    data_dict = json.load(file)

# Print the dictionary to verify
print(data_dict)
