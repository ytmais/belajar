class Mahasiswa():
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

print("=== Data Mahasiswa ===")
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
jurusan = input("Masukkan Jurusan: ")

print("\n=== Hasil Input Data Mahasiswa ===")
mahasiswa = Mahasiswa(nama, nim, jurusan)
print(f"Nama: {mahasiswa.nama}")
print(f"NIM: {mahasiswa.nim}")
print(f"Jurusan: {mahasiswa.jurusan}")