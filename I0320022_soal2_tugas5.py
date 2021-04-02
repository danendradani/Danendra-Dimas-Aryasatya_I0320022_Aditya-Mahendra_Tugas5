# input
nama = input("Masukkan nama anda : ")
nilai = int(input("Masukkan nilai anda : "))

# memeriksa nilai
if nilai > 100:
    print("Nilai anda tidak valid")
elif nilai >= 85:
    konversi = "A"
    print("Halo", nama, "!", "Nilai anda setelah dikonversi adalah", konversi)
elif nilai >= 80:
    konversi = "A-"
    print("Halo", nama, "!", "Nilai anda setelah dikonversi adalah", konversi)
elif nilai >= 75:
    konversi = "B+"
    print("Halo", nama, "!", "Nilai anda setelah dikonversi adalah", konversi)
elif nilai >= 70:
    konversi = "B"
    print("Halo", nama, "!", "Nilai anda setelah dikonversi adalah", konversi)
elif nilai >= 65:
    konversi = "C+"
    print("Halo", nama, "!", "Nilai anda setelah dikonversi adalah", konversi)
elif nilai >= 60:
    konversi = "C"
    print("Halo", nama, "!", "Nilai anda setelah dikonversi adalah", konversi)
else:
    konversi = "E"
    print("Halo", nama, "!", "Nilai anda setelah dikonversi adalah", konversi)