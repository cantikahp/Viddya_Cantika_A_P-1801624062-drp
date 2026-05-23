from datetime import datetime

print("=== Aplikasi Manajemen Aktivitas ===")

aktivitas = input("Masukkan aktivitas: ").lower()

if aktivitas == "sarapan":
    menu = input("Masukkan menu sarapan: ").lower()

    if menu == "telur" or menu == "ikan" or menu == "nugget":
        print("Bahan tersedia, silakan dimasak terlebih dahulu.")
    else:
        print("Bahan tidak tersedia, silakan membeli bahan terlebih dahulu.")

elif aktivitas == "berangkat kerja":
    sekarang = datetime.now()

    print("Waktu sekarang:", sekarang.strftime("%H:%M"))

    if sekarang.hour >= 8:
        print("Anda terlambat masuk kerja!")
    else:
        print("Anda belum terlambat masuk kerja.")

else:
    print("Aktivitas tidak dikenali.")