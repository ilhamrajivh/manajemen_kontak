#program manajemen kontak

kontak1 = {'nama': 'Andi', 'HP': '100077881', 'email': 'andilaw@mail.com'}
kontak2 = {'nama' : 'Ani', 'HP': '100099881', 'email': 'ani22@mail.com'}
kontak = [kontak1, kontak2]


while True:


    print("\nMenu Kontak")
    print("1. Melihat semua kontak")
    print("2. Menambahkan kontak baru")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == '1':
        #melihat semua kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong.")

    elif pilihan == '2':
        #menambahkan kontak
        nama = input("masukkan nama kontak yang baru: ")
        HP = input ("masukkan nomor HP kontak yang baru: ")
        email = input("masukkan email kontak yang baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")
    elif pilihan == '3':
        #menghapus kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong.")
            continue
        i_hapus = int(input("Masukkan nomor kontak yang dihapus: "))
        del kontak[i_hapus -1]
        print("Kontak yang dimaksud sudah dihapus")
    elif pilihan == '4':
        #keluar dari kontak
       break
    else :
        print("anda memasukkan pilihan yang salah")
