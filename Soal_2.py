nilai = [
    [80, 75, 90],
    [85, 70, 95],
    [78, 88, 84],
    [92, 76, 89],
]

def hitung_rata_rata(nilai):
    rata_mk = [sum(col) / len(col) for col in zip(*nilai)]
    rata_mhs = [sum(row) / len(row) for row in nilai]
    return rata_mk, rata_mhs

def tampilkan_hasil(nilai):
    print("Tabel Nilai:")
    for i, baris in enumerate(nilai, start=1):
        print(f"Mahasiswa {i}: {baris}")

    rata_mk, rata_mhs = hitung_rata_rata(nilai)
    print("\nRata-rata per Mata Kuliah:")
    for i, rata in enumerate(rata_mk, start=1):
        print(f"Mata Kuliah {i}: {rata:.2f}")

    print("\nRata-rata per Mahasiswa:")
    for i, rata in enumerate(rata_mhs, start=1):
        print(f"Mahasiswa {i}: {rata:.2f}")

tampilkan_hasil(nilai)
