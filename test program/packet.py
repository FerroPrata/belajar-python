import os
import hashlib
import time
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def hash_file(file_path):
    """Menghitung hash SHA-256 dari suatu file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Baca file dalam blok 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def collect_file_info(file_path):
    """Mengumpulkan informasi tentang suatu file."""
    if os.path.exists(file_path):
        file_info = {
            'File Path': file_path,
            'Size (bytes)': os.path.getsize(file_path),
            'Last Modified Time': time.ctime(os.path.getmtime(file_path)),
            'Hash (SHA-256)': hash_file(file_path),
            'Latitude': None,
            'Longitude': None
        }

        # Coba ambil informasi lokasi dari metadata Exif
        try:
            with Image.open(file_path) as img:
                exif_data = img._getexif()
                if exif_data is not None:
                    for tag, value in exif_data.items():
                        tag_name = TAGS.get(tag, tag)
                        if tag_name == 'GPSInfo':
                            for key in value.keys():
                                sub_tag_name = GPSTAGS.get(key, key)
                                file_info[sub_tag_name] = value[key]

        except (AttributeError, KeyError, IndexError):
            pass

        return file_info

    else:
        return None

def search_file(file_name):
    """Mencari lokasi file di sistem."""
    for root, dirs, files in os.walk('/'):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def main():
    # Ganti dengan nama file yang ingin dicari
    target_file_name = 'WIN_20231024_23_36_11_Pro.jpg'

    # Cari lokasi file
    target_file_path = search_file(target_file_name)

    if target_file_path:
        print(f"File ditemukan di lokasi: {target_file_path}")
        
        # Kumpulkan informasi tentang file
        file_info = collect_file_info(target_file_path)

        if file_info:
            print("\nInformasi File:")
            for key, value in file_info.items():
                print(f"{key}: {value}")
    else:
        print("File tidak ditemukan.")

if __name__ == "__main__":
    main()
