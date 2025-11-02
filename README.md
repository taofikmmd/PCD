Oke! Berikut aku buatkan versi **README.md yang lebih menarik** untuk GitHub, lengkap dengan **instruksi, screenshot GUI, dan contoh citra**. Kamu bisa langsung pakai, dan di GitHub orang bisa langsung lihat fungsionalitas project.

---

````markdown
# UTS Pengolahan Citra Digital

## 📌 Deskripsi

Proyek ini adalah implementasi praktikum **Pengolahan Citra Digital** untuk Ujian Tengah Semester (*UTS*) dengan fokus pada konsep **Smart Health**, menampilkan citra menggunakan tombol (*trigger*), konversi ke grayscale, analisis matriks piksel RGB, dan analisis sederhana area terang/gelap pada citra.

Program ini menggunakan **Python**, **OpenCV**, dan **Tkinter** untuk GUI.

---

## 🛠️ Fitur

1. **Tampilkan Citra Berwarna**  
   Menampilkan citra asli (RGB) melalui tombol trigger.

2. **Tampilkan Citra Keabuan (Grayscale)**  
   Mengubah citra berwarna menjadi grayscale dan menampilkannya.

3. **Tampilkan Matriks Piksel RGB**  
   Menampilkan nilai R, G, B pada piksel tertentu di terminal.

4. **Analisis Smart Health Sederhana**  
   Menghitung persentase area terang pada citra sebagai contoh analisis kesehatan.

---

## 💻 Cara Menjalankan

1. **Pastikan Python 3.x sudah terinstal**  
   ```bash
   python --version
````

Jika belum, unduh dari [Python.org](https://www.python.org/downloads/).

2. **Buat virtual environment (opsional tapi direkomendasikan)**

   ```bash
   python -m venv venv
   ```

   Aktifkan environment:

   * **Windows:** `venv\Scripts\activate`
   * **Linux/Mac:** `source venv/bin/activate`

3. **Install modul yang dibutuhkan**

   ```bash
   pip install opencv-python pillow numpy
   ```

4. **Siapkan file citra**

   * Letakkan gambar di folder project, misal `xray.jpg`.
   * Pastikan nama file sesuai dengan yang ada di `main.py`.

5. **Jalankan program**

   ```bash
   python main.py
   ```

---

## 🖼️ Tampilan GUI

### 1️⃣ Citra Berwarna

![Citra Berwarna](screenshots/color_example.png)

### 2️⃣ Citra Keabuan (Grayscale)

![Citra Keabuan](screenshots/gray_example.png)

### 3️⃣ Output Matriks RGB di Terminal

```
Ukuran citra: (512, 512, 3)
Nilai piksel pada (100,100): R=180, G=172, B=165
```

### 4️⃣ Analisis Smart Health

```
Area terang: 48.32% dari total piksel
```

> *Catatan:* Screenshots dan output di atas hanyalah contoh. Kamu bisa mengganti citra sesuai kebutuhan.

---

## 📁 Struktur Proyek

```
UTS_Pengolahan_Citra_Digital/
│
├─ main.py              # Kode utama praktikum
├─ xray.jpg             # Contoh citra
├─ README.md            # Penjelasan proyek
└─ screenshots/         # Folder untuk screenshot GUI
     ├─ color_example.png
     └─ gray_example.png
```

---

## 🧠 Penjelasan Kode

* `cv2.imread()` → Membaca citra dari file.
* `cv2.cvtColor()` → Mengubah format warna (BGR → RGB atau grayscale).
* `np.sum()` → Digunakan untuk analisis piksel (misal menghitung area terang/gelap).
* `Tkinter` → Membuat GUI dengan tombol trigger untuk menampilkan citra.
* `PIL.ImageTk` → Menghubungkan OpenCV image dengan Tkinter.

---

## 📈 Tujuan Pembelajaran

* Memahami **konversi citra berwarna ke grayscale**.
* Mengerti **struktur matriks piksel RGB**.
* Mengimplementasikan **trigger tombol GUI** untuk menampilkan citra.
* Mempelajari konsep **analisis citra untuk Smart Health**.

---

## 📚 Referensi

* [OpenCV Documentation](https://docs.opencv.org/)
* [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
* Modul Praktikum Pengolahan Citra Digital – Smart Health

```

---

💡 **Tips untuk GitHub:**

1. Buat folder `screenshots/` di project kamu.  
2. Masukkan screenshot GUI (`color_example.png` dan `gray_example.png`).  
3. GitHub akan menampilkan screenshot langsung di README.  

---

Kalau mau, aku bisa buatkan **versi README yang sudah include GIF animasi tombol diklik**, supaya GitHub langsung menampilkan interaksi GUI tanpa perlu buka program.  

Apakah mau aku buatkan versi GIF itu juga?
```
