# program manajemen kontak

def melihat_kontak():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong.")
        return 1

def menambah_kontak():
    nama = input("Masukkan nama kontak yang baru: ")
    HP = input("Masukkan nomor HP kontak yang baru: ")
    email = input("Masukkan email kontak yang baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan.")

def menghapus_kontak():
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus - 1]
        print("Kontak yang dimaksud sudah dihapus.")

kontak1 = {'nama': 'Andi', 'HP': '100077881', 'email': 'andilaw@mail.com'}
kontak2 = {'nama': 'Ani', 'HP': '100099881', 'email': 'ani22@mail.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat semua kontak")
    print("2. Menambahkan kontak baru")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == '1':
        melihat_kontak()
    elif pilihan == '2':
        menambah_kontak()
    elif pilihan == '3':
        menghapus_kontak()
    elif pilihan == '4':
        print("Keluar dari program. Sampai jumpa!")
        break
    else:
        print("Anda memasukkan pilihan yang salah.")
