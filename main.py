pengambilan_produk = 1020000
jumlah_kendaraan = 6

if pengambilan_produk >= 1000000:
    if jumlah_kendaraan > 8:
        print("Anda memenuhi syarat sebagai Distributor di daerah ini.")
    else:
        print("Jumlah kendaraan Anda tidak memenuhi syarat.")
else:
    print("Pengambilan produk Anda tidak memenuhi syarat.")