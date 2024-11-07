import pwinput
import pandas as pd
from prettytable import PrettyTable
import os
import csv
import time
import sys
import json
from datetime import datetime
os.system("cls")

# ----------------------------------------- Import tabel dan CRUD! ---------------------------------------------

def tabel_obat():
    df = pd.read_csv('produkobat.csv')
    df = df.sort_values(by='Harga')  
    tabel_obat = PrettyTable()
    tabel_obat.field_names = df.columns.tolist()
    for index, row in df.iterrows():
        tabel_obat.add_row(row.tolist())
    print(tabel_obat)

def tabel_reguler():
    df = pd.read_csv('datapasienreguler.csv')
    df = df.sort_values(by='Umur')  
    tabel_reguler = PrettyTable()
    tabel_reguler.field_names = df.columns.tolist()
    for index, row in df.iterrows():
        tabel_reguler.add_row(row.tolist())
    print(tabel_reguler)

def tabel_bpjs():
    df = pd.read_csv('datapasienBPJS.csv')
    df = df.sort_values(by='Umur')  
    tabel_bpjs = PrettyTable()
    tabel_bpjs.field_names = df.columns.tolist()
    for index, row in df.iterrows():
        tabel_bpjs.add_row(row.tolist())
    print(tabel_bpjs)

def tabel_ruang():
    df = pd.read_csv('dataruangan.csv')
    df = df.sort_values(by='Harga')  
    tabel_ruang = PrettyTable()
    tabel_ruang.field_names = df.columns.tolist()
    for index, row in df.iterrows():
        tabel_ruang.add_row(row.tolist())
    print(tabel_ruang)

def tabel_jadwal():
    df = pd.read_csv('jadwaldokter.csv')
    tabel_jadwal = PrettyTable()
    tabel_jadwal.field_names = df.columns.tolist()
    for index, row in df.iterrows():
        tabel_jadwal.add_row(row.tolist())
    print(tabel_jadwal)

# ------------------------------------------- CRUD OBAT --------------------------------------------------

file_path = 'produkobat.csv'

def create_obat(file_path):

    nama = input("Masukkan nama obat     : ")
    harga = float(input("Masukkan harga obat    : "))

    df = pd.read_csv(file_path)
    
    new_data = [nama, harga]
    new_row = pd.DataFrame([new_data], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path, index=False)
    
    print(f"Obat {nama} berhasil ditambahkan ke data.")
    crud_obat()

def update_obat(file_path):
    nama_obat = input("Masukkan jenis obat yang ingin diperbarui: ")
    df = pd.read_csv(file_path)
    
    if nama_obat in df['Nama Obat'].values:

        nama_baru = input("Masukkan nama baru obat   : ")
        harga_baru = float(input("Masukkan harga baru       : "))

        df.loc[df['Nama Obat'] == nama_obat, ['Nama Obat', 'Harga']] = [nama_baru, harga_baru]
        df.to_csv(file_path, index=False)
        print(f"Data {nama_obat} berhasil diperbarui. Silahkan cek kembali.")
        crud_obat()
    else:
        print(f"Obat dengan nama {nama_obat} tidak ada dalam data. Masukkan nama obat yang tersedia.")
        update_obat(file_path)

def delete_obat(file_path):

    obat_name = input("Masukkan nama obat yang ingin dihapus: ")
    df = pd.read_csv(file_path)
    
    if obat_name in df['Nama Obat'].values:
        df = df[df['Nama Obat'] != obat_name]
        df.to_csv(file_path, index=False)
        print(f"Obat {obat_name} berhasil dihapus!")
    else:
        print(f"{obat_name} tidak ditemukan. Masukkan obat yang tersedia. ")
        delete_obat(file_path)

def crud_obat():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Tambah Data Obat                                    |")
    print("|   2. Lihat Data Obat                                     |")
    print("|   3. Hapus Data Obat                                     |")
    print("|   4. Perbarui Data Obat                                  |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == '1':
        create_obat(file_path)
    elif pilihan == '2':
        tabel_obat()
        crud_obat()
    elif pilihan == '3':
        delete_obat(file_path)
    elif pilihan == '4':
        update_obat(file_path)
    elif pilihan == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        crud_obat()

# ------------------------------------------- CRUD REG --------------------------------------------------

file_path1 = 'datapasienreguler.csv'

def create_reg(file_path1):
    nama_pasien = input("Masukkan nama pasien Reguler  : ")
    umur = int(input("Masukkan umur pasien          : "))
    penyakit = input("Masukkan jenis penyakit       : ")

    df = pd.read_csv(file_path1)

    new_data = [nama_pasien, umur, penyakit]
    new_row = pd.DataFrame([new_data], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path1, index=False)
    
    print(f"Pasien {nama_pasien} berhasil ditambahkan ke data.")
    crud_reg()

def update_reg(file_path1):
    nama_reg = input("Masukkan nama pasien yang ingin diperbarui: ")
    df = pd.read_csv(file_path1)
    
    if nama_reg in df['Nama Pasien Reguler'].values:

        nama_baru = input("Masukkan nama baru pasien BPJS    : ")
        umur_baru = int(input("Masukkan umur baru                : "))
        penyakit_baru = input("Masukkan penyakit baru            : ")

        df.loc[df['Nama Pasien Reguler'] == nama_reg, ['Nama Pasien Reguler', 'Umur', 'Penyakit']] = [nama_baru, umur_baru, penyakit_baru]
        df.to_csv(file_path1, index=False)
        
        print(f"Data pasien {nama_reg} berhasil diperbarui.")
        crud_reg()
    else:
        print(f"Pasien {nama_reg} tidak ditemukan. Masukkan nama yang tersedia.")
        update_reg(file_path1)

def delete_reg(file_path1):

    reg_name = input("Masukkan nama pasien yang ingin dihapus: ")
    df = pd.read_csv(file_path1)
    
    if reg_name in df['Nama Pasien Reguler'].values:
        df = df[df['Nama Pasien Reguler'] != reg_name]
        df.to_csv(file_path1, index=False)
        print(f"Pasien {reg_name} berhasil dihapus!")
        crud_reg()
    else:
        print(f"{reg_name} tidak ditemukan. Masukkan nama yang tersedia. ")
        delete_reg(file_path1)

def crud_reg():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Tambah Data Pasien Reguler                          |")
    print("|   2. Lihat Data Pasien Reguler                           |")
    print("|   3. Hapus Data Pasien Reguler                           |")
    print("|   4. Perbarui Data Pasien Reguler                        |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jwb_reg = input("Masukkan pilihan: ")
    if jwb_reg == '1':
        create_reg(file_path1)
    elif jwb_reg == '2':
        tabel_reguler()
        crud_reg()
    elif jwb_reg == '3':
        delete_reg(file_path1)
    elif jwb_reg == '4':
        update_reg(file_path1)
    elif jwb_reg == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        crud_reg()
# ------------------------------------------- CRUD REG --------------------------------------------------

file_path2 = 'datapasienBPJS.csv'

def create_bpjs(file_path2):
    nama_pasien = input("Masukkan nama pasien BPJS     : ")
    umur = int(input("Masukkan umur pasien          : "))
    penyakit = input("Masukkan jenis penyakit       : ")

    df = pd.read_csv(file_path2)

    new_data = [nama_pasien, umur, penyakit]
    new_row = pd.DataFrame([new_data], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path2, index=False)

    print(f"Pasien {nama_pasien} berhasil ditambahkan ke data.")
    crud_reg()

def update_bpjs(file_path2):
    nama_reg = input("Masukkan nama pasien yang ingin diperbarui: ")
    df = pd.read_csv(file_path2)
    
    if nama_reg in df['Nama Pasien BPJS'].values:

        nama_baru = input("Masukkan nama baru pasien BPJS    : ")
        umur_baru = int(input("Masukkan umur baru                : "))
        penyakit_baru = input("Masukkan penyakit baru            : ")

        df.loc[df['Nama Pasien BPJS'] == nama_reg, ['Nama Pasien BPJS', 'Umur', 'Penyakit']] = [nama_baru, umur_baru, penyakit_baru]
        df.to_csv(file_path2, index=False)
        
        print(f"Data pasien {nama_reg} berhasil diperbarui.")
    else:
        print(f"Pasien {nama_reg} tidak ditemukan. Masukkan nama yang tersedia.")
        update_bpjs(file_path2)

def delete_bpjs(file_path2):
    reg_name = input("Masukkan nama pasien yang ingin dihapus: ")
    df = pd.read_csv(file_path2)
    
    if reg_name in df['Nama Pasien BPJS'].values:

        df = df[df['Nama Pasien BPJS'] != reg_name]
        df.to_csv(file_path2, index=False)
        print(f"Pasien {reg_name} berhasil dihapus!")
    else:
        print(f"Pasien {reg_name} tidak ditemukan. Masukkan nama yang tersedia.")
        delete_bpjs(file_path2)

def crud_bpjs():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Tambah Data Pasien BPJS                             |")
    print("|   2. Lihat Data Pasien BPJS                              |")
    print("|   3. Hapus Data Pasien BPJS                              |")
    print("|   4. Perbarui Data Pasien BPJS                           |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jwb_bpjs = input("Masukkan pilihan: ")
    if jwb_bpjs == '1':
        create_bpjs(file_path2)
    elif jwb_bpjs == '2':
        tabel_bpjs()
        crud_bpjs()
    elif jwb_bpjs == '3':
        delete_bpjs(file_path2)
    elif jwb_bpjs == '4':
        update_bpjs(file_path2)
    elif jwb_bpjs == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        crud_bpjs()

# ------------------------------------------- CRUD Ruangan --------------------------------------------------

file_path3 = 'dataruangan.csv'

def create_ruang(file_path3):
    ruangan = input("Masukkan nomor ruangan                            : ")
    status = input("Masukkan status ruangan (Diisi/Kosong)            : ")
    kelas = input("Masukkan kelas ruangan (Kelas 1/2/3/VIP/VVIP)     : ")

    df = pd.read_csv(file_path3)

    new_data = [ruangan, status, kelas]
    new_row = pd.DataFrame([new_data], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path3, index=False)

    print(f"Ruang {ruangan} berhasil ditambahkan ke data.")
    crud_ruang()

def update_ruang(file_path3):
    ruangan = input("Masukkan nomor ruangan yang ingin diperbarui: ")
    df = pd.read_csv(file_path3)
    
    if ruangan in df['Ruangan'].values:

        ruangan_baru = input("Masukkan nomor ruangan baru               : ")
        status_baru = input("Masukkan status baru (Diisi/Kosong)       : ")
        kelas_baru = input("Masukkan kelas baru (Kelas 1/2/3/VIP/VVIP): ")

        df.loc[df['Ruangan'] == ruangan, ['Ruangan', 'Status', 'Kelas']] = [ruangan_baru, status_baru, kelas_baru]
        df.to_csv(file_path3, index=False)
        
        print(f"Data Ruang {ruangan} berhasil diperbarui.")
    else:
        print(f"Ruang {ruangan} tidak ada di data. Masukkan nomor ruangan yang tersedia.")
        update_ruang(file_path3)

def delete_ruang(file_path3):
    ruangan = input("Masukkan nomor ruangan yang ingin dihapus: ")
    df = pd.read_csv(file_path3)
    
    if ruangan in df['Ruangan'].values:
        df = df[df['Ruangan'] != ruangan]
        df.to_csv(file_path3, index=False)
        print(f"Ruang {ruangan} berhasil dihapus!")
    else:
        print(f"Ruang {ruangan} tidak ada di data. Masukkan nomor ruangan yang tersedia.")
        delete_ruang(file_path3)

def crud_ruang():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Tambah Data Ruangan                                 |")
    print("|   2. Lihat Data Ruangan                                  |")
    print("|   3. Hapus Data Ruangan                                  |")
    print("|   4. Perbarui Data Ruangan                               |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jwb_ruang = input("Masukkan pilihan: ")
    if jwb_ruang == '1':
        create_ruang(file_path3)
    elif jwb_ruang == '2':
        tabel_ruang()
        crud_ruang()
    elif jwb_ruang == '3':
        delete_ruang(file_path3)
    elif jwb_ruang == '4':
        update_ruang(file_path3)
    elif jwb_ruang == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        crud_ruang()

# ------------------------------------------- CRUD Jadwal Dokter --------------------------------------------------

file_path4 = 'jadwaldoktercsv'

def create_jadwal(file_path4):
    nama_dokter = input("Masukkan nama dokter                  : ")
    spesialis = input("Masukkan spesialis dokter             : ")
    jadwal = input("Masukkan jadwal praktik (e.g. Senin-Rabu) : ")

    df = pd.read_csv(file_path4)

    new_data = [nama_dokter, spesialis, jadwal]
    new_row = pd.DataFrame([new_data], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path4, index=False)

    print(f"Jadwal dokter {nama_dokter} berhasil ditambahkan.")
    crud_jadwal(file_path4)

def update_jadwal(file_path4):
    nama_dokter = input("Masukkan nama dokter yang ingin diperbarui: ")
    df = pd.read_csv(file_path4)
    
    if nama_dokter in df['Nama dokter'].values:
        nama_baru = input("Masukkan nama dokter baru                  : ")
        spesialis_baru = input("Masukkan spesialis baru                    : ")
        jadwal_baru = input("Masukkan jadwal praktik baru (e.g. Senin-Rabu) : ")

        df.loc[df['Nama dokter'] == nama_dokter, ['Nama dokter', 'Spesialis', 'Jadwal']] = [nama_baru, spesialis_baru, jadwal_baru]
        df.to_csv(file_path4, index=False)
        
        print(f"Jadwal dokter {nama_dokter} berhasil diperbarui.")
    else:
        print(f"Dokter {nama_dokter} tidak ditemukan. Masukkan nama yang tersedia.")
        update_jadwal(file_path4)

def delete_jadwal(file_path4):
    nama_dokter = input("Masukkan nama dokter yang ingin dihapus: ")
    df = pd.read_csv(file_path4)
    
    if nama_dokter in df['Nama dokter'].values:
        # Menghapus data dokter
        df = df[df['Nama dokter'] != nama_dokter]
        df.to_csv(file_path4, index=False)
        print(f"Jadwal dokter {nama_dokter} berhasil dihapus!")
    else:
        print(f"Dokter {nama_dokter} tidak ditemukan. Masukkan nama yang tersedia.")
        delete_jadwal(file_path4)

def crud_jadwal():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Tambah Data dan Jadwal Dokter                       |")
    print("|   2. Lihat Data dan Jadwal Dokter                        |")
    print("|   3. Hapus Data dan Jadwal Dokter                        |")
    print("|   4. Perbarui Data dan Jadwal Dokter                     |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jwb_jad = input("Masukkan pilihan: ")
    if jwb_jad == '1':
        create_jadwal(file_path4)
    elif jwb_jad == '2':
        tabel_jadwal()
        crud_jadwal()
    elif jwb_jad == '3':
        delete_jadwal(file_path4)
    elif jwb_jad == '4':
        update_jadwal(file_path4)
    elif jwb_jad == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        crud_jadwal()

# -------------------------------------------------------------------------------------

def exit():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|             Terima kasih sudah berkunjung!               |")
    print("╚══════════════════════════════════════════════════════════╝")

def loading(duration):
    for i in range(duration):
        sys.stdout.write(f"\r ── ⪼ {'»' * (i + 1)}{' ' * (duration - i - 1)} ── ⟢  {duration - i} detik tersisa untuk membuka blokir.")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\n")

json_path = "C:/Users/Asus GK/Documents/tea/datars.json"
with open(json_path, "r") as jsondatabase:
        data = json.loads(jsondatabase.read())

# ----------------------------------------- Menu-Menu! ---------------------------------------------

def menu_dokter():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|                  Layanan Dokter                          |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Lihat Jadwal Dokter                                 |")
    print("|   2. Lihat Data Pasien Reguler                           |")
    print("|   3. Lihat Data Pasien BPJS                              |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jawab_menudokter = input("Masukkan pilihanmu: ")
    if jawab_menudokter == '1':
        tabel_jadwal()
        menu_dokter()
    elif jawab_menudokter == '2':
        tabel_reguler()
        menu_dokter()
    elif jawab_menudokter == '3':
        tabel_bpjs()
        menu_dokter()
    else:
        print("Masukkan format yang benar.")
        menu_dokter()

def menu_perawat():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|                  Layanan Perawat                         |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Lihat Jadwal Dokter                                 |")
    print("|   2. Lihat Data Pasien Reguler                           |")
    print("|   3. Lihat Data Pasien BPJS                              |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jawab_menuper = input("Masukkan pilihanmu: ")
    if jawab_menuper == '1':
        tabel_jadwal()
        menu_perawat()
    elif jawab_menuper == '2':
        tabel_reguler()
        menu_perawat()
    elif jawab_menuper == '3':
        tabel_bpjs()
        menu_perawat()
    elif jawab_menuper == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        menu_perawat()

def menu_farmasi():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|                 Layanan Farmasi                          |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("|   1. Lihat Data Obat                                     |")
    print("|   2. Lihat Data Pasien                                   |")
    print("|   3. Lihat Data Pasien BPJS                              |")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jawab_menufarmasi = input("Masukkan pilihanmu: ")
    if jawab_menufarmasi == '1':
        tabel_obat()
        menu_farmasi()
    if jawab_menufarmasi == '2':
        tabel_reguler()
        menu_farmasi()
    if jawab_menufarmasi == '3':
        tabel_bpjs()
        menu_farmasi()
    elif jawab_menufarmasi == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        menu_farmasi()

# ----------------------------------------- Revisian Buat Akun  ---------------------------------------------

json_path = "datars.json"

def buat_akun():
    os.system("cls")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("|                 Buat Akun Pasien Reguler                     |")
    print("╚══════════════════════════════════════════════════════════════╝")

    nama_pasien = input("Nama Pasien: ")
    username = input("Buat Username: ")
    pin = input("Buat PIN: ")

    with open(json_path, "r") as jsondatabase:
        data = json.loads(jsondatabase.read())

    existing_usernames = [user["Username"] for user in data.get("Pasien_Reguler", [])]
    if username in existing_usernames:
        print("Username sudah terdaftar. Silakan buat username lain.")
        return

    new_patient = {
        "Nama_Pasien": nama_pasien,
        "Username": username,
        "PIN": pin,  
        "Saldo_EMoney": 0 
    }

    data.setdefault("Pasien_Reguler", []).append(new_patient)

    with open(json_path, "r") as jsondatabase:
        data = json.loads(jsondatabase.read())
        print("Data setelah akun ditambahkan.")

    print("Akun pasien reguler berhasil dibuat! Silahkan login!")
    awal()

def cek_saldo(user):
    saldo = user.get("Saldo_EMoney", 0)  
    print(f"Saldo E-Money Anda: {saldo}")

# ----------------------------------------- Revisian Login ---------------------------------------------

def login():

    def cek_saldo(user):
        saldo = user.get("Saldo_EMoney", 0)  
        print(f"Saldo E-Money Anda: {saldo}")

    os.system("cls")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("|                     Masukkan Data Anda!                      |")
    print("╚══════════════════════════════════════════════════════════════╝")

    with open(json_path, "r") as jsondatabase:
        data = json.loads(jsondatabase.read())

    anu = 3  
    error_count = 0  

    try:
        while True:  
            for i in range(anu):
                input_username = input("Username : ")
                input_pin = pwinput.pwinput(prompt="PIN : ")

                login_admin = data.get("Admin")
                if login_admin and input_username == login_admin.get("Username"):
                    if input_pin == login_admin.get("PIN"):
                        print("Login berhasil sebagai Admin!")
                        menu_admin()  
                        return  
                    else:
                        print("PIN Admin salah!")
                        error_count += 1

                for role in ["Dokter", "Apoteker", "Perawat"]:
                    login_users = data.get(role)
                    if login_users:
                        for user in login_users:
                            if input_username == user.get("Username"):
                                if input_pin == user.get("PIN"):
                                    print(f"Login berhasil sebagai {role} {user.get('Nama_Staff')}!")
                                    if role == "Dokter":
                                        menu_dokter()  
                                    elif role == "Apoteker":
                                        menu_farmasi()  
                                    elif role == "Perawat":
                                        menu_perawat()  
                                    return 
                                else:
                                    print(f"PIN untuk {role} salah!")
                                    error_count += 1

                login_reguler = data.get("Pasien_Reguler")
                if login_reguler:
                    for user in login_reguler:
                        if input_username == user.get("Username"):
                            if input_pin == user.get("PIN"):
                                print(f"Login berhasil sebagai Pasien Reguler {user.get('Nama_Pasien')}!")
                                username = input_username  
                                menu_pasien(username)  
                                return 
                            else:
                                print("PIN Pasien Reguler salah!")
                                error_count += 1


                login_bpjs = data.get("Pasien_BPJS")
                if login_bpjs:
                    for user in login_bpjs:
                        if input_username == user.get("Username"):
                            if (input_pin) == user.get("PIN"):
                                print(f"Login berhasil sebagai Pasien BPJS {user.get('Nama_Pasien')}!")
                                menu_bpjs() 
                                return 
                            else:
                                print("PIN Pasien BPJS salah!")
                                error_count += 1

                print("Data salah. Silakan coba lagi.")

                if error_count == 2:
                    print("Anda telah melakukan 2 kesalahan. Silakan coba lagi.")
                    error_count = 0 
                
                if i == anu - 1:
                    print("Anda telah melakukan percobaan 3 kali. Akses diblokir.")
                    loading(10)  
                    print("Silahkan masukkan data kembali.")
                    login() 

    except ValueError:
        print("Masukkan data yang benar.")
        awal()

# ----------------------------------------- Menu Administrasi! ---------------------------------------------

def menu_admin():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("|                     Layanan Resepsionis                      |")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("|   1. Kelola data pasien reguler                              |")
    print("|   2. Kelola data pasien BPJS                                 |")
    print("|   3. Kelola data obat                                        |")
    print("|   4. Kelola data dan jadwal dokter                           |")
    print("|   5. Kelola data ruangan                                     |")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                                 |")
    print("╚══════════════════════════════════════════════════════════════╝")
    jawab_admin = input("Masukkan pilihanmu: ")
    if jawab_admin == '1':
        tabel_reguler()
        crud_reg()
    elif jawab_admin == '2':
        tabel_bpjs()
        crud_bpjs()
    elif jawab_admin == '3':
        tabel_obat()
        crud_obat()
    elif jawab_admin == '4':
        tabel_jadwal()
        crud_jadwal()
    elif jawab_admin == '5':
        tabel_ruang()
        crud_ruang()
    elif jawab_admin == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        menu_admin()

# -------------------------------------- Menu Utama ---------------------------------------------------------

def wologin():
    print("============================================================")
    print("|          Hello, Guest! Silahkan pilih menu dibawah.      |")
    print("============================================================")
    print("|   1. Fasilitas & Layanan                                 |")
    print("|   2. Kontak RSUD                                         |")
    print("|   3. Daftar Layanan Poli                                 |")
    print("|   4. Daftar Kelas Rawat Inap                             |")
    print("|   5. Penunjang Medis                                     |")
    print("|   6. Kembali                                             |")
    print("|   0. Keluar                                              |")
    print("============================================================")
    without = input("Masukkan menu yang ingin Anda lihat: ")
    if without == "1":
        fasilitas()
    elif without == "2":
        kontak()
    elif without == "3":
        poli()
    elif without == "4":
        kelas()
    elif without == "5":
        penunjang()
    elif without == "6":
        awal()
    elif without == "0":
        exit()
    else:
        print("Masukkan format yang benar.")
        wologin()

def awal():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|               Selamat Datang di RSUD Samarinda!          |")
    print("|                 Silahkan pilih menu dibawah.             |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Buat Akun Pasien Reguler                            |")
    print("|   2. Login (Pasien, Dokter dan Staff)                    |")
    print("|   3. Lihat Informasi Lebih Lanjut                        |")
    print("|   0. Keluar                                              |")
    print("╚══════════════════════════════════════════════════════════╝")
    jawab = input("Pilihanmu: ")
    if jawab == '1':
        buat_akun()
    elif jawab == '2':
        login()
    elif jawab == '3':
        wologin()
    elif jawab == '0':
        exit()
    else:
        print("Masukkan format yang benar.")
        awal()

def kelas():
    print("============================================================")
    print("|              Layanan Kelas Rawat Inap                    |")
    print("============================================================")
    print("|   1. Ruangan VVIP                                        |")
    print("|   2. Ruangan VIP                                         |")
    print("|   3. Kelas I                                             |")
    print("|   4. Kelas II                                            |")
    print("|   5. Kelas III                                           |")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jawab_kelas = input("Masukkan pilihanmu: ")
    if jawab_kelas == '0':
        wologin()
    else:
        print("Masukkan format yang benar.")
        kelas()

def fasilitas():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|                 Fasilitas dan Layanan                    |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("|   1. Ambulance                                           |")
    print("|   2. Instalasi Gawat Darurat                             |")
    print("|   3. Farmasi                                             |")
    print("|   4. Bank Darah                                          |")
    print("|   5. Ruang Operasi                                       |")
    print("|   6. Stroke Center                                       |")
    print("|   7. Rehabilitasi Medis                                  |")
    print("|   8. Medical Check Up                                    |")
    print("|   9. Terapi                                              |")
    print("|   10. Bidan dan Perawat                                  |")
    print("|   11. Dokter Umum dan Spesialis                          |")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jawab_fasi = input("Masukkan pilihanmu: ")
    if jawab_fasi == '0':
        wologin()
    else:
        print("Masukkan format yang benar.")
        fasilitas()

def kontak(): 
    print("╔══════════════════════════════════════════════════════════╗")
    print("                    Hubungi kami!                           ")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Whatsapp      : 08121314151                         |")
    print("|   2. Instagram     : @RSUD_SMD                           |")
    print("|   3. Facebook      : @RSUD_SMD                           |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jawab_kontak = input("Masukkan pilihanmu: ")
    if jawab_kontak == '0':
        wologin()
    else:
        print("Masukkan format yang benar.")
        kontak()

def poli(): 
    print("╔══════════════════════════════════════════════════════════╗")
    print("|               Daftar Layanan Poli                        |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   1. Poliklinik Gigi dan Mulut                           |")
    print("|   2. Spesialis Penyakit Dalam                            |")
    print("|   3. Spesialis Kebidanan dan Kandungan                   |")
    print("|   4. Spesialis Anak                                      |")
    print("|   5. Spesialis Anestesi                                  |")
    print("|   6. Spesialis Bedah                                     |")
    print("|   7. Spesialis Mata                                      |")
    print("|   8. Spesialis THT                                       |")
    print("|   9. Spesialis Paru                                      |")
    print("|   10. Spesialis Saraf                                    |")
    print("|   11. Spesialis Kejiwaan                                 |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jawab_poli = input("Masukkan pilihanmu: ")
    if jawab_poli == '0':
        wologin()
    else:
        print("Masukkan format yang benar.")
        poli()

def penunjang():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|                 Penunjang Medis                          |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("|   1. Laboratorium                                        |")
    print("|   2. Radiologi (Rontgen)                                 |")
    print("|   3. Ultrasonografi (USG)                                |")
    print("|   4. Elektrokardiogram (EKG)                             |")
    print("|   5. Elektroensefalografi(EEG)                           |")
    print("|   6. Magnetic Resonance Imaging (MRI)                    |")
    print("|   7. Radiotrapi                                          |")
    print("|   8. Fisioterapi                                         |")
    print("|   9. Endoskopi                                           |")
    print("|   10. Hemodialisa                                        |")
    print("|   11. Kateterisasi Jantung (Cath Lab)                    |")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jawab_penunjang = input("Masukkan pilihanmu: ")
    if jawab_penunjang == '0':
        wologin()
    else:
        print("Masukkan format yang benar.")
        penunjang()

# -------------------------------------- Ilmu Persaldoan ----------------------------------------------------

def isi_saldo(username):
    os.system("cls")
    print("Anda akan mengisi saldo.")
    try:
        tarif = int(input("Masukkan tarif saldo yang ingin diisi: "))
        if tarif <= 0:
            print("Jumlah saldo harus lebih dari 0.")
            isi_saldo(username)

        confirm = input(f"Konfirmasi pengisian Rp.{tarif:,} saldo? (y/n): ")
        if confirm.lower() == "y":
            found = False
            for user in data["Pasien_Reguler"]:
                if user["Username"] == username:
                    user["Saldo_EMoney"] += tarif
                    with open(json_path, "w") as jsondatabase:
                        json.dump(data, jsondatabase, indent=4)
                    print(f"Isi saldo berhasil. Saldo Anda sekarang: Rp.{user['Saldo_EMoney']:,}")
                    found = True
                    menu_pasien(username)
                    break
            if not found:
                print("Username tidak ditemukan.")
        else:
            print("Pengisian saldo dibatalkan.")
            menu_pasien()
    except ValueError:
        print("Masukan harus berupa angka.")
        menu_pasien()

def cek_saldo(username):
    os.system("cls")

    found = False
    for user in data["Pasien_Reguler"]:
        if user["Username"] == username:

            print(f"Nama Pasien     : {user['Nama_Pasien']}")
            print(f"Saldo EMoney    : Rp.{user['Saldo_EMoney']:,}")
            menu_pasien(username)
            found = True
            break
    
    if not found:
        print("Username tidak ditemukan.")
        menu_pasien(username) 

def baca_obat_dari_csv(file_csv):
    daftar_obat = []
    with open(file_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            daftar_obat.append({"Nama Obat": row["Nama Obat"], "Harga": float(row["Harga"])})
    return daftar_obat

def beli_obat(username):
    os.system("cls")
    tabel_obat()  
    nama_obat_pilih = input("Masukkan nama obat yang ingin dibeli: ").lower()  
    daftar_obat = baca_obat_dari_csv('produkobat.csv') 
    obat_terpilih = None

    for obat in daftar_obat:
        if obat["Nama Obat"].lower() == nama_obat_pilih.lower():
            obat_terpilih = obat
            break

    if obat_terpilih:
        harga_obat = obat_terpilih["Harga"]
        nama_obat = obat_terpilih["Nama Obat"]

        konfirmasi = input(f"Anda akan membeli {nama_obat} seharga Rp.{harga_obat:,}. Lanjutkan pembelian? (y/n): ").lower()
        if konfirmasi == 'y': 
            found = False
            for user in data["Pasien_Reguler"]:
                if user["Username"] == username:
                    if user["Saldo_EMoney"] >= harga_obat:

                        user["Saldo_EMoney"] -= harga_obat
                        sisa_saldo = user["Saldo_EMoney"]

                        print(f"Anda telah membeli {nama_obat} seharga Rp.{harga_obat:,}.")
                        print(f"Sisa saldo Anda: Rp.{sisa_saldo:,}")

                        current_time = datetime.now()
                        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                        invoice_content = invoice_obat(formatted_time, harga_obat, username, nama_obat)

                        invoice_path = "C:/Users/Asus GK/Documents/tea/invoice_obat.txt"
                        with open(invoice_path, "a") as invoice_file:
                            invoice_file.write(invoice_content + "\n")
                        print(invoice_content)

                        with open(json_path, "w") as jsondatabase:
                            json.dump(data, jsondatabase, indent=4)

                        menu_pasien(username)  
                    else:
                        print(f"Saldo Anda tidak mencukupi untuk membeli {nama_obat}.")
                        beli_obat(username)
                    found = True
                    break

            if not found:
                print("Username tidak ditemukan.")
        else:
            print("Pembelian dibatalkan.")  
            menu_pasien(username)
    else:
        print("Obat dengan nama tersebut tidak tersedia.")
        menu_pasien(username)

def baca_ruang_dari_csv(file_csv):
    daftar_ruang = []
    with open(file_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            daftar_ruang.append({
                "Ruangan": int(row["Ruangan"]),
                "Kelas": row["Kelas"],
                "Harga": float(row["Harga"]),
                "Status": row["Status"]
            })
    return daftar_ruang

def pesan_ruangan(username):
    os.system("cls")
    tabel_ruang() 

    daftar_ruang = baca_ruang_dari_csv('dataruangan.csv')

    try:
        ruangan_input = int(input("Masukkan nomor ruangan yang ingin Anda pesan: "))
        
        ruangan_terpilih = next((ruang for ruang in daftar_ruang if ruang["Ruangan"] == ruangan_input and ruang["Status"] == "Kosong"), None)

        if ruangan_terpilih:
            harga_ruangan = ruangan_terpilih["Harga"]
            kelas_ruangan = ruangan_terpilih["Kelas"]

            print(f"Anda telah memilih ruangan {ruangan_input} dengan kelas {kelas_ruangan}.")
            print(f"Harga untuk kelas {kelas_ruangan} adalah Rp.{harga_ruangan:,}.")

            konfirmasi = input(f"Konfirmasi pemesanan ruangan {ruangan_input}? (y/n): ").lower()
            if konfirmasi == 'y':
                found = False
                for user in data["Pasien_Reguler"]:
                    if user["Username"] == username:
                        if user["Saldo_EMoney"] >= harga_ruangan:
                            user["Saldo_EMoney"] -= harga_ruangan
                            print(f"Anda telah berhasil memesan ruangan {ruangan_input} dengan kelas {kelas_ruangan}.")
                            print(f"Sisa saldo Anda: Rp.{user['Saldo_EMoney']:,}")

                            current_time = datetime.now()
                            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                            invoice_content = invoice_ruangan(formatted_time, harga_ruangan, username, kelas_ruangan)

                            invoice_path = "C:/Users/Asus GK/Documents/tea/invoice_ruangan.txt"
                            with open(invoice_path, "a") as invoice_file:
                                invoice_file.write(invoice_content + "\n")
                            print(invoice_content)

                            with open(json_path, "w") as jsondatabase:
                                json.dump(data, jsondatabase, indent=4)

                            menu_pasien(username)
                            found = True
                            break
                        else:
                            print(f"Saldo Anda tidak mencukupi untuk memesan ruangan {ruangan_input}.")
                            menu_pasien(username)
                            found = True
                            break

                if not found:
                    print("Username tidak ditemukan.")
            else:
                print("Pemesanan ruangan dibatalkan.")
                menu_pasien(username)
        else:
            print("Ruangan tidak ditemukan atau tidak tersedia.")
            menu_pasien(username)
    except ValueError:
        print("Masukkan nomor ruangan yang valid.")
        menu_pasien(username)

def baca_jadwal_dari_csv(file_csv):
    daftar_jadwal = []
    with open(file_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            daftar_jadwal.append({
                "Nama Dokter": row["Nama dokter"],   
                "Spesialis": row["Spesialis"],       
                "Jadwal": row["Jadwal"],             
            })
    return daftar_jadwal

def pesan_dokter(username):

    daftar_jadwal = baca_jadwal_dari_csv('jadwaldokter.csv')  

    try:
        spesialis_input = input("Masukkan spesialis yang ingin Anda temui: ").lower()

        dokter_terpilih = next((dokter for dokter in daftar_jadwal if spesialis_input in dokter["Spesialis"].lower()), None)

        if dokter_terpilih:
            nama_dokter = dokter_terpilih["Nama Dokter"]
            spesialis = dokter_terpilih["Spesialis"]
            jadwal = dokter_terpilih["Jadwal"]

            print(f"Anda telah memilih {nama_dokter}, spesialis {spesialis}.")
            print(f"Jadwal praktek: {jadwal}.")

            konfirmasi = input(f"Konfirmasi pemesanan konsultasi dengan {nama_dokter}? (y/n): ").lower()
            if konfirmasi == 'y':
                print(f"Anda telah memesan jadwal dengan {nama_dokter}, spesialis {spesialis} di hari {jadwal}.")
                menu_pasien(username)
            else:
                print("Pemesanan konsultasi dibatalkan.")
                menu_pasien(username)
        else:

            print(f"Spesialis '{spesialis_input}' tidak ditemukan. Silakan coba lagi.")
            pesan_dokter(username)  
    except ValueError:
        print("Masukkan spesialis yang valid.")
        menu_pasien(username)

def menu_pasien(username):
    print("╔══════════════════════════════════════════════════════════╗")
    print("|                 Layanan Pasien                           |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("|   1. Cek Saldo                                           |")
    print("|   2. Isi Saldo                                           |")
    print("|   3. Beli obat                                           |")
    print("|   4. Pesan ruangan                                       |")
    print("|   5. Ajukan pertemuan dengan Dokter                      |")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jwb_menupasien = input("Masukkan pilihanmu: ")
    if jwb_menupasien == '1':
        cek_saldo(username)
    elif jwb_menupasien == '2':
        isi_saldo(username)
    elif jwb_menupasien == '3':
        beli_obat(username)
    elif jwb_menupasien == '4':
        pesan_ruangan(username)
        print("pesan room")
    elif jwb_menupasien == '5':
        tabel_jadwal()
        pesan_dokter(username)
    elif jwb_menupasien == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        menu_pasien(username)

# ----------------------------------------------- BPJS AREA ---------------------------------------------------------

def ajuan_obat():
    input_obat = input("Masukkan nama obat yang ingin Anda pesan: ").lower()
    if input_obat == "paracetamol":
        jawab = input("Anda akan menemui mengajukan pembelian obat paracetamol. Konfirmasi? (y/n): ")
        if jawab == "y":
            print("Anda bisa mengambilnya di apotek.")
            menu_bpjs()
        elif jawab == "n":
            print("Pengajuan dibatalkan.")
            menu_bpjs()
        else:
            print("Masukkan data yang valid, ulangi pesanan.")
            ajuan_obat()
    elif input_obat == "antibiotik":
        jawab = input("Anda akan menemui mengajukan pembelian obat antibiotik. Konfirmasi? (y/n): ")
        if jawab == "y":
            print("Anda bisa mengambilnya di apotek.")
            menu_bpjs()
        elif jawab == "n":
            print("Pengajuan dibatalkan.")
            menu_bpjs()
        else:
            print("Masukkan data yang valid, ulangi pesanan.")
            ajuan_obat()
    elif input_obat == "aspirin":
        jawab = input("Anda akan menemui mengajukan pembelian obat aspirin. Konfirmasi? (y/n): ")
        if jawab == "y":
            print("Anda bisa mengambilnya di apotek.")
            menu_bpjs()
        elif jawab == "n":
            print("Pengajuan dibatalkan.")
            menu_bpjs()
        else:
            print("Masukkan data yang valid, ulangi pesanan.")
            ajuan_obat()
    else:
        print("Obat tidak tersedia. Coba cek kembali.")
        menu_bpjs()

def ajuan_ruang():
    input_ruang = input("Masukkan nama obat yang ingin Anda pesan: ").lower()
    if input_ruang == "paracetamol":
        jawab = input("Anda akan menemui mengajukan pembelian obat paracetamol. Konfirmasi? (y/n): ")
        if jawab == "y":
            print("Anda bisa mengambilnya di apotek.")
            menu_bpjs()
        elif jawab == "n":
            print("Pengajuan dibatalkan.")
            menu_bpjs()
        else:
            print("Masukkan data yang valid, ulangi pesanan.")
            ajuan_obat()
    elif input_ruang == "antibiotik":
        jawab = input("Anda akan menemui mengajukan pembelian obat antibiotik. Konfirmasi? (y/n): ")
        if jawab == "y":
            print("Anda bisa mengambilnya di apotek.")
            menu_bpjs()
        elif jawab == "n":
            print("Pengajuan dibatalkan.")
            menu_bpjs()
        else:
            print("Masukkan data yang valid, ulangi pesanan.")
            ajuan_obat()
    elif input_ruang == "aspirin":
        jawab = input("Anda akan menemui mengajukan pembelian obat aspirin. Konfirmasi? (y/n): ")
        if jawab == "y":
            print("Anda bisa mengambilnya di apotek.")
            menu_bpjs()
        elif jawab == "n":
            print("Pengajuan dibatalkan.")
            menu_bpjs()
        else:
            print("Masukkan data yang valid, ulangi pesanan.")
            ajuan_obat()
    else:
        print("Obat tidak tersedia. Coba cek kembali.")
        menu_bpjs()

def ajuan_ruang():
    ruangan = {}
    with open("dataruangan.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            ruangan[row["Ruangan"]] = {
                "status": row["Status"],
                "kelas": row["Kelas"],
                "harga": int(row["Harga"])
            }
    
    input_ruang = input("Masukkan nomor ruangan yang ingin Anda pesan: ")

    if input_ruang in ruangan:
        if ruangan[input_ruang]["status"].lower() == "kosong":

            jawab = input(f"Anda akan memesan ruangan {input_ruang} ({ruangan[input_ruang]['kelas']}) dengan harga Rp{ruangan[input_ruang]['harga']}. Konfirmasi? (y/n): ")
            if jawab.lower() == "y":
                print(f"Ruangan {input_ruang} berhasil dipesan.")
                menu_bpjs()
            elif jawab.lower() == "n":
                print("Pengajuan dibatalkan.")
                menu_bpjs()
            else:
                print("Masukkan data yang valid, ulangi pemesanan.")
                ajuan_ruang()
        else:
            print("Ruangan tidak tersedia.")
            menu_bpjs()
    else:
        print("Nomor ruangan tidak valid. Silakan coba lagi.")
        ajuan_ruang()

def ajuan_dokter():
    dokter = {}
    with open("jadwaldokter.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dokter[row["Nama dokter"]] = {
                "spesialis": row["spesialis"],
                "jadwal": row["Jadwal"]
            }

    input_dokter = input("Masukkan nama dokter yang ingin Anda temui: ").capitalize()

    if input_dokter in dokter:

        spesialis = dokter[input_dokter]["spesialis"]
        jadwal = dokter[input_dokter]["jadwal"]
        jawab = input(f"Anda akan menemui {input_dokter}, spesialis {spesialis} dengan jadwal hari {jadwal}. Konfirmasi? (y/n): ")
        
        if jawab.lower() == "y":
            print(f"Janji temu dengan {input_dokter} berhasil dibuat.")
            menu_bpjs()
        elif jawab.lower() == "n":
            print("Pengajuan dibatalkan.")
            menu_bpjs()
        else:
            print("Masukkan data yang valid, ulangi pemesanan.")
            ajuan_dokter()
    else:
        print("Nama dokter tidak ditemukan. Silakan coba lagi.")
        ajuan_dokter()

def menu_bpjs():
    print("╔══════════════════════════════════════════════════════════╗")
    print("|                   Layanan BPJS                           |")
    print("╚══════════════════════════════════════════════════════════╝")
    print("|   1. Ajukan pemberian obat                               |")
    print("|   2. Ajukan pemesanan ruangan                            |")
    print("|   3. Ajukan pertemuan dengan Dokter                      |")
    print("╔══════════════════════════════════════════════════════════╗")
    print("|   0. Kembali                                             |")
    print("╚══════════════════════════════════════════════════════════╝")
    jwb_menubpjs = input("Masukkan pilihanmu: ")
    if jwb_menubpjs == '1':
        tabel_obat()
        ajuan_obat()
    elif jwb_menubpjs == '2':
        tabel_ruang()
        ajuan_ruang()
    elif jwb_menubpjs == '3':
        tabel_jadwal()
        ajuan_dokter()
    elif jwb_menubpjs == '0':
        awal()
    else:
        print("Masukkan format yang benar.")
        menu_bpjs()

def invoice_ruangan(formatted_time, harga_ruangan, username, kelas_ruangan):
    invoice_content = f"===== Detail Invoice =====\n"
    invoice_content += f"Waktu pemesanan: {formatted_time}\n"
    invoice_content += f"Harga: Rp.{harga_ruangan:,}\n"
    invoice_content += f"Ruangan: {kelas_ruangan}\n"
    invoice_content += f"Pembeli: {username}\n"
    invoice_content += f"===========================\n"
    invoice_content += f"Terimakasih telah memesan.\n"
    return invoice_content

def invoice_obat(formatted_time, harga_obat, username, nama_obat):
    invoice_content = f"===== Detail Invoice =====\n"
    invoice_content += f"Waktu pemesanan: {formatted_time}\n"
    invoice_content += f"Harga: Rp.{harga_obat:,}\n"
    invoice_content += f"Obat: {nama_obat}\n"
    invoice_content += f"Pembeli: {username}\n"
    invoice_content += f"===========================\n"
    invoice_content += f"Terimakasih telah memesan.\n"
    return invoice_content

awal()
