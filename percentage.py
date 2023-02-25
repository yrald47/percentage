import requests
import math
import time
import pandas as pd

LINE_UP = '\33[1A'
CLEAR_CURRENT_LINE = '\x1b[2K'

response = requests.get('https://indonesia-public-static-api.vercel.app/api/heroes')
heroes = response.json() 

# STEP ANIMASI SEDERHANA PERSENTASE
# Tentukan banyak dot untuk progress bar, misal 50
bar = 50
# Hitung total data yang ingin di-load
total_progress = len(response.json())
# KEMANA PERGINYA FILE INI
path = "D:/PROJECT/Iseng2"
filename = "pahlawan.csv"
f = open(path+"/"+filename, 'w', 0o777)

# TULIS HEADER
header = "LOAD DATA API PAHLAWAN INDONESIA"
print(header + "\n" + "="*len(header) + "\n")
f.write("NAMA;TAHUN LAHIR;TAHUN MENINGGAL;TAHUN KENAIKAN;DESKRIPSI\n")
# Masuk perulangan
for current_progress in range(total_progress + 1):
    # Hitung persentase
    percentage = current_progress/total_progress*100
    # Karena 100 persen = 50 tanda "." untuk progress bar, maka 1 "." = 2 persen
    # Bulantkan ke bawah, karena ya persentase, mau 79,8% tetep hitungannya 79%, berguna juga untuk memperjelas penentuan jumlah titik sebagai progress bar
    progress = math.floor(percentage)
    # Tentukan jumlah titik per 2 persen sebagai progress bar
    dot = int(progress/2) if progress % 2 == 0 else int((progress - 1)/2)
    # Tentukan sisanya, yaitu spasi = total bar (50) - progress bar
    space = bar - dot

    # Masukkan ke dalam csv untuk melihat hasilnya
    if current_progress < total_progress:
        f.write(heroes[current_progress]['name'] + ";" + str(heroes[current_progress]['birth_year']) + ";" + str(heroes[current_progress]['death_year']) + ";" + str(heroes[current_progress]['ascension_year']) + ";" + heroes[current_progress]['description'] + "\n")
    
    # Tampilkan current progress
    prog = str(current_progress) + "/" + str(total_progress) + " heroes loaded [" + "."*dot + " "*space + "] " + str("{:.2f}".format(percentage)) + "%"
    print(prog, end = "\r")
    
    time.sleep(0.001) #karena data cuma 191, progressnya ga keliatan, jadi di-sleep dikit

    # print(CLEAR_CURRENT_LINE, LINE_UP)
    print(CLEAR_CURRENT_LINE, LINE_UP)
# f.close()
# Pertahankan progress terakhir
print(prog)
print("DONE, RESULTS WRITE IN " + path + "/" + filename)
