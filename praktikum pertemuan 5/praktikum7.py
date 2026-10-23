def hitung_subtotal(harga, jumlah):
    return harga * jumlah

def hitung_diskon(subtotal):
    if subtotal >= 100000:
        return subtotal * 0.10
    else:
        return 0

def tampilkan_struk(nama_barang, subtotal, diskon):
    total_akhir = subtotal - diskon
    print("=" * 35)
    print("          STRUK BELANJA          ")
    print("=" * 35)
    print(f"Nama Barang : {nama_barang}")
    print(f"Subtotal    : Rp {subtotal:,.0f}")
    print(f"Diskon      : Rp {diskon:,.0f}")
    print("-" * 35)
    print(f"Total Akhir : Rp {total_akhir:,.0f}")
    print("=" * 35)

# Menguji program kasir dengan harga 25000 dan jumlah 5
nama_produk = "Buku Gambar"
harga_produk = 25000
jumlah_beli = 5

subtotal_belanja = hitung_subtotal(harga_produk, jumlah_beli)
potongan_harga = hitung_diskon(subtotal_belanja)
tampilkan_struk(nama_produk, subtotal_belanja, potongan_harga)