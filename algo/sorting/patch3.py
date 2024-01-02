import json
from prettytable import PrettyTable

with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
    dataa = json.load(f)

data = list(dataa.items())

def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if data[j][1]["rekomendasi"] > data[max_idx][1]["rekomendasi"]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]
        
selection_sort(data)

table = PrettyTable()
table.field_names = ["Nama Rumah Makan", "Rekomendasi"]

for nama, info in data:
    table.add_row([nama, info['rekomendasi']])

print(table)