import matematika as mt

print("PI",  mt.pi)
print(mt.luas_lingkaran(radius=21))
print(mt.luas_persegi(sisi=12))
print(mt.luas_segitiga(alas=20, tinggi=10))

# import tanpa manggil
print()
from matematika import *
print(luas_lingkaran(21))
print(luas_persegi(12))
print(luas_segitiga(20, 10))


# import 1 def
print()
from matematika import luas_persegi as luli
print(luli(20))
