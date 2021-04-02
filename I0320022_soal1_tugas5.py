# input
nama = input("Masukkan nama anda : ")
jenis_kelamin = input("Masukkan jenis kelamin anda (L/P) : ")
print()

# memeriksa jenis kelamin
if jenis_kelamin == "L" or jenis_kelamin == "l":
    sebut = "Tuan"
    print("Selamat datang", sebut, nama)
else:
    sebut = "Nyonya"
    print("Selamat datang", sebut, nama)