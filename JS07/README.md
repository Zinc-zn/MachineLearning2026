# JS07 — Klasterisasi (K-Means & DBSCAN)

Pengerjaan Jobsheet 07 mengikuti modul [JTI - Modul Praktikum Pembelajaran Mesin](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-mah/js07-klasterisasi). Semua notebook sudah dieksekusi penuh (output & grafik tersimpan di dalamnya).

## Isi Folder

| File | Isi |
|---|---|
| `JS07_01.ipynb` | Lab 1 — K-Means pada `Iris.csv`: seleksi fitur, SSE (`inertia_`), elbow method |
| `JS07_02.ipynb` | Lab 2 — Data non-linier `make_moons`: K-Means gagal vs DBSCAN `eps=0.3, min_samples=2`; evaluasi silhouette & DBI |
| `JS07_03.ipynb` | Lab 3 — Kompresi warna citra `flower.jpg` dengan `MiniBatchKMeans` (16 warna) |
| `JS07_Tugas.ipynb` | Tugas — Klasterisasi data nasabah kartu kredit (`CC_Customer_Dataset.csv`): 6 soal |
| `Iris.csv` | Dataset Iris (dengan kolom `Id`, dari halaman modul) |
| `CC_Customer_Dataset.csv` | Dataset nasabah kartu kredit (dari halaman modul) |
| `_modul/` | Snapshot markdown halaman modul + script pembuat/eksekutor notebook |
| `.venv/` | Virtual environment Python 3.14 (scikit-learn, seaborn, dst.) |

## Cara Menjalankan

```bash
# dari folder JS07
.venv\Scripts\activate
jupyter notebook
```

## Ringkasan Hasil

| Percobaan | Hasil utama |
|---|---|
| Lab 1 (K-Means Iris) | k=2 (asumsi visual): SSE 152.37; elbow method → **k=3** paling optimal |
| Lab 2 (DBSCAN moons) | K-Means silhouette 0.4922 (salah bentuk); DBSCAN membentuk 2 cluster sempurna (0 noise), silhouette 0.3259 (asumsi linier metrik tidak terpenuhi), DBI 1.1623 |
| Lab 3 (kompresi citra) | 16 juta warna → 16 cluster warna; kualitas visual terjaga, tiap piksel cukup 4 bit (±6× hemat) |
| Tugas (nasabah) | (1) sebaran `Avg_Credit_Limit` vs `Total_Credit_Cards` **tidak linier**; (2-3) K-Means 2 variabel, elbow → **k=3**; (4) DBSCAN seluruh 5 variabel (`eps=0.9` dari k-distance graph, `min_samples=6`) → 3 cluster + 31 noise (4.7%); (5) elbow seluruh variabel konsisten k=3; (6) silhouette (non-noise) **0.4810**, DBI **0.7961** |

> Catatan lingkungan: Python 3.14 + scikit-learn 1.9. `KMeans`/`MiniBatchKMeans` diberi `random_state` agar dapat direproduksi. Pada Tugas no. 5, DBSCAN tidak memiliki parameter k sehingga elbow method dijalankan dengan K-Means pada seluruh variabel sebagai pelengkap analisis (diinterpretasikan di notebook).
