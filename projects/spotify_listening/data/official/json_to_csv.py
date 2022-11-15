# import statements
import csv
import json

# streaming history
json_data = 'projects\spotify_listening\data\official\StreamingHistory0.json'
csv_conv = 'projects\spotify_listening\data\official\official_stats_1_year.csv'

input = open(json_data, encoding='utf8')
output = open(csv_conv, 'w', encoding='utf8')
data = json.load(input)
input.close()

new_csv = csv.writer(output)

new_csv.writerow(data[0].keys()) 
for r in data:
    new_csv.writerow(r.values())