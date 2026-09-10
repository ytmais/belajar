import numpy as np

angka = np.array([1, 2, 3, 4, 5, 6])

print("Array: ", angka)
print("Tipe data: ", angka.dtype)
print("Jumlah elemen: ", angka.size)
print("Bentuk array: ", angka.shape)


print("Dikali 2: ", angka * 2)
print("Ditambah 20: ", angka + 20)
print("Jumlah: ", np.sum(angka))
print("Rata-rata : ", np.mean(angka))
print("Nilai maksimum : ", np.max(angka))
print("Nilai minimum : ", np.min(angka))


matriks = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatriks : ")
print(matriks)
print("Bentuk matriks :", matriks.shape)
print("Baris pertama matriks :", matriks[0])
print("Kolom kedua :", matriks[:, 1])