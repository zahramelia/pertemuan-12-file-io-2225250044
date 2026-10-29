
teks_nilai = ["85", "78", "abc", "92", "70"]

for teks in teks_nilai:
    try:
        nilai = int(teks)
        print(f"Nilai berhasil dibaca: {nilai}")
    except ValueError:
        print(f"Error: '{teks}' bukan bilangan bulat yang valid.")
