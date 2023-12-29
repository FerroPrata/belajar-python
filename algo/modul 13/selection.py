import random
import time
data = [random.randint(1, 100) for i in range(20)]

def sort():
    n = len(data)
    a = 0
    print(f"nilai awal : {data} \n")
    print("ascending")
    start = time.time()
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[min_idx] > data[j]:
                a += 1
                min_idx = j
                data[i], data[min_idx] = data[min_idx], data[i]
                print(f"step ke {a} : {data} iterasi ke-{i + 1}")
    end = time.time()
    elapsed = end- start
    print(f"waktu {elapsed:.6f}")
    print()
    return data

def sortd():
    n = len(data)
    a = 0
    print(f"nilai awal : {data} \n")
    print("descending")
    start = time.time()
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[min_idx] < data[j]:
                a += 1
                min_idx = j
                data[i], data[min_idx] = data[min_idx], data[i]
                print(f"step ke {a} : {data} iterasi ke-{i + 1}")
    end = time.time()
    elapsed = end- start
    print(f"waktu {elapsed:.6f}")
    return data
sort()
sortd()
