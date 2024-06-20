import os
import json
import glob

def count_items_in_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return len(data)



def concatenate_json_files(directory):
    json_files = glob.glob(os.path.join(directory, '*.json'))
    all_data = []
    for file in json_files:
        with open(file, 'r') as f:
            data = json.load(f)
            all_data.extend(data)

    with open(f'data/final/final_from_{os.path.basename(directory)}.json', 'w') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

def remove_en_keys(file_path):
    # Load the data from the file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Remove the 'en' key from each item
    for item in data:
        if 'en' in item:
            del item['en']

    # Write the modified data back to the file
    with open(file_path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    directory = 'data/json/centrafrique.sango.free.fr'
    
    file_path = 'data/json/japprendslesango.json'
    num_items = count_items_in_json(file_path)
    print(f'Number of items in {file_path}: {num_items}')

    # file_path = 'data/json/lexilogos.com/lexilogos_translations.json'
    # num_items = count_items_in_json(file_path)
    # print(f'Number of items in {file_path}: {num_items}')