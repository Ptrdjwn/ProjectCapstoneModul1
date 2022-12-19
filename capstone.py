#PENJUALAN BARANG TOKO BANG GANS

#data awal barang
ListBarang = {
    # 'KS' : {'Kode' : 'KS', 'Nama' : 'Kulkas', 'Tipe' : 'Elektronik', 'Merk' : 'Samsung', 'Stock' : 10, 'Harga' : 1500000},
    # 'TS' : {'Kode' : 'TS', 'Nama' : 'Televisi', 'Tipe' : 'Elektronik', 'Merk' : 'Samsung', 'Stock' : 17, 'Harga' : 3000000},
    # 'MI' : {'Kode' : 'MI', 'Nama' : 'Meja', 'Tipe' : 'Mebel', 'Merk' : 'Ikea', 'Stock' : 20, 'Harga' : 500000},
    # 'KI' : {'Kode' : 'KI', 'Nama' : 'Kursi', 'Tipe' : 'Mebel', 'Merk' : 'Ikea', 'Stock' : 13, 'Harga' : 350000},
    # 'PM' : {'Kode' : 'PM', 'Nama' : 'Panci', 'Tipe' : 'Alat Masak', 'Merk' : 'Miyako', 'Stock' : 8, 'Harga' : 75000},
    # 'WM' : {'Kode' : 'WM', 'Nama' : 'Wajan', 'Tipe' : 'Alat Masak', 'Merk' : 'Miyako', 'Stock' : 5, 'Harga' : 60000} 
}

Keranjang =[]

# menampilkan seluruh data 
def menampilkanSeluruh() :
    if len(ListBarang) == 0 :
        print('Data Barang Kosong')
    else :
        print('List Barang\n')
        for key in ListBarang.keys() :
            print('Kode : {}, Nama : {}, Tipe : {}, Merk : {}, Stock : {}, Harga : {}'.format(ListBarang[key]['Kode'],ListBarang[key]['Nama'],ListBarang[key]['Tipe'],ListBarang[key]['Merk'],ListBarang[key]['Stock'],ListBarang[key]['Harga']))

# menampilkan berdasarkan kode
def menampilkanSebagian() :
    if len(ListBarang) == 0 :
        print('Data Barang Kosong')
    else :
        KodeBarang = input('Masukkan Kode Barang : ')
        if KodeBarang.upper() in ListBarang.keys() :
            print(f'Barang Dengan Kode Barang : {KodeBarang}')
            print('Kode : {}, Nama : {}, Tipe : {}, Merk : {}, Stock : {}, Harga : {}'.format(ListBarang[KodeBarang]['Kode'],ListBarang[KodeBarang]['Nama'],ListBarang[KodeBarang]['Tipe'],ListBarang[KodeBarang]['Merk'],ListBarang[KodeBarang]['Stock'],ListBarang[KodeBarang]['Harga']))
        else :
            print(f'Barang Dengan Kode Barang : {KodeBarang}')
            print('***Tidak Ada Data Barang***')

# menampilkan berdasarkan merk
def menampilkanMerk() :
    count=0
    if len(ListBarang) == 0 :
            print('Data Barang Kosong')
    else :
        merkBarang = input('Masukkan Merk Barang : ')
        for key in ListBarang :
            if merkBarang.capitalize() == ListBarang[key]['Merk']  : 
                print('Kode : {}, Nama : {}, Tipe : {}, Merk : {}, Stock : {}, Harga : {}'.format(ListBarang[key]['Kode'],ListBarang[key]['Nama'],ListBarang[key]['Tipe'],ListBarang[key]['Merk'],ListBarang[key]['Stock'],ListBarang[key]['Harga'])) 
                count+=1
        if count == 0 :
            print('Maaf Stock Barang Merk Tersebut Kosong')

#FUNGSI READ
# menampilkan list data barang
def menampilkanListDataBarang() :
    while True :
        pilihanMenu = input('''
            +++++++List Data Barang+++++++

                List Menu :
                1. Tampilkan Seluruh Data
                2. Tampilkan Data Tertentu
                3. Tampilkan Data Menurut Merk
                4. Kembali Ke Menu Utama

                Silahkan Pilih Sub Menu: ''')
        if(pilihanMenu == '1') :
            menampilkanSeluruh()
        elif(pilihanMenu == '2') :
            menampilkanSebagian() 
        elif(pilihanMenu == '3') :
            menampilkanMerk()
        elif(pilihanMenu == '4') :
            break
        else :
            print('Mohon Maaf Pilihan Tidak Tersedia, Silahkan Pilih Menu Yang Tersedia')

#FUNGSI CREATE
# Menu tambah data barang
def menambahkanDataBarang() :
    while True :
        pilihanMenu = input('''
            +++++++Menu Tambah Data Barang+++++++

                List Menu :
                1. Menambah Data Barang
                2. Kembali Ke Menu Utama

                Silahkan Pilih Sub Menu: ''')
        if(pilihanMenu == '1') :
            while True : 
                kodeBarang = input('''
                    Kode Barang Terdiri Dari :
                    Huruf Pertama Nama Barang &
                    Huruf Pertama Merk Barang.
                    Contoh : Kulkas Samsung --> Kode Barang : KS
                    Masukkan Kode Barang : ''')
                kodeBarang = kodeBarang.upper()
                if kodeBarang.isalpha() == False :
                    print('Kode Barang Tidak Dapat Berisi Angka')
                elif len(kodeBarang) > 2 :
                    print('Kode Barang Hanya Boleh Berisi 2 Huruf')
                else : 
                    break
            if kodeBarang.upper() not in ListBarang.keys() :
                while True : 
                    namaBarang = input('Masukkan Nama Barang : ')
                    namaBarang = namaBarang.capitalize()
                    if namaBarang[0] != kodeBarang[0] :
                        print('Huruf Pertama Nama Barang Harus Sesuai Dengan Huruf Pertama Kode Barang')
                    else : 
                        break
                tipeBarang = input('Masukkan Tipe Barang : ')
                while True :
                    merkBarang = input('Masukkan Merk Barang : ')
                    merkBarang = merkBarang.capitalize()
                    if merkBarang[0] != kodeBarang[1] :
                        print('Huruf Pertama Merk Barang Harus Sesuai Dengan Huruf Kedua Kode Barang')
                    else : 
                        break
                while True :
                    stockBarang = input('Masukkan Stock Barang : ')
                    if stockBarang.isnumeric() == False :
                        print('Stock Barang Harus Diisi Dengan Angka')
                    else :
                        break
                while True :
                    hargaBarang = input('Masukkan Harga Barang : ')
                    if hargaBarang.isnumeric() == False :
                        print('Harga Barang Harus Diisi Dengan Angka')
                    elif int(hargaBarang) < 1000 :
                        print('Barang Harus Bernilai Lebih Dari 1000 Rupiah')
                    else :
                        break
                while True : 
                    checker = input(f'\nApakah Anda Ingin Menambahkan Barang {namaBarang.capitalize()} Merk {merkBarang.capitalize()} Berjumlah {stockBarang} Unit Dengan Harga {hargaBarang} Per Unit? (Y/N): \n')
                    if checker.upper() == 'Y' :
                        ListBarang[kodeBarang.upper()]={'Kode':kodeBarang.upper(),'Nama':namaBarang.capitalize(),'Tipe':tipeBarang.capitalize(),'Merk':merkBarang.capitalize(),'Stock':int(stockBarang),'Harga':int(hargaBarang)}
                        print('Data Tersimpan\n')
                        menampilkanSeluruh()
                        break
                    elif checker.upper() == 'N' :
                        break
                    else : 
                        ('Maaf Pilihan Tersebut Tidak Ada')
            else :
                print('Barang Sudah Terdata, Jika Ingin Menambah Stock Bisa Pilih Menu Ubah Data Barang')
        elif(pilihanMenu == '2') :
            break
        else :
            print('Mohon Maaf Pilihan Tidak Tersedia, Silahkan Pilih Menu Yang Tersedia')

#FUNGSI UPDATE
# Menu ubah data barang
def mengubahDataBarang() :
    while True :
        pilihanMenu = input('''
            +++++++Menu Ubah Data Barang+++++++

                List Menu :
                1. Mengubah Data Barang
                2. Kembali Ke Menu Utama

                Silahkan Pilih Sub Menu: ''')
        if(pilihanMenu == '1') :
            if len(ListBarang) == 0 :
                print('Data Barang Kosong')
                break
            while True : 
                menampilkanSeluruh()
                KodeBarang = input('Masukkan Kode Barang : ')
                KodeBarang = KodeBarang.upper()
                if KodeBarang in ListBarang.keys() :
                    print(f'Barang Dengan Kode Barang : {KodeBarang}')
                    print('Kode : {}, Nama : {}, Tipe : {}, Merk : {}, Stock : {}, Harga : {}'.format(ListBarang[KodeBarang]['Kode'],ListBarang[KodeBarang]['Nama'],ListBarang[KodeBarang]['Tipe'],ListBarang[KodeBarang]['Merk'],ListBarang[KodeBarang]['Stock'],ListBarang[KodeBarang]['Harga']))
                    break
                else :
                    print(f'Barang Dengan Kode Barang : {KodeBarang}')
                    print('***Tidak Ada Data Barang***')
            while True :
                checker = input('Apakah Ingin Mengubah Data Barang Ini? (Y/N): ')
                if checker.upper() == 'Y' :
                    while True :
                        kolomBarang = input('Masukkan Kolom Barang Yang Ingin Diubah : ')
                        kolomBarang = kolomBarang.capitalize()
                        if kolomBarang == 'Kode' : 
                            print('Kode Barang Tidak Bisa Diubah Karena Terikat Dengan Nama Barang & Merk Barang')
                            break
                        if kolomBarang == 'Nama' :
                            namaBaru = input('Masukkan Nama Baru : ')
                            namaBaru = namaBaru.capitalize()
                            if namaBaru in ListBarang[KodeBarang]['Nama'] :
                                print('Tidak Bisa Memasukkan Nama Yang Sama, Masukkan Nama Lain')
                            elif namaBaru.isalpha() == False :
                                print('Nama Barang Tidak Boleh Mengandung Angka')
                            elif namaBaru[0] != KodeBarang[0] :
                                print('Huruf Pertama Nama Barang Harus Sesuai Dengan Huruf Pertama Kode Barang')
                            else :
                                checker = input (f'Apakah Anda Ingin Mengganti Nama Barang {ListBarang[KodeBarang]["Nama"]} Menjadi {namaBaru}? (Y/N): ')
                                if checker.upper() == 'Y':
                                    ListBarang[KodeBarang]['Nama'] = namaBaru
                                    print('Nama Barang Berhasil Diubah')
                                    menampilkanSeluruh()
                                    break
                                elif checker.upper() == 'N' :
                                    break
                                else :              
                                    print('Maaf Pilihan Tersebut Tidak Ada')
                        elif kolomBarang == 'Tipe' :
                            tipeBaru = input('Masukkan Tipe Baru : ')
                            tipeBaru = tipeBaru.capitalize()
                            if tipeBaru in ListBarang[KodeBarang]['Tipe'] :
                                print('Tidak Bisa Memasukkan Tipe Yang Sama, Masukkan Tipe Lain')
                            elif tipeBaru.isalpha() == False :
                                print('Tipe Barang Tidak Boleh Mengandung Angka')
                            else :
                                checker = input (f'Apakah Anda Ingin Mengganti Tipe Barang {ListBarang[KodeBarang]["Tipe"]} Menjadi {tipeBaru}? (Y/N): ')
                                if checker.upper() == 'Y':
                                    ListBarang[KodeBarang]['Tipe'] = tipeBaru
                                    print('Tipe Barang Berhasil Diubah')
                                    menampilkanSeluruh()
                                    break
                                elif checker.upper() == 'N' :
                                    break
                                else :              
                                    print('Maaf Pilihan Tersebut Tidak Ada')
                        elif kolomBarang == 'Merk' :
                            merkBaru = input('Masukkan Merk Baru : ')
                            merkBaru = merkBaru.capitalize()
                            if merkBaru in ListBarang[KodeBarang]['Merk'] :
                                print('Tidak Bisa Memasukkan Merk Yang Sama, Masukkan Merk Lain')
                            elif merkBaru.isalpha() == False :
                                print('Merk Barang Tidak Boleh Mengandung Angka')
                            elif merkBaru[0] != KodeBarang[1] :
                                print('Huruf Pertama Merk Barang Harus Sesuai Dengan Huruf Kedua Kode Barang')
                            else :
                                checker = input (f'Apakah Anda Ingin Mengganti Merk Barang {ListBarang[KodeBarang]["Merk"]} Menjadi {merkBaru}? (Y/N): ')
                                if checker.upper() == 'Y':
                                    ListBarang[KodeBarang]['Merk'] = merkBaru
                                    print('Merk Barang Berhasil Diubah')
                                    menampilkanSeluruh()
                                    break
                                elif checker.upper() == 'N' :
                                    break
                                else :              
                                    print('Maaf Pilihan Tersebut Tidak Ada')
                        elif kolomBarang == 'Stock' :
                            stockBaru = input('Masukkan Stock Baru : ')
                            if stockBaru.isnumeric() == False :
                                print('Stock Barang Tidak Boleh Mengandung Huruf')
                            elif int(stockBaru) == ListBarang[KodeBarang]['Stock'] :
                                print('Tidak Bisa Memasukkan Jumlah Stock Yang Sama, Masukkan Jumlah Stock Lain')
                            else :
                                checker = input (f'Apakah Anda Ingin Mengganti Stock Barang {ListBarang[KodeBarang]["Stock"]} Menjadi {stockBaru}? (Y/N): ')
                                if checker.upper() == 'Y':
                                    ListBarang[KodeBarang]['Stock'] = int(stockBaru)
                                    print('Stock Barang Berhasil Diubah')
                                    menampilkanSeluruh()
                                    break
                                elif checker.upper() == 'N' :
                                    break
                                else :              
                                    print('Maaf Pilihan Tersebut Tidak Ada')
                        elif kolomBarang == 'Harga' :
                            hargaBaru = input('Masukkan Harga Baru : ')
                            if hargaBaru.isnumeric() == False :
                                print('Harga Barang Tidak Boleh Mengandung Huruf')
                            elif int(hargaBaru) == ListBarang[KodeBarang]['Harga'] :
                                print('Tidak Bisa Memasukkan Jumlah Harga Yang Sama, Masukkan Jumlah Harga Lain')
                            else :
                                checker = input (f'Apakah Anda Ingin Mengganti Harga Barang {ListBarang[KodeBarang]["Harga"]} Menjadi {hargaBaru}? (Y/N): ')
                                if checker.upper() == 'Y':
                                    ListBarang[KodeBarang]['Harga'] = int(hargaBaru)
                                    print('Nama Barang Berhasil Diubah')
                                    menampilkanSeluruh()
                                    break
                                elif checker.upper() == 'N' :
                                    break
                                else :              
                                    print('Maaf Pilihan Tersebut Tidak Ada')
                        else :
                            print('Kolom Barang Yang Anda Ketik Salah, Silahkan Masukkan Kolom Yang Benar')
                elif checker.upper() == 'N' :
                    break
                else :              
                    print('Maaf Pilihan Tersebut Tidak Ada')
        elif(pilihanMenu == '2') :
            break
        else :
            print('Mohon Maaf Pilihan Tidak Tersedia, Silahkan Pilih Menu Yang Tersedia')

#FUNGSI DELETE
# Menu hapus data barang
def menghapusDataBarang() :
    while True :
        pilihanMenu = input('''
            +++++++Menu Hapus Data Barang+++++++

                List Menu :
                1. Menghapus Data Barang
                2. Kembali Ke Menu Utama

                Silahkan Pilih Sub Menu: ''')
        if(pilihanMenu == '1') :
            if len(ListBarang) == 0 :
                print('Data Barang Kosong')
                break
            menampilkanSeluruh()
            while True : 
                KodeBarang = input('Masukkan Kode Barang : ')
                KodeBarang = KodeBarang.upper()
                if KodeBarang in ListBarang.keys() :
                    print(f'Barang Dengan Kode Barang : {KodeBarang}')
                    print('Kode : {}, Nama : {}, Tipe : {}, Merk : {}, Stock : {}, Harga : {}'.format(ListBarang[KodeBarang]['Kode'],ListBarang[KodeBarang]['Nama'],ListBarang[KodeBarang]['Tipe'],ListBarang[KodeBarang]['Merk'],ListBarang[KodeBarang]['Stock'],ListBarang[KodeBarang]['Harga']))
                    break
                else :
                    print(f'Barang Dengan Kode Barang : {KodeBarang}')
                    print('***Tidak Ada Data Barang***')
            while True :
                checker = input('Apakah Ingin Menghapus Data Barang Ini? (Y/N): ')
                if checker.upper() == 'Y' :
                    del ListBarang[KodeBarang]
                    print('Data Barang Berhasil Dihapus')
                    break
                elif checker.upper() == 'N' :
                    break
                else : 
                    ('Maaf Pilihan Tersebut Tidak Ada')
        elif(pilihanMenu == '2') :
            break
        else :
            print('Mohon Maaf Pilihan Tidak Tersedia, Silahkan Pilih Menu Yang Tersedia')

#FUNGSI CREATE
# Menu beli barang
def membeliBarang() :
    while True :
        if len(ListBarang) == 0 :
                print('Data Barang Kosong')
                break
        menampilkanSeluruh()
        kodeBarang = input('Masukkan Kode Barang Yang Ingin Dibeli : ')
        kodeBarang = kodeBarang.upper()
        if kodeBarang not in ListBarang.keys() :
            print('Barang Dengan Kode Tersebut Tidak Ada')
        elif kodeBarang in ListBarang.keys() :
            while True :
                jml_beli = input('Masukkan Jumlah Yang Ingin Dibeli : ')
                if jml_beli.isnumeric() == False :
                    print('Jumlah Beli Harus Diinput Dengan Angka')
                else :
                    if int(jml_beli) > ListBarang[kodeBarang]['Stock'] :
                        print('Stock Barang Tidak Mencukupi. Stock Barang {} tersisa {}'.format(ListBarang[kodeBarang]['Nama'],ListBarang[kodeBarang]['Stock']))
                    elif int(jml_beli) <=0 :
                        print('Tidak Bisa Membeli Barang Dengan Jumlah Di Bawah 1')
                    else :
                        Keranjang.append({'Kode' : ListBarang[kodeBarang]['Kode'], 'Nama' : ListBarang[kodeBarang]['Nama'], 'Stock' : int(jml_beli), 'Harga' : ListBarang[kodeBarang]['Harga'], 'Total' : int(jml_beli)*ListBarang[kodeBarang]['Harga']})
                        lihatKeranjang()
                        break
        checker = input ('Apakah Anda Ingin Membeli Barang Lain : (Y/N)')
        if checker.upper() == 'Y' :
            membeliBarang()
        elif checker.upper() == 'N' :
            break
        else : 
            ('Maaf Pilihan Tersebut Tidak Ada')

#FUNGSI READ
# Menu lihat keranjang
def lihatKeranjang() :
    if len(Keranjang) == 0 :
        print('Keranjang Anda Kosong')
    else : 
        print('Keranjang Anda : \n')
        for barang in Keranjang :
            print('Kode : {}, Nama : {}, Stock : {}, Harga : {}, Total : {}'.format(barang['Kode'], barang['Nama'], barang['Stock'], barang['Harga'], barang['Total']))

#FUNGSI DELETE
# Menu hapus keranjang
def menghapusKeranjang() :
    while True :
        pilihanMenu = input('''
            +++++++Menu Hapus Barang Keranjang+++++++

                List Menu :
                1. Menghapus Barang
                2. Kembali Ke Menu Utama

                Silahkan Pilih Sub Menu: ''')
        if(pilihanMenu == '1') :
            if len(Keranjang) == 0 :
                print('Keranjang Anda Kosong')
                break
            for x in range(len(Keranjang)) :
                print('{}. Kode : {}, Nama : {}, Stock : {}, Harga : {}, Total : {}'.format(x, Keranjang[x]['Kode'], Keranjang[x]['Nama'], Keranjang[x]['Stock'], Keranjang[x]['Harga'], Keranjang[x]['Total']))
            while True : 
                barang = input('Masukkan Nomor Barang : ')
                if int(barang) >= len(Keranjang) :
                    print(f'Barang Dengan Nomor Barang : {barang}')
                    print('***Tidak Ada Data Barang***')
                else :
                    barang=int(barang)
                    print(f'Barang Dengan Nomor Barang : {barang}')
                    print('{}. Kode : {}, Nama : {}, Stock : {}, Harga : {}, Total : {}'.format(barang, Keranjang[barang]['Kode'], Keranjang[barang]['Nama'], Keranjang[barang]['Stock'], Keranjang[barang]['Harga'], Keranjang[barang]['Total']))
                    break
            while True :
                checker = input('Apakah Ingin Menghapus Barang Ini Dari Keranjang? (Y/N): ')
                if checker.upper() == 'Y' :
                    del Keranjang[barang]
                    print('Barang Di Keranjang Berhasil Dihapus')
                    break
                elif checker.upper() == 'N' :
                    break
                else : 
                    ('Maaf Pilihan Tersebut Tidak Ada')
        elif(pilihanMenu == '2') :
            break
        else :
            print('Mohon Maaf Pilihan Tidak Tersedia, Silahkan Pilih Menu Yang Tersedia')

#FUNGSI UPDATE
# Menu checkout
def checkout() :
    if len(Keranjang) == 0 :
        print('Keranjang Anda Kosong')
        keranjang()    
    print('Keranjang Anda : \n')
    totalHarga = 0
    for barang in Keranjang :
        print('Kode : {}, Nama : {}, Stock : {}, Harga : {}, Total : {}'.format(barang['Kode'], barang['Nama'], barang['Stock'], barang['Harga'], barang['Total']))
        totalHarga += barang['Total']
    while True :
        print('Total Yang Harus Dibayar = {}'.format(totalHarga))
        jmlUang = int(input('Masukkan jumlah uang : '))
        if(jmlUang > totalHarga) :
            kembali = jmlUang - totalHarga
            print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
            for barang in Keranjang :
                ListBarang[barang['Kode']]['Stock'] -= barang['Stock']
            Keranjang.clear()
            break
        elif(jmlUang == totalHarga) :
            print('Terima kasih')
            for barang in Keranjang :
                ListBarang[barang['Kode']]['Stock'] -= barang['Stock']
            Keranjang.clear()
            break
        else :
            kekurangan = totalHarga - jmlUang
            print('Uang anda kurang sebesar {}'.format(kekurangan))

# Menu keranjang
def keranjang() :
    while True :
        pilihanMenu = input('''
            =======Keranjang Belanja Anda=======

                List Menu :
                1. Melihat Keranjang
                2. Menghapus Barang Di Keranjang
                3. Checkout Belanja
                4. Kembali Ke Menu Customer

                Silahkan Pilih Menu: ''')
        if(pilihanMenu == '1') :
            lihatKeranjang()
        elif(pilihanMenu == '2') :
            menghapusKeranjang()
        elif(pilihanMenu == '3') :
            checkout()
        elif(pilihanMenu == '4') :
            break
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan Lain')

# Menu staff
def toko():
    while True :
        pilihanMenu = input('''
            =======Data Record Barang Toko 420=======

                List Menu :
                1. List Data Barang
                2. Menambahkan Data Barang
                3. Mengubah Data Barang
                4. Menghapus Data Barang
                5. Kembali Ke Menu Utama

                Silahkan Pilih Menu: ''')
        if(pilihanMenu == '1') :
            menampilkanListDataBarang()
        elif(pilihanMenu == '2') :
            menambahkanDataBarang()
        elif(pilihanMenu == '3') :
            mengubahDataBarang()
        elif(pilihanMenu == '4') :
            menghapusDataBarang()
        elif(pilihanMenu == '5') :
            break
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan Lain')

# Menu awal
def menuUtama() :
    while True :
        login = input('''
                ==========Selamat Datang Di Toko 420==========
                
                Masuk Sebagai : 
                1. Staff
                2. Customer
                3. Exit
                Silahkan Pilih Menu : ''')
        if login == '1' :
            toko()
        elif login == '2' :
            customer()
        elif login == '3' :
            break
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan Lain')

# Menu customer
def customer() :
    while True :
        pilihanMenu = input('''
            =======Selamat Datang Di Toko 420=======

            List Menu :
            1. Tampilkan Barang
            2. Membeli Barang
            3. Keranjang
            4. Kembali Ke Menu Utama

            Silahkan Pilih Menu Utama: ''')
        if(pilihanMenu == '1') :
            menampilkanSeluruh()
        elif(pilihanMenu == '2') :
            membeliBarang()
        elif(pilihanMenu == '3') :
            keranjang()
        elif(pilihanMenu == '4') :
            break
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan Lain')


menuUtama()