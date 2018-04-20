from texttable import Texttable

def nilai_mahasiswa():
    table = Texttable()
    jawab = "y"
    no = 0
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    while(jawab == "y"):
        nama.append(input ("Masukan Nama : "))
        nim.append(input ("Masukan NIM : "))
        nilai_tugas.append(input ("Nilai Tugas : "))
        nilai_uts.append(input ("Nilai UTS : "))
        nilai_uas.append(input ("Nilai UAS : "))
        jawab = input("Tambah Data (y/n)?")
        no += 1
    for i in range(no):
        tugas = int(nilai_tugas[i])
        uts = int(nilai_uts[i])
        uas = int(nilai_uas[i])
        akhir = (tugas + uts + uas)/3
        table.add_rows([['No','Nama','NIM','Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'],
                        [i+1, nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])
    print (table.draw() )
nilai_mahasiswa()
