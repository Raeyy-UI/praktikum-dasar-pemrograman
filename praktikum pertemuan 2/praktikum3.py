harga_satuan = float(input("Masukkan harga satuan barang (Rp): "))
jumlah_barang = int(input("Masukkan jumlah barang: "))
persentase_diskon = float(input("Masukkan persentase diskon (%): "))
subtotal = harga_satuan * jumlah_barang
nominal_diskon = subtotal * (persentase_diskon / 100)
total_bayar = subtotal - nominal_diskon
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal      : Rp {subtotal:,.2f}")
print(f"Diskon ({persentase_diskon}%): Rp {nominal_diskon:,.2f}")
print(f"Total Bayar   : Rp {total_bayar:,.2f}")