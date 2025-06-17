from tabulate import tabulate
from datetime import datetime, timedelta

# ===== Sistem Peminjaman Buku di Perpustakaan =====

daftar_buku = [
    {"id_buku": "B1",
     "judul": "Bulan",
     "penulis": "Tere Liye",
     "kategori": "Novel",
     "stok": 3
     },
     { "id_buku": "B2",
     "judul": "Bumi",
     "penulis": "Tere Liye",
     "kategori": "Novel",
     "stok": 3
     },
     {"id_buku": "B3",
     "judul": "The Power of Habits",
     "penulis": "Charles Duhigg",
     "kategori": "Motivasi",
     "stok": 4
     },
     {"id_buku": "B4",
     "judul": "Becoming",
     "penulis": "Michelle Obama",
     "kategori": "Biografi",
     "stok": 5
     },
     {"id_buku": "B5",
     "judul": "The Alpha Girl",
     "penulis": "Henry Manampiring",
     "kategori": "Motivasi",
     "stok": 2
     }
]
data_peminjam = []
id_peminjam = 0

# Menu awal
def menu_perpus():
        print("\n=== Selamat Datang di Perpustakaan Kota ===")
        print("-----------------------------------------------")
        print("1. Tampilkan Buku")
        print("2. Pinjam Buku")
        print("3. Pengembalian Buku")
        print("4. Update Data Buku")
        print("5. Hapus Buku")
        print("6. Keluar")

# menampilkan sub menu tampil buku
def sub_menu_tampil():
        print("\n=== Pilih Menu ===")
        print("-----------------------------------------------")
        print("1. Tampilkan Daftar Buku")
        print("2. Cari Buku")
        print("3. Menu Utama")

def tampil_daftar_buku():
        print("\n=== Daftar Buku Bacaan ===")
        print("----------------------------")   
        print(tabulate(daftar_buku, headers="keys", tablefmt="grid"))

def cari_buku():
        print("\n==== Cari Buku ====")
        print("----------------------")
        keyword = input("Masukkan kata kunci (Judul/Penulis): ").lower()
        cari = []
        for buku in daftar_buku:
                if keyword in buku["judul"].lower() or keyword in buku["penulis"].lower():
                        cari.append(list(buku.values()))
        hasil_pencarian = ("Hasil Pencarian: ")
        if hasil_pencarian:
                print("\nHasil Pencarian: ")
                header = list(daftar_buku[0].keys()) 
                print(tabulate(cari, headers=header, tablefmt="grid"))

        else:
              print("\nTidak ada buku yang ditemukan!")

def cari_buku_by_judul(judul):
        # Fungsi untuk mencari buku berdasarkan judul dan mengembalikan objek buku
        for buku in daftar_buku:
            if judul.lower() in buku["judul"].lower():
                return buku
        return None
      
# peminjaman buku
def sub_menu_pinjam():
        print("\n=== Pilih Menu ===")
        print("-----------------------------------------------")
        print("1. Menu Pinjam Buku")
        print("2. Data Peminjam")
        print("3. Menu Utama")

def pinjam_buku():
        global id_peminjam
        id_peminjam += 1
        nama_peminjam = input("Masukkan nama peminjam: ")

        tampil_daftar_buku()
        judul_buku = input("Masukkan judul buku yang ingin dipinjam: ")
        buku_dipinjam = cari_buku_by_judul(judul_buku)

        if not buku_dipinjam:
                print("Buku tidak ditemukan!\n")
                return
        if buku_dipinjam["stok"] <= 0:
                print("Stok Buku Habis!\n")
                return

        # Validasi apakah peminjam sudah meminjam buku (berdasarkan judul buku)
        for peminjam in data_peminjam:
                if peminjam["Nama Peminjam"].lower() == nama_peminjam.lower() and peminjam["Judul Buku"].lower() == buku_dipinjam["judul"].lower():
                        print(f"Error: {nama_peminjam} sudah meminjam buku '{buku_dipinjam['judul']}'. Kembalikan dulu sebelum meminjam lagi.")
                        return

        # validasi tanggal
        try:
                tanggal_pinjam_input = input("Tanggal Pinjam (DD-MM-YYYY): ")
                tanggal_pinjam = datetime.strptime(tanggal_pinjam_input, "%d-%m-%Y")
                tanggal_kembali = tanggal_pinjam + timedelta(days=10)
        except ValueError:
                print("Format tanggal salah! Gunakan Format DD-MM-YYYY")
                return
       
        # simpan data
        data = {
                "ID" : id_peminjam,
                "Nama Peminjam" : nama_peminjam,
                "Judul Buku" : buku_dipinjam["judul"],
                "Tanggal Pinjam" : tanggal_pinjam.strftime("%d-%m-%Y"),
                "Tanggal Kembali" : tanggal_kembali.strftime("%d-%m-%Y")
        }

        data_peminjam.append(data)
        buku_dipinjam["stok"] -= 1
        print(f"Buku '{buku_dipinjam['judul']}' berhasil dipinjam!")
        print(f"Tanggal Kembali Otomatis: {tanggal_kembali.strftime('%d-%m-%Y')}")


def tampil_data_peminjam():
        if not data_peminjam:
                print("Belum ada data peminjam.")
                return
        
        print("\n=== Data Peminjam ===")
        print("----------------------")
        header = list(data_peminjam[0].keys())
        tabel = []
        for item in data_peminjam:
                tabel.append(list(item.values()))
        print(tabulate(tabel, headers=header, tablefmt="grid"))

# pengembalian buku

def pengembalian_buku():
        if not data_peminjam:
                print("Tidak ada data peminjam")
                return
        
        tampil_data_peminjam()
        try:
                id_kembali = int(input("Masukkan ID peminjam untuk pengembalian: "))
                for i, peminjam in enumerate(data_peminjam):
                        if peminjam["ID"] == id_kembali:
                                
                                #Kembalikan stok buku
                                judul_dikembalikan = peminjam["Judul Buku"]
                                tgl_kembali_str = peminjam["Tanggal Kembali"]
                                tgl_kembali = datetime.strptime(tgl_kembali_str, "%d-%m-%Y")
                                try:
                                        tgl_pengembalian_input = input("Masukkan tanggal pengembalian (DD-MM-YYYY): ")
                                        tgl_pengembalian = datetime.strptime(tgl_pengembalian_input, "%d-%m-%Y")
                                except ValueError:
                                        print("Format tanggal salah! Gunakan format DD-MM-YYYY.")
                                        return
                                # Apakah terlambat dikembalikan atau tepat waktu
                                if tgl_pengembalian > tgl_kembali:
                                        selisih = (tgl_pengembalian - tgl_kembali).days
                                        print(f"⚠️ Pengembalian terlambat {selisih} hari!")
                                else:
                                        print("Buku dikembalikan tepat waktu.")


                                buku_dikembalikan = cari_buku_by_judul(judul_dikembalikan)
                                if buku_dikembalikan:
                                        buku_dikembalikan["stok"] += 1

                                #Hapus data peminjam
                                data_peminjam.pop(i)
                                print(f"Buku '{judul_dikembalikan}' berhasil dikembalikan")
                                return
                print("ID peminjam tidak ditemukan!")
        except ValueError:
                print("ID harus berupa angka!")


# Update data buku

def update_buku():
        tampil_daftar_buku()
        id_buku = input("Masukkan ID buku yang ingin diupdate: ").upper()

        for buku in daftar_buku:
                if buku["id_buku"] == id_buku:
                        print(f"Data buku saat ini: {buku}")
                        print("Kosongkan field jika tidak ingin mengubah")

                        judul_baru = input(f"Judul baru (sekarang: {buku['judul']}): ")
                        if judul_baru:
                                buku["judul"] = judul_baru

                        penulis_baru = input(f"Penulis baru (sekarang: {buku['penulis']}): ")
                        if penulis_baru:
                                buku["penulis"] = penulis_baru

                        kategori_baru = input(f"Kategori baru (sekarang: {buku['kategori']}): ")
                        if kategori_baru:
                                buku["kategori"] = kategori_baru

                        stok_baru = input(f"Stok baru (sekarang: {buku['stok']}): ")
                        if stok_baru:
                                try:
                                        buku["stok"] = int(stok_baru)
                                except ValueError:
                                        print("Stok harus berupa angka!")
                                        return
                                
                        print("Data buku berhasil diupdate!")
                        return
        print("ID buku tidak ditemukan!")

def hapus_buku():
        tampil_daftar_buku()
        id_buku = input("Masukkan ID buku yang ingin dihapus: ").upper()

        for i, buku in enumerate(daftar_buku):
                if buku["id_buku"] == id_buku:
                        while True:
                                konfirmasi = input(f"Yakin ingin menghapus buku '{buku['judul']}'? (y/n): ").lower()
                                if konfirmasi.lower() == 'y':
                                        daftar_buku.pop(i)
                                        print("\nBuku Berhasil Dihapus!")
                                        return
                                elif konfirmasi.lower()== "n":
                                        print("\nPenghapusan Dibatalkan.")
                                        return
                                else:
                                        print("\nInput Tidak Valid !!!")
                                                
        print("ID buku tidak ditemukan!")

# loop menu utama
while True:
    menu_perpus()
    pilihan = input("\nPilih Menu: ")

    if pilihan == "1":
            while True:
                sub_menu_tampil()
                pilih = input("\n Pilih Menu: ")
                if pilih == "1":
                        tampil_daftar_buku()
                elif pilih == "2":
                        cari_buku()
                elif pilih == "3":
                        break
                else:
                        print("Pilihan tidak valid!")

    elif pilihan == "2":
            while True:
                    sub_menu_pinjam()
                    pilih = input("\nPilih Menu: ")
                    if pilih == "1":
                            pinjam_buku()
                    elif pilih == "2":
                            tampil_data_peminjam()
                    elif pilih == "3":
                            break
                    else:
                            print("Pilihan tidak valid!")

    elif pilihan == "3":
            print("\n==Pengembalian Buku==")
            pengembalian_buku()

    elif pilihan == "4":
            print("\n==Update Buku==")
            update_buku()

    elif pilihan == "5":
            print("==Hapus buku==")
            hapus_buku()

    elif pilihan == "6":
            print("Terimakasih Telah Menggunakan Program!")
            break
    else:
            print("Pilihan tidak valid!")
