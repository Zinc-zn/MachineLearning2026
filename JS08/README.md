# JS08 — Hierarchical Clustering & HDBSCAN

Pengerjaan Jobsheet 08 mengikuti modul [JTI - Modul Praktikum Pembelajaran Mesin](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-mah/js08-hierarchical-clustering). Semua notebook sudah dieksekusi penuh (output & grafik tersimpan di dalamnya).

## Isi Folder

| File | Isi |
|---|---|
| `JS08_01.ipynb` | Lab 1 — Agglomerative Clustering pada `Mall_Customers.csv`: dendogram (ward), model 5 cluster, silhouette |
| `JS08_02.ipynb` | Lab 2 — HDBSCAN vs DBSCAN: uji scale invariance, dataset multiscale, fungsi visualisasi |
| `JS08_03.ipynb` | Lab 3 — Eksperimen hyperparameter HDBSCAN: `min_cluster_size`, `min_samples`, `cut_distance`; evaluasi silhouette & DBI |
| `JS08_Tugas1.ipynb` | Tugas 1 — Agglomerative Clustering seluruh variabel `CC_Customer_Dataset.csv` + scatterplot + evaluasi |
| `JS08_Tugas2.ipynb` | Tugas 2 — Clustering HDBSCAN pada dataset nyata (Iris) + visualisasi PCA + analisis vs label asli |
| `Mall_Customers.csv` | Dataset customer toko ritel (dari halaman modul) |
| `CC_Customer_Dataset.csv` | Dataset nasabah kartu kredit (sama dengan Tugas Lab JS07) |
| `_modul/` | Snapshot markdown halaman modul + script pembuat/eksekutor notebook |
| `.venv/` | Virtual environment **Python 3.10** (hdbscan 0.8.44, scikit-learn, dst.) — paket `hdbscan` belum tersedia untuk Python 3.14 |

## Cara Menjalankan

```bash
# dari folder JS08
.venv\Scripts\activate
jupyter notebook
```

> Jika `.venv` dibuat ulang: `py -3.10 -m venv .venv` lalu `pip install hdbscan scikit-learn pandas matplotlib seaborn ipykernel nbformat nbclient jinja2`.

## Ringkasan Hasil

| Percobaan | Hasil utama |
|---|---|
| Lab 1 (Mall) | Dendogram → 5 cluster (threshold 100-150); silhouette k=5 = **0.5530** (tertinggi di antara k=3..8) |
| Lab 2 (HDBSCAN) | DBSCAN tidak invarian skala (perlu setel ulang `eps`); HDBSCAN identik pada skala 1/0.5/3 dan menemukan 4 cluster pada data multiscale tanpa parameter `eps` |
| Lab 3 (hyperparameter) | `min_cluster_size` besar → cluster berkurang; `min_samples` besar → lebih banyak noise; `cut_distance` = "DBSCAN dari pohon HDBSCAN" pada berbagai level kepadatan |
| Tugas 1 (nasabah) | k terbaik **3** (dendogram + silhouette); silhouette **0.5148**, DBI **0.6810**; cluster 385/225/50 nasabah (rendah-menengah / menengah / premium) |
| Tugas 2 (Iris) | HDBSCAN membentuk **2 cluster tanpa noise**: cluster 0 = setosa (50, sempurna), cluster 1 = versicolor+virginica (100, memang tumpang tindih); **ARI = 0.5681** |

> Catatan lingkungan: Python 3.10 + hdbscan 0.8.44 + scikit-learn. Instalasi hdbscan pada venv lokal (bukan `!pip install` Colab). Seluruh seed (`random_state=42`) dipasang agar hasil dapat direproduksi.
