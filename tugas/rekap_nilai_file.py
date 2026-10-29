
def baca_nilai(nama_file):
    data_valid = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                try:
                    nim = bagian[0].strip()
                    nilai = int(bagian[1].strip())
                    data_valid.append((nim, nilai))

                except (ValueError, IndexError):
                    print(f"Baris {nomor_baris} tidak valid dan dilewati.")

    except FileNotFoundError:
        print("Error: File nilai tidak ditemukan.")

    return data_valid


def hitung_rekap(data_valid):
    if not data_valid:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "tertinggi": 0,
            "terendah": 0,
            "lulus": 0
        }

    daftar_nilai = [nilai for nim, nilai in data_valid]

    jumlah = len(daftar_nilai)
    rata_rata = sum(daftar_nilai) / jumlah
    tertinggi = max(daftar_nilai)
    terendah = min(daftar_nilai)
    lulus = sum(1 for nilai in daftar_nilai if nilai >= 60)

    return {
        "jumlah": jumlah,
        "rata_rata": rata_rata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "lulus": lulus
    }

def tulis_rekap(nama_file, rekap):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("HASIL REKAP NILAI MAHASISWA\n")
        file.write("===========================\n")
        file.write(f"Jumlah nilai valid: {rekap['jumlah']}\n")
        file.write(f"Rata-rata nilai: {rekap['rata_rata']:.2f}\n")
        file.write(f"Nilai tertinggi: {rekap['tertinggi']}\n")
        file.write(f"Nilai terendah: {rekap['terendah']}\n")
        file.write(f"Jumlah mahasiswa lulus: {rekap['lulus']}\n")

if __name__ == "__main__":
    file_input = "data/nilai.txt"
    file_output = "data/hasil_rekap.txt"

    data_valid = baca_nilai(file_input)
    rekap = hitung_rekap(data_valid)

    tulis_rekap(file_output, rekap)

    print("\nRekap nilai selesai.")
    print(f"Jumlah nilai valid: {rekap['jumlah']}")
    print(f"Rata-rata: {rekap['rata_rata']:.2f}")
    print(f"Nilai tertinggi: {rekap['tertinggi']}")
    print(f"Nilai terendah: {rekap['terendah']}")
    print(f"Jumlah mahasiswa lulus: {rekap['lulus']}")
    print(f"Hasil disimpan di: {file_output}")

