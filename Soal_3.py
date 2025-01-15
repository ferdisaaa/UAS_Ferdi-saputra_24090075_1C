Antrian = []

def Gambaran():
    print('1.Tambah Antrian')
    print('2.Lanjutan Antrian Selanjutnya')
    print('3.Lihat antrian ')
    print('4.keluar')

def enqueue(value):
    Antrian.append(value)
    print(f'"{value}" ditambahkan ke dalam antrian')

    
def deque():
    Antrian.pop(0)

def isEmpty():
    return len(Antrian) == 0

def front():
    if isEmpty():
        return 'antrian kosong'
    
def second():
    if isEmpty() or len(Antrian)==1:
        return 'Kosong'
    else :
        return Antrian[1]
    
def lihat_semua():
    for i in Antrian:
        print(i)