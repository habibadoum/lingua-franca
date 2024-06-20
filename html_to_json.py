import json
from bs4 import BeautifulSoup

def html_to_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.select('table tbody tr')
    data = []
    
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            fr_text = cells[0].get_text(strip=True)
            sg_text = cells[1].get_text(strip=True)
            data.append({"fr": fr_text, "sg": sg_text})
        elif len(cells) == 3:
            fr_text = cells[0].get_text(strip=True)
            sg_text = cells[1].get_text(strip=True)
            data.append({"fr": fr_text, "sg": sg_text})
            examples_fr_sg = cells[2].get_text(strip=True).split(":")
            if len(examples_fr_sg) == 2:
                example_fr = examples_fr_sg[0].strip()
                example_sg = examples_fr_sg[1].strip()
                data.append({"fr": example_fr, "sg": example_sg})

    return data

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    data = html_to_json(html_content)
    
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_file = 'japprendslesango.html'
    output_file = 'data/json/japprendslesango.json'
    main(input_file, output_file)
