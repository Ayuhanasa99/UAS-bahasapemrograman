import getpass
from texttable import Texttable
def menu():
    print("====================================")
    print("\n\t-----Pilihan Utama-----")
    print("\n\t1. Penilaian Mahasiswa")
    print("\n\t2. Pembayaran Mahasiswa")
    print("\n\t3. Kalkulator")

    pilih = input("\n\tSilahkan Pilih : ")
    if pilih == "1" :
        from perhitungan.penilaian_mahasiswa import nilai_mahasiswa
    elif pilih == "2" :
        from perhitungan.pembayaran_mahasiswa import pembayaran
    elif pilih == "3" :
        from perhitungan.kalkulator import kalkulator
    else :
        exit
    tanya()

def tanya():
    tanya=input("\n\tKembali Ke Pilihan Utama (y/n) ? ")
    if tanya == "y" :
        menu()
    elif tanya == "n" :
        exit
    else :
        print("Pilihan Yang Anda Masukan Tidak Tersedia !")

user = input("\nUsername : ")
password = getpass.getpass()
print("======================================")

if user == "ayu hana" and password == "1234":
    menu()
else :
    print("Maaf Username Atau Password Salah !")
