import xml.etree.ElementTree as ET
import json

# Parse the XML document
document_path = 'nllb-en-sg.tmx'
tree = ET.parse(document_path)
root = tree.getroot()

# Initialize an empty list to store the translation pairs
translation_pairs = []

# Define the namespace map
namespaces = {'xml': 'http://www.w3.org/XML/1998/namespace'}

# Iterate over the 'tu' elements in the XML document
for tu in root.iter('tu'):
    # Find the 'tuv' elements with 'xml:lang' attributes of 'en' and 'sg'
    tuv_en = tu.find("tuv[@xml:lang='en']", namespaces)
    tuv_sg = tu.find("tuv[@xml:lang='sg']", namespaces)

    # Extract the text from the 'seg' child of each 'tuv' element
    en_text = tuv_en.find('seg').text
    sg_text = tuv_sg.find('seg').text

    # Add a dictionary with the English and Sango translations to the list
    translation_pairs.append({'en': en_text, 'sg': sg_text})

# Write the list of translation pairs to a JSON file
with open('nllb-en-sg_translation_pairs.json', 'w', encoding='utf-8') as f:
    json.dump(translation_pairs, f, ensure_ascii=False, indent=4)