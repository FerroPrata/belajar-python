import json
from prettytable import PrettyTable

with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
    dataa = json.load(f)

data = list(dataa.items())

def buble_sort():
    a = 0
    array = data
    n = len(array) 
    for i in range(n):
        for j in range(n - i - 1): 
            if array[j][1]["jarak"] > array[j + 1][1]["jarak"]:                
                a += 1
                array[j], array[j + 1] = array[j + 1], array[j]
                bukun = [buku[1]['jarak'] for buku in data] 
                print(f"step ke {a} : {bukun}, iterasi ke {i + 1}")
    return array

buble_sort()

table = PrettyTable()
table.field_names = ["nama warung", "jarak"]
for buku in buble_sort():
    table.add_row([buku[0], buku[1]['jarak']])
print(table)