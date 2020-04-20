import pandas as pd
import json
import requests
import csv 
import os


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

f=pd.read_csv("data_file.csv")
keep_col = ['totalconfirmed','totaldeceased']
new_f = f[keep_col]
new_f.to_csv("newFile.csv", index=False)

with open("newFile.csv", 'r') as input, open('result.csv', 'w') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')

    all = []
    row = next(reader)
    row.insert(0, 'ID')
    all.append(row)
    count = 0
    for row in reader:
        row.insert(0, count)
        count += 1
        all.append(row)
    writer.writerows(all)

os.remove("data.json")
os.remove("data_file.csv")
os.remove("newFile.csv")

with open('result.csv', 'r') as fin:
    data = fin.read().splitlines(True)
with open('result.csv', 'w') as fout:
    fout.writelines(data[1:])
