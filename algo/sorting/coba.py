import json
import time
import random


with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
        dataa = json.load(f)

hasil = list(dataa.keys())

tahun_terbit_list = [buku["tahun_terbit"] for buku in dataa.values()]


print(tahun_terbit_list)


data = tahun_terbit_list
def insertion_sort(data):
    a = 0
    waktuM = time.time()
    for i in range(1, len(data)): # perulangan pertama
        key_item = data[i] # ini elemen yang akan kita posisikan
        j = i - 1 # kunci index posisi
        while j >= 0 and data[j] > key_item: # lakukan perulangan kedua
            data[j + 1] = data[j] # menggeser elemen yang lain
            j -= 1
            data[j + 1] = key_item # memposisikan elemen
            print(f"step ke-{a} : {data}, iterasi ke-{i}")
            a += 1

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}' )

    return data

print("Hasil dari Insertion Sort adalah ",insertion_sort(data))


