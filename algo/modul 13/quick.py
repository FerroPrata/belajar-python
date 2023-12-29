import random

def quick_sort(my_list, awal, akhir, move_count):
    if awal < akhir:
        pindex = partisi(my_list, awal, akhir, move_count)
        quick_sort(my_list, awal, pindex - 1, move_count)  
        quick_sort(my_list, pindex + 1, akhir, move_count)  

def partisi(my_list, awal, akhir, move_count):
    pivot = my_list[akhir]  
    pindex = awal
    for i in range(awal, akhir):  
        move_count[0] += 1 
        if my_list[i] <= pivot:  
            my_list[i], my_list[pindex] = my_list[pindex], my_list[i]
            pindex += 1
        print(f"step ke-{move_count} : {my_list}")

    my_list[pindex], my_list[akhir] = my_list[akhir], my_list[pindex]  
    return pindex

my_list = [random.randint(1, 100) for i in range(20)]
move_count = [0]  

quick_sort(my_list, 0, len(my_list) - 1, move_count)



