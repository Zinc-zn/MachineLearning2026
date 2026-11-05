# JS09 — Approximate Nearest Neighbors (ANNOY, FAISS, HNSW)

Pengerjaan Jobsheet 09 mengikuti modul [JTI - Modul Praktikum Pembelajaran Mesin](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-mah/js09-approximate-nearest-neighbors-ann). Semua notebook sudah dieksekusi penuh (output & grafik tersimpan di dalamnya).

## Isi Folder

| File | Isi |
|---|---|
| `JS09_01.ipynb` | Lab 1 — Exact NN vs ANNOY (1000 data 2D, 3 tree, metrik Euclidean) |
| `JS09_02.ipynb` | Lab 2 — Exact NN vs FAISS (IndexFlatL2 vs IndexIVFPQ) |
| `JS09_03.ipynb` | Lab 3 — Exact NN vs HNSW (`hnswlib`, k=5, ef=50) |
| `JS09_04.ipynb` | Lab 4 — ANNOY vs FAISS vs HNSW pada **1.000.000 data 5D** (build & query time) |
| `JS09_05.ipynb` | Lab 5 — Uji performansi ANN dengan **recall query** (100k×128D, kurva recall vs query time) |
| `JS09_Tugas1.ipynb` | Tugas 1 — Benchmark grid: 1000/1.000.000 data × 2D/5D × ANNOY/FAISS/HNSW (tabel build, query, recall@10) |
| `JS09_Tugas2.ipynb` | Tugas 2 — Exact NN vs ANNOY vs FAISS vs HNSW pada dataset **Spotify** (fitur audio + StandardScaler) |
| `spotify_songs.csv` | Dataset Spotify ±32.833 track (mirror publik TidyTuesday dari dataset Kaggle modul — unduhan Kaggle memerlukan akun; kolom fitur identik dengan boilerplate modul) |
| `_modul/` | Snapshot markdown halaman modul, script pembuat/eksekutor notebook, `_conda_pkgs/` (paket annoy & hnswlib yang dipakai instalasi) |
| `.venv/` | Virtual environment **Python 3.10** (annoy, faiss-cpu, hnswlib, scikit-learn, dst.) |

## Cara Menjalankan

```bash
# dari folder JS09
.venv\Scripts\activate
jupyter notebook
```

> Catatan instalasi di Windows tanpa compiler C++: `annoy` dan `hnswlib` tidak menyediakan wheel Windows di PyPI. Pada `.venv` ini keduanya dipasang dari paket prebuilt conda-forge (`python-annoy 1.17.3` & `hnswlib 0.8.0`, win-64 py310) yang diekstrak ke site-packages; `faiss-cpu 1.15.1` dipasang via pip (wheel resmi). Langkah detail ada di `_modul/_conda_pkgs/`.

## Ringkasan Hasil

| Percobaan | Hasil utama |
|---|---|
| Lab 1 (ANNOY) | 3-NN: ANNOY ±0.1-0.2 ms vs brute force ±5-10 ms; 2 dari 3 tetangga identik, kompensasi kecepatan signifikan |
| Lab 2 (FAISS) | IVF+PQ menemukan tetangga yang sama dengan exact NN dengan waktu lebih singkat pada data kecil |
| Lab 3 (HNSW) | 5-NN identik dengan exact NN; jarak hnswlib = kuadrat jarak Euclidean (space `l2`) |
| Lab 4 (1M×5D) | Build: ANNOY ±20-25 s, FAISS flat <1 s, HNSW ±80-155 s. Query: HNSW/ANNOY ±0.2-0.3 ms, FAISS flat (exact) ±10-13 ms |
| Lab 5 (recall) | HNSW paling dekat sudut kanan atas (recall tinggi, query tercepat); FAISS IVF cepat namun recall bergantung `nprobe`; ANNOY butuh `search_k` besar untuk recall tinggi |
| Tugas 1 (grid) | Tabel lengkap di notebook — build 1M: ANNOY 19-25 s / FAISS IVF 0.7-0.9 s / HNSW 78-93 s; query semuanya sub-milidetik; **recall@10: FAISS & HNSW 1.0, ANNOY 0.9-1.0** |
| Tugas 2 (Spotify) | ANN menemukan 9-10 dari 10 tetangga yang sama dengan exact NN (±33 ribu track, 9 fitur ternormalisasi), dengan waktu query oranan ratusan mikrodetik vs brute force yang jauh lebih lambat |

> Catatan lingkungan: Python 3.10 + faiss-cpu 1.15.1 + annoy 1.17.3 + hnswlib 0.8.0. Seed `np.random.seed(42)`/`RandomState(42)` dipasang agar hasil dapat direproduksi; **waktu (build/query) tetap bervariasi antar mesin**.
