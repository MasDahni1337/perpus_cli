import zerodata
import os
import sys
from tabulate import tabulate

def awal():
    print('''
     _______________
< Selamat datang di Perpustakan Zeromind >
< 0_0 >
< hehehe yang penting enjoy kawan ... >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
----------------------------
< cari saja buku sesukamu ... >
    ''')
    print("[1] Data buku")
    print("[2] Cari buku")
    print("[3] Tambah buku")
    print("[4] Update buku")
    print("[5] Hapus buku")

def milihapa():
    milihapa = int(input("Yuk dipilih : "))
    return milihapa

def pilihmenu():
    awal()
    tunyok = milihapa()
    eksekusi = zerodata.hayuk.execute
    while tunyok !=7:
        if tunyok==1:
            databuku = "select * from buku"
            eksekusi(databuku)
            hasilnya = zerodata.hayuk.fetchall()
            if hasilnya is None:
                print("belum ada data")
            else:
                kepala = ['No', 'Judul Buku', 'Kode Buku']
                print("No          Kode Buku                      Judul Buku")
                for inihasil in hasilnya:
                    nmrs = inihasil[0]
                    jd_b = inihasil[1]
                    kd_b = inihasil[2]
                    print(nmrs, end='           ')
                    print(kd_b, end='                     ')
                    print(jd_b)
            break
        elif tunyok==2:
            mau = input("mau nyari buku apa? : ")
            cari = "select * from buku where judul = '{}'".format(mau)
            eksekusi(cari)
            hasilnya = zerodata.hayuk.fetchall()
            if hasilnya is None:
                print("belum ada data")
            else:
                for ygdicari in hasilnya:
                    print(ygdicari)
            break
        elif tunyok==3:
            print("silahkan tambahkan buku")
            judul = input("judul buku : ")
            while True:
                kode_B = input("kode buku : ")
                if len(kode_B) <= 4 :
                    print("harus 5 karakter")
                elif len(kode_B) >= 6:
                    print("harus 5 karakter")
                else:
                    break
            masukinB = "insert into buku (judul, kode_buku) values (%s, %s)"
            isinya = (judul, kode_B)
            eksekusi(masukinB, isinya)
            zerodata.cekdb.commit()
            print("Berhasil tambahkan data buku berjudul {} dengan kode buku {}".format(judul, kode_B))
            break
        elif tunyok==4:
            print("silahkan perbarui data")
            ini_id = int(input("nomer berapa : "))
            ubahjudul = input("perbaharui judul buku : ")
            while True:
                buku_kode = input("perbaharui kode buku : ")
                if len(buku_kode) <= 4 :
                    print("harus 5 karakter")
                elif len(buku_kode) >= 6:
                    print("harus 5 karakter")
                else:
                    break
            ubah_data = "update buku set judul=%s, kode_buku=%s where buku_id=%s"
            isi_data = (ubahjudul, buku_kode, ini_id)
            eksekusi(ubah_data, isi_data)
            zerodata.cekdb.commit()
            print("Berhasil tambahkan data buku nomer {} dengan judul {} dan kode buku {}".format(ini_id, ubahjudul, buku_kode))
            break
        elif tunyok==5:
            print("silahkan hapus data")
            hps_id = int(input("mau hapus nomer berapa : "))
            hps_data = "delete from buku where buku_id=%s"
            hps_isi = (hps_id, )
            eksekusi(hps_data, hps_isi)
            zerodata.cekdb.commit()
            print("Berhasil hapus data nomer {}".format(hps_id))
            return pilihmenu()
        else:
            print("masukin yang bener dong sayang")
            break

pilihmenu()
