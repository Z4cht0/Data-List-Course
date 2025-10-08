import time
#data list
list_nama = []
list_nim = []
list_prodi = []
list_fakultas = []
list_universitas = []

data_nama1 = input('Masukkan nama anda: ')
data_nim1 = input('Masukkan NIM anda: ')
data_prodi1 = input('Masukkan prodi anda: ')
data_fakultas1 = input('Masukkan fakultas anda: ')
data_universitas1 = input('Masukkan universitas anda: ')

#memasukkan data ke dalam list
list_nama.append(data_nama1)
list_nim.append(data_nim1)
list_prodi.append(data_prodi1)
list_fakultas.append(data_fakultas1)
list_universitas.append(data_universitas1)
print('data telah tersimpan')
time.sleep(3)
print(f'data yang tersimpan adalah: \nNama: {list_nama} \nNIM: {list_nim} \nProdi: {list_prodi} \nFakultas: {list_fakultas} \nUniversitas: {list_universitas}')
is_data_kedua = input('apakah anda ingin memasukkan data ke dua? (y/n): ')
if is_data_kedua == 'y':
    data_nama2 = input('Masukkan nama anda: ')
    data_nim2 = input('Masukkan NIM anda: ')
    data_prodi2 = input('Masukkan prodi anda: ')
    data_fakultas2 = input('Masukkan fakultas anda: ')
    data_universitas2 = input('Masukkan universitas anda: ')

    #memasukkan data ke dalam list
    list_nama.append(data_nama2)
    list_nim.append(data_nim2)
    list_prodi.append(data_prodi2)
    list_fakultas.append(data_fakultas2)
    list_universitas.append(data_universitas2)
    print('data telah tersimpan')
    time.sleep(3)
    list_nama.sort()
    list_nim.sort()
    list_prodi.sort()
    list_fakultas.sort()
    list_universitas.sort()
    print(f'data yang tersimpan adalah: \nNama: {list_nama} \nNIM: {list_nim} \nProdi: {list_prodi} \nFakultas: {list_fakultas} \nUniversitas: {list_universitas}')
elif is_data_kedua == 'n':
    print('terima kasih telah menggunakan program ini')