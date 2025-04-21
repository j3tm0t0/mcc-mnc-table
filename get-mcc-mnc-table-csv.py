# Get the Mobile Country Codes (MCC) and Mobile Network Codes (MNC) table
# from mcc-mnc.com and output it in CSV format.

import urllib.request
from bs4 import BeautifulSoup

print("MCC,MCC (int),MNC,MNC (int),ISO,Country,Country Code,Network")

with urllib.request.urlopen('http://mcc-mnc.com/') as f:
    html = f.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the table with MCC/MNC data
    table = soup.find('table')
    
    if table:
        # Process each row in the table (skip header row)
        for row in table.find_all('tr')[1:]:  # Skip header row
            cells = row.find_all('td')
            if len(cells) >= 6:  # Ensure we have enough cells
                mcc = cells[0].text.strip()
                mnc = cells[1].text.strip()
                iso = cells[2].text.strip()
                country = cells[3].text.strip().replace(',', '')
                country_code = cells[4].text.strip()
                network = cells[5].text.strip().replace(',', '')
                
                # Calculate MCC (int)
                mcc_int = str(int(mcc, 16)) if mcc.isalnum() else mcc
                
                # Calculate MNC (int)
                mnc_int = ""
                if mnc.isalnum() and mnc != "n/a":
                    if len(mnc) == 2:
                        mnc_int = str(int(mnc + 'f', 16))
                    else:
                        mnc_int = str(int(mnc, 16))
                else:
                    mnc_int = mnc
                
                # Construct CSV line
                csv_line = f"{mcc},{mcc_int},{mnc},{mnc_int},{iso},{country},{country_code},{network}"
                print(csv_line)
    else:
        print("Error: Could not find table in the HTML")
