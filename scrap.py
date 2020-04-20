import json
import requests
import csv 


solditems = requests.get('https://api.covid19india.org/data.json') # (your url)
data = solditems.json()
with open('data.json', 'w') as f:
    json.dump(data, f,indent=4)

with open('data.json') as json_file: 
    data = json.load(json_file) 
cases=data['cases_time_series']

data_file = open('data_file.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0
  
for case in cases: 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = case.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(case.values()) 
  
data_file.close() 
