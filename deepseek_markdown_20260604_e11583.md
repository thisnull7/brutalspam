<p align="center"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=36&duration=2500&pause=600&color=FF0000&center=true&vCenter=true&width=650&lines=BRUTALSPAM;Nonstop+WhatsApp+OTP+Bomber;MapClub+Brutal+Spammer;Your+Nightmare+Just+Started" alt="BRUTALSPAM" /></p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20termux-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/thisnull7/brutalspam?style=social" />
  <img src="https://img.shields.io/github/forks/thisnull7/brutalspam?style=social" />
</p>

# ═══ BRUTALSPAM ═══

**BRUTALSPAM** adalah senjata spam OTP tanpa henti yang menargetkan layanan **MapClub**. Dengan memanfaatkan token tamu yang telah di-hardcode, alat ini mengirimkan permintaan OTP WhatsApp secara brutal setiap ~60 detik (sesuai batas rate limit server). Tidak perlu login, tidak perlu ambil token manual — langsung jalankan, masukkan nomor target, dan biarkan alat bekerja.

> **⚠️ PERINGATAN KERAS**  
> Alat ini dibuat untuk **pendidikan keamanan** dan **pengujian stres server sendiri**. Penyalahgunaan terhadap nomor orang lain tanpa izin adalah **ilegal**. Pengembang tidak bertanggung jawab atas segala kerusakan atau pelanggaran hukum yang disebabkan oleh penggunaan alat ini. **Gunakan dengan bijak!**

---

## 🩸 TAMPILAN

<p align="center">
  <img src="https://raw.githubusercontent.com/thisnull7/brutalspam/refs/heads/main/otp.png" alt="BRUTALSPAM Preview" width="600" />
</p>

---

## 🔥 FITUR UTAMA

- **Spam OTP WhatsApp** ke nomor target menggunakan endpoint MapClub.
- **Token tamu terpasang** – tidak perlu repot ambil token dari Burp Suite atau browser.
- **Mode ganda** – pilih jumlah pesan tertentu atau nonstop berdasarkan durasi (detik).
- **Otomatis menghormati rate limit** – mendeteksi `timeRemaining` dari respons server dan menunggu sebelum mengirim lagi.
- **Tampilan terminal seram** – banner merah darah, animasi spinners, progress real-time.
- **Konversi nomor pintar** – input `0895xxx`, `895xxx`, atau `62895xxx` akan otomatis diubah ke format internasional.
- **Cross-platform** – Windows, Linux, Termux Android.

---

## 📦 PERSYARATAN

- Python **3.8** atau lebih tinggi
- Koneksi internet stabil
- Modul Python: `requests`, `colorama` (opsional, untuk warna)

---

## ⚙️ INSTALASI

```bash
# clone repositori
git clone https://github.com/thisnull7/brutalspam.git
cd brutalspam

# install dependensi
pip install -r requirements.txt