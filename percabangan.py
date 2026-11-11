 # program kelulusan ujian mahasiswa

nama = input ("masukkan nama mahasiswa: ")

# menentukan target niali
if nama. lower() == "andi":
    target = 70
    
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80 
else:
    print("nama mahasiswa tidak ditemukan!")
    exit()
    
print("nama mahasiwa:", nama)
print("target nilai:", target)

percobaan = 1
lulus = False

#perulangan maksimal 3 kali
while percobaan <= 3:
    nilai = int(input(f"masukkan nilai ujian ke-{percobaan}: "))
    if  nilai >= target:
        lulus = True
        break
    else:
        print("nilai belum mencapai target!")
    percobaan += 1
    
# menampilkan hasil akhir
if lulus:
    print (f"{nama} berhasil setelah {percobaan} kali percobaan!") 
else:
    print(f"{nama} tidak lulus setelah 3 kali percobaan.")       
    