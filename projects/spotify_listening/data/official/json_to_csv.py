# import statements
import csv
import json

# streaming history
input = 'projects\spotify_listening\data\official\StreamingHistory0.json'
output = 'projects\spotify_listening\data\official\official_stats_1_year.csv'

data = open(input, encoding='utf8')
new_csv = open(output, 'w', encoding='utf8')
loaded_data = json.load(data)
data.close()

out1 = csv.writer(new_csv)

out1.writerow(loaded_data[0].keys()) 
for r in loaded_data:
    out1.writerow(r.values())