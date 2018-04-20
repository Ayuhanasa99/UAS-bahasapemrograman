def kalkulator():
    print("\n\t=============================")
    print("\tProgram Kalkulator Sederhana")
    print("\t=============================")
    print("\n\t1. Penjumlahan")
    print("\n\t2. Pengurangan")
    print("\n\t3. Perkalian")
    print("\n\t4. Pembagian")
    print("\t=============================")
    print("\n\tSilahkan pilih 1-4")
    print(" ")
    pilih = input("\tMasukan Pilihan : ")
    if pilih == "1":
        tambah()
    if pilih == "2":
        kurang()
    if pilih == "3":
        kali()
    if pilih == "4":
        bagi()
    else:
        print("\tPilihan Anda Tidak Tersedia !")
        print("\tSilahkan Ulangi Kembali !")
        tanya()
        
def tambah():
    print("\t1. Penjumlahan")
    a = int(input("\tx = "))
    b = int(input("\ty = "))
    ab = a+b
    print("\tx+y=",ab)
    tanya()
def kurang():
    print("\t2. Pengurangan")
    a = int(input("\tx = "))
    b = int(input("\ty = "))
    ab = a-b
    print("\tx-y=",ab)
    tanya()
def kali():
    print("\t3. Perkalian")
    a = int(input("\tx = "))
    b = int(input("\ty = "))
    ab = a*b
    print("\tx*y=",ab)
    tanya()
def bagi():
    print("\t4. Pembagian")
    a = int(input("\tx = "))
    b = int(input("\ty = "))
    ab = a/b
    print("\ta/b=",ab)
    tanya()

def tanya():
    tanya = input("\n\tKembali Ke Menu Kalkulator ? (y/n)")
    if tanya == "y":
        kalkulator()
    elif tanya == "n":
        exit
    else:
        print ("\n\tMaaf Pilihan Yang Anda Masukan Tidak Tersedia !")

kalkulator()
