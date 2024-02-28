# CapstoneProjectM1_AplikasiAdminPerpustakaan
Capstone Project Purwadhika Bandung: Program CRUD menggunakan regular funcion dari aplikasi Python

## Konsep
Pada file ini menampilkan aplikasi Admin Perpustakaan menggunakan program CRUD yang memiliki 4 fitur utama, yaitu:
  - Create: menambahkan data buku dalam bentuk dictionary berdasarkan input user
  - Update: memperbaharui data buku yang sudah ada dalam dictionary
  - Delete: menghapus sebagian data buku berdasarkan 'ID_BUKU' dan menghapus daftar buku secara keseluruhan (reset)
  - Read: melihat daftar buku yang sudah ada, user dapat mensortir data buku berdasarkan key (judul, penulis, dan tahun terbit) dan dapat memfilter data buku berdasarkan kategori buku

Dictionary yang digunakan pada program ini berisikan 6 kolom (keys) termasuk ID buku yang merupakan Primary Key dari daftar buku, kolom tersebut berisikan 'ID' (Primary Key, 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', dan 'Kategori'

## Tujuan
Menyediakan fasilitas administrasi Perpustakaan agar dapat mengatur aktivitas pendataan daftar buku pada Perpustakaan

## Stakeholders
1. End Users: Pegawai administrasi (admin) Perpustakaan yang berkaitan dengan pengolahan data buku.
2. Developers: Tim Developer yang bertugas membangun aplikasi, dan pemeliharaan aplikasi .
3. Investors : Penerbit buku.

## Keterbatasan
1. Data Terbatas: Program menggunakan data dummy untuk admin perpustakaan.
2. Kerja Program Manuak: Program ini digunakan/dijalankan secara manual dan tidak bisa terbaharui secara otomatis.

## Isi Data
1. ID Buku
2. Data Buku (Judul, Penulis, Penerbit, Tahun Terbit, Kategori)

# Instruksi
sebelum menjalanlkan program ini harus dipastikan sudah menginstall Python dan tabulate 
--> pip install tabulate (pada terminal desktop)


