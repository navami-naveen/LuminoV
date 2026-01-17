
import xml.etree.ElementTree as ET
import json
import os

base_path = 'temp_xlsx/xl/'
shared_strings_path = os.path.join(base_path, 'sharedStrings.xml')
sheet_path = os.path.join(base_path, 'worksheets/sheet1.xml')

# 1. Parse sharedStrings.xml
print("Parsing sharedStrings.xml...")
tree = ET.parse(shared_strings_path)
root = tree.getroot()
# Namespaces
ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
shared_strings = []
for si in root.findall('main:si', ns):
    t = si.find('main:t', ns)
    if t is not None:
        shared_strings.append(t.text)
    else:
        # Handle cases with multiple r (rich text)
        texts = si.findall('.//main:t', ns)
        shared_strings.append("".join([x.text for x in texts if x.text]))

# 2. Parse sheet1.xml
print("Parsing sheet1.xml...")
tree = ET.parse(sheet_path)
root = tree.getroot()
sheet_data = root.find('main:sheetData', ns)

occupations = {}

# Column indices (from sharedStrings analysis)
# 0: O*NET-SOC Code
# 1: Title
# 3: Element Name
# 6: Data Value

def get_cell_value(cell):
    v = cell.find('main:v', ns)
    if v is None:
        return None
    val = v.text
    if cell.get('t') == 's':
        return shared_strings[int(val)]
    return val

rows = sheet_data.findall('main:row', ns)
header_row = rows[0]
headers = {}
for cell in header_row.findall('main:c', ns):
    ref = cell.get('r')
    col = ''.join([i for i in ref if not i.isdigit()])
    headers[col] = get_cell_value(cell)

print(f"Headers: {headers}")

riasec_map = {
    "Realistic": "R",
    "Investigative": "I",
    "Artistic": "A",
    "Social": "S",
    "Enterprising": "E",
    "Conventional": "C"
}

for row in rows[1:]:
    cells = row.findall('main:c', ns)
    data = {}
    for cell in cells:
        ref = cell.get('r')
        col = ''.join([i for i in ref if not i.isdigit()])
        val = get_cell_value(cell)
        data[headers[col]] = val
    
    title = data.get('Title')
    element = data.get('Element Name')
    value = data.get('Data Value')
    
    if title and element in riasec_map and value is not None:
        if title not in occupations:
            occupations[title] = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}
        occupations[title][riasec_map[element]] = float(value)

# 3. Simplify and filter
# We want the top occupations for each trait
top_occupations = {trait: [] for trait in "RIASEC"}
for title, scores in occupations.items():
    # Find the top trait for this occupation
    max_trait = max(scores, key=scores.get)
    max_val = scores[max_trait]
    if max_val > 0:
        top_occupations[max_trait].append({"title": title, "score": max_val})

# Sort and take top 10 for each
for trait in top_occupations:
    top_occupations[trait].sort(key=lambda x: x['score'], reverse=True)
    top_occupations[trait] = [x['title'] for x in top_occupations[trait][:10]]

with open('occupations_data.json', 'w') as f:
    json.dump(top_occupations, f, indent=2)

print("Extraction complete. Saved to occupations_data.json")
