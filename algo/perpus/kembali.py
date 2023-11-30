import json
from data import tes as ts


def kmb(a):
    # Call the function to get an instance of the Tes class
    ts_instance = ts()

    if a in ts_instance.buku:
        if ts_instance.buku[a]["tersedia"] < ts_instance.buku[a]["total"]:
            # Pengembalian buku
            ts_instance.buku[a]["tersedia"] += 1
            print(f"Buku {a} berhasil dikembalikan.")
        else:
            print(f"Maaf, stok buku {a} sudah penuh.")
    else:
        print(f"Buku {a} tidak valid atau tidak sedang dipinjam.")

    # Save the updated data to the file
    with open('/backup data 2023/optional/belajar python/algo/perpus/data_buku.json', 'w') as file:
        # Use ts_instance.buku directly to update and write to the file
        json.dump(ts_instance.buku, file, indent=2)

    # Print the updated dictionary
    for i, data in ts_instance.buku.items():
        print(i, data["tersedia"])