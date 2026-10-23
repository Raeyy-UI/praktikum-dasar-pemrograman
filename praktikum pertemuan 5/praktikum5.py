# Variabel Global (Dapat diakses di mana saja di dalam file ini)
biaya_admin = 2500

def hitung_total(harga):
    # Variabel Lokal 'total' (Hanya dapat diakses di dalam fungsi ini)
    total = harga + biaya_admin
    return total

# Memanggil fungsi dengan harga 15000
hasil_pembayaran = hitung_total(15000)
print(f"Total Pembayaran: {hasil_pembayaran}")