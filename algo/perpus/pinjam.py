import json
from data import tes as ts

def pj(a):
    # Call the function to get an instance of the Tes class
    ts_instance = ts()

    # Assuming ts_instance.buku is a dictionary where the values represent the quantity of each book
    if a in ts_instance.buku:
        if ts_instance.buku[a]["tersedia"] > 0:
            # Peminjaman buku
            ts_instance.buku[a]["tersedia"] -= 1
            print(f"Buku {a} berhasil dipinjam.")
        else:
            print(f"Maaf, stok buku {a} habis.")
    else:
        print(f"Buku {a} tidak tersedia.")

    # Print the updated dictionary
    for i, jumlah in ts_instance.buku.items():
         print(f"{i} Tersedia: {jumlah['tersedia']}")

    # Update the JSON file
    with open('/backup data 2023/optional/belajar python/algo/perpus/data_buku.json', 'w') as file:
        # Use ts_instance.buku directly to update and write to the file
        json.dump(ts_instance.buku, file, indent=2)