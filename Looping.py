print("=== Layout Catur ===")

for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("⬛", end="")
        else:
            print("⬜", end="")
    print()

print("\n=== Manajemen Aktivitas ===")

daftar_aktivitas = []

jumlah = int(input("Berapa aktivitas yang ingin ditambahkan? "))

for i in range(jumlah):
    print(f"\nAktivitas ke-{i+1}")

    aktivitas = input("Masukkan aktivitas: ")
    jam = input("Masukkan jam aktivitas: ")
    prioritas = input("Masukkan prioritas (tinggi/sedang/rendah): ")

    data = {
        "aktivitas": aktivitas,
        "jam": jam,
        "prioritas": prioritas
    }

    daftar_aktivitas.append(data)

print("\n=== Daftar Aktivitas ===")

for i, data in enumerate(daftar_aktivitas, start=1):
    print(f"\n{i}. Aktivitas : {data['aktivitas']}")
    print(f"   Jam       : {data['jam']}")
    print(f"   Prioritas : {data['prioritas']}")

print("\nSemua aktivitas berhasil disimpan!")