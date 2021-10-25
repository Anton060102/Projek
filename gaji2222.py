#-------------------------------------------
#Program		: Enployee Income 
#Kelompok		: IV (Empat)
#kelas			: 17.1A.25
#Mata Kuliah	: Dasar Pemrograman
#-------------------------------------------

print("-------------------------------------")
print("======= PROGRAM GAJI KARYAWAN =======")
print("-------------------------------------")
nama = input("NAMA KARYAWAN : ")
tgl = input("Tanggal sekarang (dd/mm/yyyy) : ")

menu="y"
while menu is "y":
    print("=============================================")
    print("                 PROGRAM GAJI                  ")
    print("LIST JABATAN") 
    print("=============================================")
    print("A. OPERATOR")
    print("B. SUPERVISOR")
    print("C. MANAJER0")
    print("D. DIREKTUR")
    print("=============================================")
    opsi=input("masukan list abjad jabatan anda  =")
    if opsi == "a" :
        jab= "operator"
        gapok=200000
        lembur=50000
        
    elif opsi == "b" :
            jab= "supervisor"
            gapok=400000
            lembur=70000
    elif opsi == "c" :
            jab= "manajer"
            gapok=600000
            lembur=90000
    elif opsi == "d" :
            jab= "direktur"
            gapok=1000000
            lembur=200000
            
    else:
        opsi == "-"
        jab="-"
        gapok="-"
        lembur="-"
        menu=input("Opsi tidak tersedia, silahkan masukan list abjad jabatan anda yang tersedia ulangi kembali Y/N =")
                
    print("")
    print("")
    print("--------------------------------------")
    print("=========== GAJI KARYAWAN ============")
    print("--------------------------------------")
    print("Nama : ",nama)
    print("Tanggal/bulan/tahun :", tgl)
    print("opsi:", opsi)
    print("Jabatan :",jab)
    print("Gaji Pokok :Rp.", gapok)
    print("Gaji Lembur :Rp.", lembur)
    menu=input("apakah anda imgin menulang kembali Y/N =")
