# Rename File dengan Direktori yang Berbeda
import os

# Kalian bisa merubah nama path atau lokasi dimana file kalian disimpan
daftar_file = os.listdir('F:\\Youtube Lokal\Kelas Terbuka\\Tutorial Django Python')

for i in range(len(daftar_file)):
    file = daftar_file[i]
    nama_baru = file.replace('y2mate.com - ', '')
    os.replace('F:\\Youtube Lokal\Kelas Terbuka\\Tutorial Django Python\\'+file, 'F:\\Youtube Lokal\Kelas Terbuka\\Tutorial Django Python\\'+nama_baru)