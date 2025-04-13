# Tugas-Framework
Nama: Nurhikma
Nim: 240907501018
Kelas: B

1. Menginstal Python dan Flask, Flask adalah framework web yang memungkinkan pengembang untuk membuat aplikasi web dengan cepat dan efisien. Untuk menginstal Flask, gunakan perintah berikut di terminal:
(pip install Flask)
2. Struktur Proyek
1. Buat Folder Proye: Siapkan folder khusus untuk proyek.
2. Buat File `app.py`: Di dalam folder proyek, buat file bernama `app.py`. File ini akan berisi kode utama aplikasi.
3. Pengkodean Aplikasi
Import Flask dan Inisialisasi Aplikasi
Di dalam `app.py`, import Flask dan buat instance aplikasi:
python
from flask import Flask
app = Flask(__name__)
4. Membuat Rute
Rute digunakan untuk menentukan tampilan halaman web. Misalnya, untuk membuat halaman utama:
python
@app.route('/')
def home():
    return 'Selamat datang di aplikasi saya!'
5. Menjalankan Aplikasi
Untuk menjalankan aplikasi, tambahkan kode berikut di bagian akhir `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True)
```
Ini akan menjalankan server pengembangan Flask, dan dapat diakses aplikasi di browser dengan membuka `http://127.0.0.1:5000/`.
