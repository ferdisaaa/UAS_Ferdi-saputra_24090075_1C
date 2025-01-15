from Soal_3 import Gambaran,enqueue,deque,lihat_semua
while True:

    Gambaran()
 
    pilihan = int(input('Masukkan pilihan 1/2/3/4 :'))

    if pilihan == 1:
        value = input(f"Ditambahkan kedalam antrian: ")
        enqueue(value)

    elif pilihan == 2:
        deque()

    elif pilihan == 3:
        lihat_semua()

    elif pilihan == 4:
        keluar = input('Apakah kamu igin keluar Y/T:')
        if keluar == 'Y':
            break

print({lihat_semua()})