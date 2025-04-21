#!/bin/bash

# Update MCC/MNC tables script
# This script updates the CSV, JSON, and XML files with the latest data from mcc-mnc.com

# Check if BeautifulSoup is installed
if ! python -c "import bs4" &> /dev/null; then
    echo "BeautifulSoup is not installed. Installing..."
    pip install -r requirements.txt
fi

echo "Updating MCC/MNC tables..."

# Update CSV file
echo "Updating CSV file..."
python get-mcc-mnc-table-csv.py > mcc-mnc-table.csv
if [ $? -eq 0 ]; then
    echo "CSV file updated successfully."
else
    echo "Error updating CSV file."
    exit 1
fi

# Update JSON file
echo "Updating JSON file..."
python get-mcc-mnc-table-json.py > mcc-mnc-table.json
if [ $? -eq 0 ]; then
    echo "JSON file updated successfully."
else
    echo "Error updating JSON file."
    exit 1
fi

# Update XML file
echo "Updating XML file..."
python get-mcc-mnc-table-xml.py > mcc-mnc-table.xml
if [ $? -eq 0 ]; then
    echo "XML file updated successfully."
else
    echo "Error updating XML file."
    exit 1
fi

echo "All MCC/MNC tables have been updated successfully."