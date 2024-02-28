from tabulate import tabulate

# Header tampilan utama
print('''      
        |          SELAMAT DATANG DI           |
        | PROGRAM ADMIN PERPUSTAKAAN INDONESIA |
    ''')

# Data buku perpuskaan berbentuk nested dictionary, tujuannya agar memudahkan saat memanggil key maupun value pada syntax
daftarBuku = {
        'PI_1': {'Judul':'Laskar Pelangi', 'Penulis':'Andrea Hirata', 'Penerbit':'Bentang', 'Tahun Terbit': 2008, 'Kategori':'Novel'},
        'PI_2': {'Judul':'Sang Pemimpi', 'Penulis':'Andrea Hirata', 'Penerbit':'Bentang', 'Tahun Terbit': 2021, 'Kategori':'Novel'},
        'PI_3': {'Judul':'Sepeda Listrik', 'Penulis':'Buntarto', 'Penerbit':'Pustaka Baru', 'Tahun Terbit': 2020, 'Kategori':'Ensiklopedia'},
        'PI_4': {'Judul':'Negeri 5 Menara', 'Penulis':'Ahmad Fuadi', 'Penerbit':'Gramedia', 'Tahun Terbit': 2018, 'Kategori':'Novel'},
        'PI_5': {'Judul':'Mobil Terbang', 'Penulis':'Dzakiah', 'Penerbit':'Acil Media', 'Tahun Terbit': 2024, 'Kategori':'Fiksi'}
}

# Fungsi untuk memfilter atau menampilkan berdasarkan value pada key Kategori daftarBuku --> READ
def filterBuku():
    print('\n|  Filter  |')
    kategoriInput = input("Urutkan berdasarkan kategori: ")
    rows = []
    found = False
    for id_buku, kategori in daftarBuku.items():
        if kategori['Kategori'].lower() == kategoriInput.lower():
            rows.append([id_buku, kategori['Judul'], kategori['Penulis'], kategori['Penerbit'], kategori['Tahun Terbit'], kategori['Kategori']])
            found = True
    if found == True:
        print("\nBuku:")
        print(tabulate(rows, headers=['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Kategori'], tablefmt='fancy_grid'))
    else:
        print("\nBuku tidak ditemukan!\n")

# Fungsi sorting untuk mengurutkan data berdasarkan atribut yang diinginkan (Judul/Penulis/Tahun Terbit) --> READ
def sortBuku(atribut):
    print('\n|  Urutkan  |')
    if atribut not in ['Judul', 'Penulis', 'Tahun Terbit']:
        print("Atribut sorting tidak valid.")
        return

    sortedBuku = sorted(daftarBuku.values(), key=lambda x: x[atribut])
    rows = []
    for buku in sortedBuku:
        ID = [k for k, v in daftarBuku.items() if v == buku][0]
        JUDUL = buku['Judul']
        PENULIS = buku['Penulis']
        PENERBIT = buku['Penerbit']
        TAHUN = buku['Tahun Terbit']
        KATEGORI = buku['Kategori']
        rows.append([ID, JUDUL, PENULIS, PENERBIT, TAHUN, KATEGORI])

    print(f"\nDaftar Buku Berdasarkan {atribut}:")
    print(tabulate(rows, headers=['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Kategori'], tablefmt='fancy_grid'))

# Fungsi untuk mencari data buku satuan --> READ
def cariBuku():
    print('\n|  Cari Buku  |')
    judul = input("Masukkan judul buku yang ingin dicari: ")
    rows = []
    found = False
    for id_buku, buku in daftarBuku.items():
        if buku['Judul'].lower() == judul.lower():
            rows.append([id_buku, buku['Judul'], buku['Penulis'], buku['Penerbit'], buku['Tahun Terbit'], buku['Kategori']])
            found = True
    if found:
        print("\nBuku:")
        print(tabulate(rows, headers=['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Kategori'], tablefmt='fancy_grid'))
    else:
        print("\nBuku tidak ditemukan!\n")

# Fungsi untuk melihat dan mengurutkan dafrar buku --> READ
def lihatDaftarBuku():
    while True:
        print('\n|  Daftar Buku  |')
        print("\n1. Lihat Daftar Buku")
        print("2. Cari buku")
        print("\n[x] Kembali")
        inputMenu = input("\nPilih Menu: ")
        if inputMenu == '1':
            if not daftarBuku:
                print("\nTidak ada buku yang tersedia saat ini.")
                return
            tampilkanBuku()
            print('\n|  Lihat Daftar Buku  |')
            print("1. Urutkan")
            print("2. Filter")
            print("\n[x] Kembali")
            pilihMenu = input('Pilih Menu:')
            if pilihMenu == '1':
                urutkanBuku = input('Urutkan berdasarkan (1) Judul / (2) Penulis / (3) Tahun Terbit: ').lower()
                if urutkanBuku == '1':
                    sortBuku('Judul')
                elif urutkanBuku == '2':
                    sortBuku('Penulis')
                elif urutkanBuku == '3':
                    sortBuku('Tahun Terbit')  
            elif pilihMenu == '2':
                    filterBuku()
            elif pilihMenu.lower() == 'x':
                break
        elif inputMenu == '2':
            if not daftarBuku:
                print("\nTidak ada buku yang tersedia saat ini.")
                return
            cariBuku()
        elif inputMenu.lower() == 'x':
            mainMenuProgram()
        else:
            print("\nInput tidak valid, Silakan pilih menu yang sesuai!\n")

# Fungsi untuk mereset daftarBuku --> DELETE
def resetDataBuku():
    while True:
        global daftarBuku
        konfirmasi = input("Apakah Anda yakin ingin Mereset Data Buku? (y/n): ")
        if konfirmasi.lower() == 'y':
            daftarBuku = {}
            tampilkanBuku()
            print('Reset daftar buku Berhasil!')
        elif konfirmasi.lower() == 'n':
            print('Reset daftar buku dibatalkan!')
            break
        else:
            print("Masukkan input yang valid! (y/n).")

# Fungsi untuk menghapus data buku --> DELETE
def hapusDataBuku():
    while True:
        global daftarBuku
        if not daftarBuku:
            print("\nTidak ada buku yang tersedia saat ini.")
            return
        print('\n|  Hapus Buku  |')
        print("\n1. Hapus salah satu Buku")
        print("2. Reset Data Buku")
        print("\n[x] Kembali")
        pilih = input("Pilih Menu: ")
        if pilih == '1':
            kode_buku = input("Masukkan kode buku yang ingin dihapus: ").upper()
            if kode_buku in daftarBuku:
                konfirmasi = input("Apakah Anda yakin ingin Mereset Data Buku? (y/n): ")
                if konfirmasi.lower() == 'y':
                    del daftarBuku[kode_buku]
                    tampilkanBuku()
                    print("Buku berhasil dihapus.")
                elif konfirmasi.lower() == 'n':
                    print('\nHapus buku dibatalkan!')
                    break
                else:
                    print("Masukkan input yang benar! (y/n).")
        elif pilih == '2':
            if not daftarBuku:
                print("\nTidak ada buku yang tersedia saat ini.")
                return
            konfirmasi = input("Apakah Anda yakin ingin Mereset Data Buku? (y/n): ")
            if konfirmasi.lower() == 'y':
                daftarBuku = {}
                tampilkanBuku()
                print('Reset daftar buku Berhasil!')
            elif konfirmasi.lower() == 'n':
                print('\nReset daftar buku dibatalkan!')
                break
            else:
                print("Masukkan input yang benar! (y/n).")
        elif pilih.lower() == 'x':
            break
        else:
            print("\nInput tidak valid, Silakan pilih menu yang sesuai!\n")

# Fungsi untuk memperbarui atau mengedit data buku --> UPDATE
def updateDataBuku():
    while True:
        if not daftarBuku:
            print("\nTidak ada buku yang tersedia saat ini.")
            return
        tampilkanBuku()
        idBuku = input("Masukkan ID buku yang ingin diedit: ").upper()
        if idBuku not in daftarBuku:
            print("ID buku tidak ditemukan.")
            return
        print('\n|  Update Buku  |')
        print('\n1. Sebagian Data')
        print('2. Seluruh Data')
        print("\n[x] Kembali")
        pilih = input("Pilih Menu: ")
        if pilih == '1':
            print('1. Judul\t4. Tahun Terbit')
            print('2. Penulis\t5. Kategori')
            print('3. Penerbit\n')
            sub = input("Masukkan atribut yang ingin diubah (1-5): ")
            if sub == '1':
                nilaiBaru = input("Masukkan judul baru: ").title()
                konfirmasi = input("Apakah Anda yakin ingin Update judul Buku? (y/n): ")
                if konfirmasi.lower() == 'y':
                    daftarBuku[idBuku]['Judul'] = nilaiBaru
                    tampilkanBuku()
                    print('Update judul buku Berhasil!')
                elif konfirmasi.lower() == 'n':
                    print('\nUpdate judul buku dibatalkan!')
                    break
            elif sub == '2':
                nilaiBaru = input("Masukkan nama penulis baru: ").title()
                while not nilaiBaru.replace("'", "").replace(".", "").replace(",", "").replace(" ","").isalpha():
                    print("Input tidak valid, input harus berupa nama penulis!")
                    nilaiBaru = input('Masukkan nama penulis: ').title()
                konfirmasi = input("Apakah Anda yakin ingin Update penulis Buku? (y/n): ")
                if konfirmasi.lower() == 'y':
                    daftarBuku[idBuku]['Penulis'] = nilaiBaru
                    tampilkanBuku()
                    print('Update penulis buku Berhasil!')
                elif konfirmasi.lower() == 'n':
                    print('\nUpdate penulis buku dibatalkan!')
                    break
            elif sub == '3':
                nilaiBaru = input("Masukkan nama penerbit baru: ").title()
                konfirmasi = input("Apakah Anda yakin ingin Update penerbit Buku? (y/n): ")
                if konfirmasi.lower() == 'y':
                    daftarBuku[idBuku]['Penerbit'] = nilaiBaru
                    tampilkanBuku()
                    print('Update penerbit buku Berhasil!')
                elif konfirmasi.lower() == 'n':
                    print('\nUpdate penerbit buku dibatalkan!')
                    break
            elif sub == '4':
                nilaiBaru = input("Masukkan tahun terbit baru(YYYY): ")
                while not nilaiBaru.isdigit() or len(nilaiBaru) != 4 or int(nilaiBaru) > 2024:
                    print("Input tidak valid, input harus berupa tahun!")
                    nilaiBaru = input('Masukkan tahun terbit(YYYY): ')
                konfirmasi = input("Apakah Anda yakin ingin Update tahun terbit Buku? (y/n): ")
                if konfirmasi.lower() == 'y':
                    daftarBuku[idBuku]['Tahun Terbit'] = nilaiBaru
                    tampilkanBuku()
                    print('Update tahun terbit buku Berhasil!')
                elif konfirmasi.lower() == 'n':
                    print('\nUpdate tahun terbit buku dibatalkan!')
                    break
            elif sub == '5':
                nilaiBaru = input("Masukkan kategori baru: ").title()
                while not nilaiBaru.replace(" ", "").isalpha():
                    print("Input tidak valid, input harus berupa kategori buku!")
                    nilaiBaru = input('Masukan kategori baru: ').title()
                konfirmasi = input("Apakah Anda yakin ingin Update kategori Buku? (y/n): ")
                if konfirmasi.lower() == 'y':
                    daftarBuku[idBuku]['Kategori'] = nilaiBaru
                    tampilkanBuku()
                    print('Update kategori buku Berhasil!')
                elif konfirmasi.lower() == 'n':
                    print('\nUpdate kategori buku dibatalkan!')
                    break
            else:
                print("Input tidak valid!")
        elif pilih == '2':
            judulBaru = input("Masukkan judul baru: ")
            penulisBaru = input("Masukkan penulis baru: ")
            while not penulis.replace("'", "").replace(".", "").replace(",", "").replace(" ","").isalpha():
                print("Input tidak valid, input harus berupa nama penulis!")
                penulis = input('Masukkan nama penulis: ').title()
            penerbitBaru = input("Masukkan penerbit baru: ")
            tahunTerbitBaru = input("Masukkan tahun terbit baru(YYYY): ")
            while not tahunTerbitBaru.isdigit() or len(tahunTerbitBaru) != 4 or int(nilaiBaru) > 2024:
                print("Input tidak valid, input harus berupa tahun!")
                tahunTerbitBaru = input('Masukkan tahun terbit(YYYY): ')
            kategoriBaru = input("Masukkan kategori baru: ").title()
            while not kategoriBaru.replace(" ", "").isalpha():
                print("Input tidak valid, input harus berupa kategori buku!")
                kategoriBaru = input('Masukan kategori buku: ').title()

            daftarBuku[idBuku] = {'Judul': judulBaru, 'Penulis': penulisBaru, 'Penerbit': penerbitBaru, 'Tahun Terbit': tahunTerbitBaru, 'Kategori': kategoriBaru}
        elif pilih.lower() == 'x':
            break
        else:
            print("Pilihan tidak valid.")

        tampilkanBuku()
        
# Fungsi untuk menampilkan seluruh buku pada daftarBuku dalam bentuk tabel tabulate --> Fungsi READ
def tampilkanBuku():
    row = []
    for id, infoBuku in daftarBuku.items():
        row.append([id,infoBuku['Judul'],infoBuku['Penulis'],infoBuku['Penerbit'],infoBuku['Tahun Terbit'],infoBuku['Kategori']])
        
    print('='*38,'DAFTAR BUKU','='*38,'\n')
    print(tabulate(row,headers=['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Kategori'],tablefmt='fancy_grid'))

# Fungsi untuk menambahkan buku ke dalam daftarBuku --> fungsi CREATE
def tambahBuku():
    print('\n\t|  Tambah Buku  |\n')
    print('1. Input Data Buku')
    print('[x] Kembali')
    pilih = input("Pilih menu (1) untuk input data buku: ")
    if pilih == '1':
        judul = input("Masukkan judul buku: ").title()
        penulis = input("Masukkan nama penulis: ").title()
        while not penulis.replace("'", "").replace(".", "").replace(",", "").replace(" ","").isalpha():
            print("Input tidak valid, input harus berupa nama penulis!")
            penulis = input('Masukkan nama penulis: ').title()
        penerbit = input('Masukkan nama penerbit: ').title()
        tahunTerbit = input('Masukkan tahun terbit(YYYY): ')
        while not tahunTerbit.isdigit() or len(tahunTerbit) != 4 or int(tahunTerbit) > 2024:
            print("Input tidak valid, input harus berupa angka bulat (tahun)!")
            tahunTerbit = input('Masukkan tahun terbit(YYYY): ')
        kategori = input('Masukan kategori buku: ').title()
        while not kategori.replace(" ", "").isalpha():
            print("Input tidak valid, input harus berupa kategori buku!")
            kategori = input('Masukan kategori buku: ').title()
        konfirmasi = input('Apakah data buku sudah benar(y/n)? ')
        if konfirmasi.lower() == 'y':
            if not daftarBuku:
                indexBaru = 0+1
                keyBaru = f'PI_{indexBaru}'
            else:
                lastIndex = int(list(daftarBuku.keys())[-1].split('_')[-1])
                indexBaru = lastIndex+1
                keyBaru = f"PI_{indexBaru}"
            daftarBuku[keyBaru] = {
                    'Judul': judul,
                    'Penulis': penulis,
                    'Penerbit': penerbit,
                    'Tahun Terbit': tahunTerbit,
                    'Kategori': kategori,
                }
            tampilkanBuku()
            print("\nBuku berhasil ditambahkan!\n")
            tambahBuku()
        else:
            print('\nTambah buku dibatalkan!')
            tambahBuku()
    elif pilih.lower() == 'x':
        mainMenuProgram()
    else:
        print("\nInput tidak valid, Silakan pilih menu yang sesuai!\n")
        tambahBuku()


# Fungsi menu utama pada program perpustakaan
def mainMenuProgram():
    while True:
        print('''      
                    | Menu Utama |
            
                    1. Tambah Buku 
                    2. Update Data Buku 
                    3. Hapus Buku
                    4. Lihat Daftar Buku
                    
                    [x] Keluar
        ''')   
        opsi = input('Pilih Menu: ')
        if opsi == '1':
            tambahBuku()
        elif opsi == '2':
            updateDataBuku()
        elif opsi == '3':
            hapusDataBuku()
        elif opsi == '4':
            lihatDaftarBuku()
        elif opsi.lower() == 'x':
            konfirmasi = input("Apakah Anda yakin ingin keluar? (y/n): ")
            if konfirmasi.lower() == 'y':
                print('Program Berakhir, Terimakasih!')
                exit()
        else:
            print('Input tidak valid, Silahkan masukan input yang benar!')

# Fungsi login ditujukan pada target user program ini yaitu admin Perpustakaan Indonesia
def login():
    while True:    
        print(' '*20+'| User Login |')
        username = input("\nUsername: ")
        password = input("Password: ")
        if username.lower() == 'admin' and password.lower() == 'admin123':
            mainMenuProgram()
        else:
                print('Username atau Password anda salah!\n')

# Memanggil fungsi login() untuk memulai program
login()