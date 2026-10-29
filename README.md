
# Pertemuan 12 - File Input-Output dan Error Handling

## Identitas
- Nama: Zahra Amelia
- NIM: 2225250044
- Kelas: [Isi kelas kamu]
- Mata Kuliah: Algoritma dan Pemrograman

## Tujuan
Mempelajari pengolahan file teks menggunakan Python, membaca dan menulis data, serta menangani kesalahan menggunakan try-except.

## Struktur Folder
- latihan/: Berisi enam program latihan file I/O dan error handling.
- tugas/: Berisi program utama rekap nilai mahasiswa.
- data/: Berisi file input dan output program.
- README.md: Dokumentasi proyek.
- .gitignore: Daftar file yang diabaikan Git.

## Format File Input
File data/nilai.txt menggunakan format NIM,nilai.
Setiap baris berisi NIM dan nilai yang dipisahkan dengan koma.

Contoh:
A001,85
A002,78
A003,92

## Cara Menjalankan Program
Buka terminal di folder utama proyek, lalu jalankan:

python tugas/rekap_nilai_file.py

## Penanganan Error
- FileNotFoundError: Ditangani ketika file input tidak ditemukan.
- ValueError: Ditangani ketika nilai tidak dapat dikonversi menjadi bilangan bulat.
- IndexError: Ditangani ketika format baris tidak memiliki bagian yang diperlukan.

Data yang tidak valid dilewati, sedangkan data valid digunakan untuk menghitung rekap nilai.

## Pengujian
- File input tersedia dan dapat dibaca.
- Baris dengan nilai bukan angka dilewati.
- Jumlah nilai valid dihitung.
- Rata-rata, nilai tertinggi, dan nilai terendah dihitung.
- Jumlah mahasiswa dengan nilai minimal 60 dihitung.
- Hasil rekap disimpan ke data/hasil_rekap.txt.

## Refleksi
Melalui tugas ini, saya belajar membaca dan menulis file teks, memproses data per baris, menggunakan fungsi, serta menangani kesalahan agar program tetap dapat berjalan dengan baik.
