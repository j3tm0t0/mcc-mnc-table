# Get the Mobile Country Codes (MCC) and Mobile Network Codes (MNC) table
# from mcc-mnc.com and output it in JSON format.

import urllib.request
from bs4 import BeautifulSoup
import json

with urllib.request.urlopen('http://mcc-mnc.com/') as f:
    html = f.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the table with MCC/MNC data
    table = soup.find('table')
    
    mcc_mnc_list = []
    
    if table:
        # Process each row in the table (skip header row)
        for row in table.find_all('tr')[1:]:  # Skip header row
            cells = row.find_all('td')
            if len(cells) >= 6:  # Ensure we have enough cells
                current_item = {}
                current_item['mcc'] = cells[0].text.strip()
                current_item['mnc'] = cells[1].text.strip()
                current_item['iso'] = cells[2].text.strip()
                current_item['country'] = cells[3].text.strip()
                current_item['country_code'] = cells[4].text.strip()
                current_item['network'] = cells[5].text.strip()
                
                mcc_mnc_list.append(current_item)
    else:
        print("Error: Could not find table in the HTML")
        
    print(json.dumps(mcc_mnc_list, indent=2))
