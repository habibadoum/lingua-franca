import json

# Load the JSON file
with open('data/json/japprendslesango.json', 'r') as f:
    data = json.load(f)

# Reverse the order of the keys
# Assuming data is a list of dictionaries
for i in range(len(data)):
    data[i] = {k: data[i][k] for k in reversed(data[i].keys())}

# Write the result back to the file
with open('data/json/japprendslesango.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)