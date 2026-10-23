def sapa_mahasiswa(nama, sapaan='Selamat belajar'):
    print(f"{sapaan}, {nama}!")

# Pengujian 1: Memberikan kedua argumen
print("=== Pengujian dengan kedua argumen ===")
sapa_mahasiswa("M Raesya Nizar Ali", "Selamat pagi")

# Pengujian 2: Hanya memberikan nama (menggunakan sapaan default)
print("\n=== Pengujian hanya memberikan nama ===")
sapa_mahasiswa("M Raesya Nizar Ali")