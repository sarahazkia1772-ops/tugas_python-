print("=== SISTEM PENGELOLAAN STOK BARANG ===")

# Input data awal
nama_barang = input("Masukkan nama barang: ")
stok = int(input("Masukkan jumlah stok awal: "))

while True:
    print("\n=== MENU TRANSAKSI ===")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Selesai")

    pilihan = input("Pilih transaksi (1/2/3): ")

    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah barang masuk: "))
        stok += jumlah
        print("Barang berhasil ditambahkan.")
        print("Stok sekarang:", stok)

    elif pilihan == "2":
        jumlah = int(input("Masukkan jumlah barang keluar: "))

        if jumlah <= stok:
            stok -= jumlah
            print("Barang berhasil dikeluarkan.")
            print("Stok sekarang:", stok)
        else:
            print("Stok Tidak Mencukupi!")

    elif pilihan == "3":
        break

    else:
        print("Pilihan tidak valid!")

print("\n=== HASIL AKHIR ===")
print("Nama barang :", nama_barang)
print("Stok akhir  :", stok)
print("Transaksi selesai.")