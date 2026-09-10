import numpy as np

# 1. Membuat array dengan rentang angka
a = np.arange(1, 11)
b = np.linspace(0, 1, 5)

print("arange: ", a)
print("linspace: ", b)

# 2. mengubah bentuk array
matriks = np.arange(1, 13).reshape(3, 4)
print("\nMatriks: ")
print(matriks)

# 3. Indexing dan Slicing
print("Elemen beris 1 kolom 2: ", matriks[0, 1])
print("Baris pertama: ", matriks[0, :])
print("Kolom kedua: ", matriks[:, 1])
print("Dua baris pertama: ")
print(matriks[:2, :])

# 4. Filter dengan kondisi
data = np.array([10, 25, 30, 5, 42, 10])
print("\nData lebih besar dari 20: ", data[data > 20])
print("Data genap: ", data[data % 2 == 0])

# 5. operasi antar-array
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# 6. Fungsi statistik
nilai = np.array([70, 85, 90, 65, 80])

print("\nRata-rata: ", np.mean(nilai))
print("Median: ", np.median(nilai))
print("Standar aviasi: ", np.std(nilai))
print("Urutan data: ", np.sort(nilai))


# 7. Angka acak
acak = np.random.randint(1,101, size=5)
print("\nAngka acak: ", acak)

# 8. Menggabungkan array
nama_depan = np.array(["Budi", "Siti"])
nama_belakang = np.array(["Santoso", "Aminah"])

print("Gabungan nama: ", np.concatenate((nama_depan, nama_belakang)))