## Deskripsi Proyek

Proyek ini bertujuan untuk mengumpulkan dan mempersiapkan data review pengguna aplikasi **BRImo (BRI Mobile)** dari Google Play Store sebagai tahap awal analisis sentimen menggunakan metode **Natural Language Processing (NLP)**.

BRImo merupakan aplikasi mobile banking resmi dari **Bank Rakyat Indonesia (BRI)** yang menyediakan berbagai layanan transaksi digital seperti transfer antar bank, pembayaran tagihan, pembelian pulsa, top up e-wallet, serta pengecekan saldo dan mutasi rekening. Sebagai aplikasi dengan jumlah pengguna yang besar, BRImo memiliki banyak ulasan dari pengguna yang dapat digunakan untuk memahami pengalaman serta opini pengguna terhadap layanan yang tersedia.

Pada tahap ini, fokus pengerjaan meliputi **pengambilan data review (data scraping) serta preprocessing teks hingga tahap tokenisasi** untuk mempersiapkan data sebelum dilakukan analisis sentimen lebih lanjut.

---

## Prosedur Preprocessing

- **Scraping**  
  Mengambil data review aplikasi BRImo dari Google Play Store menggunakan library `google-play-scraper`.

- **Cleaning**  
  Membersihkan teks dengan menghapus angka, simbol, dan tanda baca yang tidak diperlukan.

- **Case Folding**  
  Mengubah seluruh teks menjadi huruf kecil agar format teks menjadi lebih konsisten.

- **Tokenization**  
  Memecah kalimat review menjadi kata-kata tunggal menggunakan `nltk.tokenize.word_tokenize()`.

---

## Tools yang Digunakan

- `google-play-scraper`
- `pandas`
- `numpy`
- `nltk`
