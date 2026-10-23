def buat_biodata(nama, umur, jurusan):
    print(f"Nama    : {nama}")
    print(f"Umur    : {umur} tahun")
    print(f"Jurusan : {jurusan}")
    print("-" * 30)

# 1. Pemanggilan menggunakan positional argument (urutan sesuai definisi: nama, umur, jurusan)
print("=== Pemanggilan dengan Positional Argument ===")
buat_biodata("M. Raesya Nizar Ali", 19, "Sistem Informasi")

# 2. Pemanggilan menggunakan keyword argument dengan urutan yang berbeda
print("=== Pemanggilan dengan Keyword Argument (Urutan Berbeda) ===")
buat_biodata(jurusan="Sistem Informasi", nama="M. Raesya Nizar Ali", umur=19)