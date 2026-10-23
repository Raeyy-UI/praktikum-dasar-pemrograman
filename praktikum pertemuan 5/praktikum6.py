def konversi_menit_ke_detik(menit):
    """
    Mengonversi durasi waktu dari satuan menit ke satuan detik.

    Parameters:
    menit (int atau float): Jumlah waktu dalam menit yang ingin dikonversi.

    Returns:
    int atau float: Jumlah waktu hasil konversi dalam satuan detik.
    """
    detik = menit * 60
    return detik

# Menguji fungsi dengan input 3 menit
menit_input = 3
hasil_detik = konversi_menit_ke_detik(menit_input)

print(f"{menit_input} menit sama dengan {hasil_detik} detik.")