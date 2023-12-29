import random
import time
def buble_sort():
    a = 0
    array = angka_random = [random.randint(1, 100) for i in range(20)]
    print(array)
    start = time.time()
    n = len(array) #jumlah list
    for i in range(n): #perluangan pertama
        for j in range(n - i - 1): #perulangan kedua
            # bandingkan masing masing element 
            if array[j] > array[j + 1]:                
                # jika lebih besar, tukar
                a +=1
                array[j], array[j + 1] = array[j + 1], array[j]
                print(f"step ke {a} : {array} iterasi ke-{i + 1}")
    # print(array)
    end = time.time()
    elapsed = end- start
    print(f"{elapsed:.6f}")

                
    return array

buble_sort()