import random
import datetime

nama = input("nama: ")
tujuan = input("tujuan: ")

nomor = random.randint(1,100)

print("nomor tiket:", nomor)

if nomor <= 50:
    print("silakan tunggu dipanggil")
else:
    print("antrian masih panjang")

print("tanggal:", datetime.date.today())

