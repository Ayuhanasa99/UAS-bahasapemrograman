def pembayaran():
    print("\n====================================")
    nama = input("\n\tMasukan Nama : ")
    nim = input("\tMasukan NIM : ")
    semester = input("\tMasukan Semester Sekarang : ")
    print("\n\t----pilihan pembayaran----")
    print("\t1. Pembayaran SPP")
    print("\t2. Pembayaran UAS")
    print("\t3. Pembayaran UTS")
    print("\t4. Pembayaran SPP & UAS")
    print ("\t5. Pembayaran SPP & UTS")
    pilih = input("\n\tSilahkan Pilih : ")
    if pilih == "1" :
        spp()
    elif pilih == "2" :
        uas()
    elif pilih == "3" :
        uts()
    elif pilih == "4" :
        spp_uas()
    elif pilih == "5" :
        spp_uts()
    else:
        exit
        tanya()

def spp():
    bulan = int(input("\n\tJumlah Bulan Yang Akan Dibayar : "))
    bulan = float(bulan)
    total = 500000 * bulan
    print("=================================================")
    print("\tTotal Pembayaran SPP Rp. 500000 * ",bulan," = Rp. ",total)
    tanya()
    
def uas():
    matkul_uas = int(input("\n\tJumlah Mata Kuliah : "))
    matkul_uas = float(matkul_uas)
    total = 50000 * matkul_uas
    print("==================================================")
    print("\tTotal Pembayaran UAS Rp.50000 * ",matkul_uas," = Rp.",total)
    tanya()
    
def uts():
    matkul_uts = int(input("\n\tJumlah Mata Kuliah : "))
    matkul_uts = float(matkul_uts)
    total = 50000 * matkul_uts
    print("==================================================")
    print("\tTotal Pembayaran UTS Rp.50000 * ",matkul_uts," = Rp.",total)
    tanya()
    
def spp_uas():
    bulan = int(input("\n\tJumlah Bulan Yang Akan Dibayar : "))
    matkul = int(input("\tJumlah Mata Kuliah : "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp =500000 * bulan
    byr_uas = 50000 * matkul
    total = total_spp + byr_uas + 5000
    print("\n\tTotal Bayar SPP Rp.50000 *",bulan," = Rp.",total_spp)
    print("\tTotal Bayar UAS Rp.50000 *",matkul," = Rp.",byr_uas)
    print("\tBiaya Tambahan Server Sebesar Rp.5000")
    print("==================================================")
    print("\tTotal Pembayaran SPP & UAS Rp.",total)
    tanya()
    
def spp_uts():
    bulan = int(input("\n\tJumlah Bulan Yang Akan Dibayar : "))
    matkul = int(input("\tJumlah Mata Kuliah : "))
    matkul = float(matkul)
    bulan = float(bulan)
    total_spp = 500000 * bulan
    byr_uts = 50000 * matkul
    total = total_spp + byr_uts + 5000
    print("\n\tTotal Bayar UTS Rp.50000 *",matkul," = Rp.",byr_uts)
    print("\tTotal Bayar SPP Rp.500000 * ",bulan," = Rp.",total_spp)
    print("\tBiaya Tambahan Server Sebesar Rp.5000")
    print("===================================================")
    print("\tTotal Pembayaran SPP & UTS Rp.",total)
    tanya()
    
def tanya():
    tanya = input("Apakah Ingin Melakukan Pembayaran Lagi (y/n) ? ")
    if tanya == "y" :
        pembayaran()
    elif tanya == "n" :
        exit
    else :
        print("\n\tMaaf Pilihan Tidak Tersedia !")

pembayaran()
