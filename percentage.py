import requests
import math
import time
import pandas as pd
from sty import fg, bg, ef, rs
from sty import Style, RgbFg, RgbBg

# ANIMASI SEDERHANA PERSENTASE PROGRESS BAR
LINE_UP = '\33[1A'
CLEAR_CURRENT_LINE = '\x1b[2K'

response = requests.get('https://indonesia-public-static-api.vercel.app/api/heroes')
heroes = response.json() 

bar = 50 # Banyak dot untuk progress bar, 100 % = 50 tanda ".", 1 "." mewakili 2%
total_progress = len(response.json()) # Hitung total data yang ingin di-load
path = "D:/PROJECT/Iseng2"
filename = "pahlawan.csv"
f = open(path+"/"+filename, 'w', 0o777) # Open a file and set permission to 777

header = "LOAD DATA API PAHLAWAN INDONESIA" # Pemanis
print(header + "\n" + "="*len(header) + "\n") # Tampilkan header diikuti garis di bawahnya 
f.write("NAMA;TAHUN LAHIR;TAHUN MENINGGAL;TAHUN KENAIKAN;DESKRIPSI\n") # Tulis Header Row untuk file csv

for current_progress in range(total_progress + 1):
    percentage = current_progress/total_progress*100 # Jumlah data yang di-load per total data yang akan di-load dikali 100
    progress = math.floor(percentage) # Bulantkan ke bawah, karena ya persentase, mau 79,8% tetep hitungannya 79%, berguna juga untuk memperjelas penentuan jumlah titik sebagai progress bar
    dot = int(progress/2) if progress % 2 == 0 else int((progress - 1)/2) # Tentukan jumlah titik per 2 persen sebagai progress bar
    space = bar - dot # Tentukan sisanya, yaitu spasi = total bar (50) - progress bar

    # Masukkan ke dalam csv untuk melihat hasilnya
    if current_progress < total_progress:
        f.write(heroes[current_progress]['name'] + ";" + str(heroes[current_progress]['birth_year']) + ";" + str(heroes[current_progress]['death_year']) + ";" + str(heroes[current_progress]['ascension_year']) + ";" + heroes[current_progress]['description'] + "\n")
        print(heroes[current_progress]['name'])
    
    fg.orange = Style(RgbFg(255, 150, 50)) # declare orange color
    bg.orange = Style(RgbBg(255, 150, 50)) # declare orange color
    colored_dot = bg.orange + fg.orange + "."*dot + fg.rs + bg.rs
    if percentage == 100.0:
        colored_dot = bg.blue + fg.blue + "."*dot + fg.rs + bg.rs
    elif percentage >= 90.0:
        colored_dot = bg.green + fg.green + "."*dot + fg.rs + bg.rs
    elif percentage >= 50.0:
        colored_dot = bg.yellow + fg.yellow + "."*dot + fg.rs + bg.rs
        

    prog = str(current_progress) + "/" + str(total_progress) + " heroes loaded [" + colored_dot + " "*space + "] " + str("{:.2f}".format(percentage)) + "%"
    print(prog, end = "\r") # Tampilkan current progress
    time.sleep(0.025) # Karena data cuma 191, progressnya kecepetan, ga keliatan, jadi di-sleep dikit

    print(CLEAR_CURRENT_LINE, LINE_UP, CLEAR_CURRENT_LINE, end = "\r") # CLEAR CURRENT LINE. LINE UP, THEN \n
# f.close()
print("\n" + prog) # Pertahankan status progres terakhir
print("DONE, RESULTS WRITE IN " + path + "/" + filename)