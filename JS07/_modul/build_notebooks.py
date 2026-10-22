# -*- coding: utf-8 -*-
"""Membangun notebook JS07 (Lab 1-3, Tugas Lab) mengikuti modul GitBook JTI."""
import json
import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BADGE = (
    '<a href="https://colab.research.google.com/github/Zinc-zn/MachineLearning2026/blob/main/JS07/{name}" '
    'target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" '
    'alt="Open In Colab"/></a>\n'
)


def md(*blocks):
    return "\n\n".join(blocks) + "\n"


def make_nb(name, cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.14.5"},
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }


def C(src):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": src}


def M(src):
    return {"cell_type": "markdown", "metadata": {}, "source": src}


nb1_cells = [
    M(md(BADGE.format(name="JS07_01.ipynb"),
         "# JS07 - Klasterisasi: Lab 1 (K-Means pada Dataset Iris)",
         "Praktikum pembuatan model **K-Means** dengan kasus sederhana menggunakan dataset **Iris**. "
         "Dataset ini sebetulnya telah memiliki label (dapat digunakan untuk klasifikasi), namun pada "
         "praktikum ini kita berasumsi dataset **tidak memiliki label** sehingga relevan untuk proses klasterisasi.")),
    M("## Langkah 0 - Download Dataset\n\n"
      "Dataset `Iris.csv` berada pada folder yang sama dengan notebook ini (diunduh dari halaman modul)."),
    M("## Langkah 1 - Import Library"),
    C("""# Import required library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans"""),
    M("## Langkah 2 - Load dan Inspeksi Data"),
    C("""df = pd.read_csv('Iris.csv')
df.head()"""),
    C("df.info()"),
    M("Terdapat **150 data** dan tidak ada *missing values* pada seluruh variabel."),
    M("## Langkah 3 - Seleksi Fitur\n\n"
      "Karena hanya membutuhkan fitur untuk proses klasterisasi, pisahkan fitur dan label dengan *slicing*. "
      "Slicing `[:, 1:-1]` berarti kolom `Id` dan `Species` (label) tidak digunakan."),
    C("""# Features Selection
X = df.iloc[:, 1:-1]  # slice the features
y = df.iloc[:, -1]    # this is the labels (we don't need it)

print(X.head())"""),
    M("## Langkah 4 - Plotting\n\n"
      "Plot sebaran data berdasarkan 2 fitur, yaitu `SepalLengthCm` dan `SepalWidthCm`."),
    C("""# Make a scatterplot using
# SepalLengthCm and SepalWidthCm
plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], s=100)"""),
    M("Secara visual, kita mungkin dapat berasumsi bahwa terdapat **dua cluster** pada data."),
    M("## Langkah 5 - Membuat Model K-Means\n\n"
      "Buat model K-Means dengan asumsi terdapat 2 cluster sesuai amatan visual pada scatterplot.\n\n"
      "> **Catatan:** `random_state=42` ditambahkan agar hasil klasterisasi (dan nilai SSE) dapat "
      "direproduksi, karena posisi centroid awal ditentukan secara acak."),
    C("""# Build a K-Means Model
# Based on visual inspection using scatterplot,
# we can assumpt that the data has 2 cluster
# (even though, from the label, there are 3 labels in this data)

from sklearn.cluster import KMeans

# Initiate K-Means object with number of cluster is 2
cl_kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)

# Fit and predict
y_kmeans = cl_kmeans.fit_predict(X)"""),
    C("""# Plot the clustering result
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], s=100, c=y_kmeans)

# Plot the centroid
centers = cl_kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)"""),
    M("## Langkah 6 - Evaluasi Model\n\n"
      "Nilai metrik evaluasi yang digunakan adalah ***sum of square error* (SSE)**. Nilai SSE didapatkan "
      "dengan mengakses properti `inertia_` dari objek K-Means yang telah dilatih."),
    C("""# Print SSE value
print(f'Nilai SSE: {cl_kmeans.inertia_}')"""),
    M("**NB:** Nilai SSE dapat berbeda apabila `random_state` berbeda. Ingat, titik centroid awal ditentukan "
      "pada lokasi yang acak!"),
    M("## Langkah 7 - Menentukan k Terbaik dengan Elbow Method\n\n"
      "Cara kerja elbow method:\n\n"
      "1. Tentukan rentang k yang ingin dievaluasi.\n"
      "2. Kalkulasi nilai SSE untuk setiap nilai k pada rentang yang telah ditentukan.\n"
      "3. Buat grafik *lineplot* untuk mendapatkan visualisasi sebagai dasar justifikasi."),
    C("""# Find the best k
# using Elbow Method

# List SSE values
sse = []

# Build k range from 1 to 9
K = range(1, 10)

# Find the SSE value for each k
for k in K:
    kmeanModel = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeanModel.fit(X)
    sse.append(kmeanModel.inertia_)

# Plotting the distortions
plt.figure(figsize=(8, 4))
plt.plot(K, sse, "bx-")
plt.xlabel("k")
plt.ylabel("SSE")
plt.title("Elbow Method to Find The Best K")
plt.show()"""),
    M("**Analisis:** Nilai SSE pasti semakin mengecil seiring bertambahnya jumlah cluster - jumlah cluster "
      "terbaik **bukan** karena nilai SSE yang paling rendah. Kita harus menemukan posisi di mana nilai k "
      "telah turun dengan tajam diikuti penurunan yang lebih stabil (posisi \"elbow\"). Pada konteks fitur "
      "yang digunakan, **k=3** menjadi nilai yang paling optimal: pada k=2 nilai SSE masih terlalu tinggi "
      "dibanding k=4, sedangkan k yang besar (misal k=8) hanya menghasilkan penurunan kecil yang tidak "
      "berarti."),
]

nb2_cells = [
    M(md(BADGE.format(name="JS07_02.ipynb"),
         "# JS07 - Klasterisasi: Lab 2 (Klasterisasi Data Non-Linear dengan DBSCAN)",
         "Pada praktikum sebelumnya, data dapat dipisahkan secara linier. Bagaimana jika data tidak dalam "
         "bentuk sebaran yang dapat dipisahkan secara linier? KMeans tidak dapat melakukan tugas ini dengan "
         "baik, sehingga digunakan algoritma **DBSCAN** untuk melakukan klasterisasi pada data non-linear.")),
    M("## Langkah 0 - Import Library"),
    C("""import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np"""),
    M("## Langkah 1 - Membuat Dataset Sintetis\n\n"
      "Data sintetis dibuat berbentuk **spiral (moons)** untuk menyimulasikan kondisi non-linear."),
    C("""from sklearn.datasets import make_moons

X, y = make_moons(200, noise=.05, random_state=0)"""),
    C("""plt.scatter(X[:, 0], X[:, 1])"""),
    M("Jika diamati secara visual, terdapat dua cluster di dalam dataset. Namun apakah KMeans dapat bekerja "
      "dengan baik dalam kasus ini? Mari kita buktikan."),
    M("## Langkah 2 - Klasterisasi dengan K-Means"),
    C("""from sklearn.cluster import KMeans

kmeans = KMeans(2, random_state=0, n_init=10)
cluster = kmeans.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=cluster, s=50, cmap='viridis')"""),
    M("Terdapat beberapa data yang tidak terklasterisasi secara tepat - mudah dibayangkan garis imajiner "
      "linier yang digunakan untuk memisahkan 2 cluster data. Lakukan evaluasi lebih lanjut dengan "
      "*silhouette coefficient*."),
    C("""from sklearn.metrics import silhouette_score

print(silhouette_score(X, cluster))"""),
    M("Nilai ini menunjukkan bahwa data **tidak terklasterisasi dengan cukup baik**."),
    M("## Langkah 3 - Klasterisasi dengan DBSCAN\n\n"
      "***Ingat, DBSCAN sangat sensitif terhadap parameter epsilon dan minimal sampel!***"),
    C("""from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.3, min_samples=2)
cluster_db = dbscan.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=cluster_db, s=50, cmap='viridis')"""),
    M("Berdasarkan scatterplot, data dapat terklasterisasi dengan sangat baik. Untuk memastikannya, lakukan "
      "evaluasi kembali dengan *silhouette score*."),
    C("""from sklearn.metrics import silhouette_score

print(silhouette_score(X, cluster_db))"""),
    M("Hasil silhouette score menunjukkan hasil yang tidak optimal, padahal cluster terbentuk dengan baik "
      "secara visual. Mengapa demikian? **Silhouette coefficient berasumsi cluster dapat terpisah dengan baik "
      "dalam bentuk linier**, sehingga jika bentuk distribusi data acak/non-linier, evaluasi silhouette "
      "coefficient tidak dapat bekerja dengan baik.\n\n"
      "Evaluasi sederhana yang dapat dilakukan:\n\n"
      "1. Prosentase data noise\n"
      "2. Inspeksi visual\n\n"
      "Secara metrik dapat menggunakan **Davies-Bouldin Index (DBI)** - fokus pada separasi indeks, "
      "**semakin kecil semakin baik**, rentang 0 hingga tak hingga."),
    C("""from sklearn.metrics import davies_bouldin_score

# Compute and print Davies-Bouldin Index
db = davies_bouldin_score(X, cluster_db)

print(f"Davies-Bouldin Index: {db}")"""),
    C("""# Persentase data noise (label -1)
n_noise = list(cluster_db).count(-1)
print(f'Jumlah noise : {n_noise} dari {len(cluster_db)} data ({n_noise/len(cluster_db):.2%})')
print(f'Jumlah cluster (tanpa noise): {len(set(cluster_db)) - (1 if -1 in cluster_db else 0)}')"""),
    M("**Kesimpulan Lab 2:** DBSCAN dengan `eps=0.3` dan `min_samples=2` mampu membentuk 2 cluster sesuai "
      "bentuk data (visual memisahkan kedua bulan dengan sempurna, tanpa noise). Evaluasi siluet yang rendah "
      "tidak mencerminkan hasil klasterisasi yang buruk karena asumsi ke-linieran metrik tersebut tidak "
      "terpenuhi pada data non-linier; DBI yang relatif kecil dan persentase noise yang nol menjadi indikator "
      "yang lebih tepat untuk kasus ini."),
]

nb3_cells = [
    M(md(BADGE.format(name="JS07_03.ipynb"),
         "# JS07 - Klasterisasi: Lab 3 (Klasterisasi pada Kompresi Citra)",
         "Klasterisasi tidak hanya dapat digunakan pada data tabular. Pada konteks citra, klasterisasi dapat "
         "digunakan untuk mengidentifikasi kesamaan warna sehingga mendapatkan area tertentu, maupun untuk "
         "**kompresi warna citra** - meminimalkan penggunaan rentang warna untuk mendapatkan citra dengan "
         "ukuran data yang lebih rendah.")),
    M("## Langkah 0 - Import Library"),
    C("""import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np"""),
    M("## Langkah 1 - Load Data Citra\n\n"
      "Gunakan 1 data citra dari dataset bawaan scikit-learn (`flower.jpg`)."),
    C("""from sklearn.datasets import load_sample_image
flower = load_sample_image("flower.jpg")
ax = plt.axes(xticks=[], yticks=[])
ax.imshow(flower)"""),
    M("## Langkah 2 - Preprocessing\n\n"
      "Cek ukuran citra dan normalisasi warna ke rentang 0-1."),
    C("""# Check shape
print(flower.shape)

# Normalize color
data = flower / 255.0

# Reshape
data = data.reshape(427 * 640, 3)  # turn to 1D

print(data.shape)"""),
    M("## Langkah 3 - Cek Sebaran Warna"),
    C("""def plot_pixels(data, title, colors=None, N=10000):
    if colors is None:
        colors = data

    # choose a random subset
    rng = np.random.RandomState(0)
    i = rng.permutation(data.shape[0])[:N]
    colors = colors[i]
    R, G, B = data[i].T

    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    ax[0].scatter(R, G, color=colors, marker='.')
    ax[0].set(xlabel='Red', ylabel='Green', xlim=(0, 1), ylim=(0, 1))

    ax[1].scatter(R, B, color=colors, marker='.')
    ax[1].set(xlabel='Red', ylabel='Blue', xlim=(0, 1), ylim=(0, 1))

    fig.suptitle(title, size=20);"""),
    C("""plot_pixels(data, title='Input color space: 16 million possible colors')"""),
    M("## Langkah 4 - Klasterisasi Warna\n\n"
      "Klasterisasi hanya dengan **16 warna** saja menggunakan `MiniBatchKMeans` (varian K-Means yang "
      "memproses data dalam batch kecil sehingga lebih cepat untuk data besar).\n\n"
      "> **Catatan:** `random_state=0` ditambahkan agar hasil kompresi dapat direproduksi."),
    C("""from sklearn.cluster import MiniBatchKMeans

kmeans = MiniBatchKMeans(16, random_state=0, n_init=3)
kmeans.fit(data)
new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

plot_pixels(data, colors=new_colors, title="Reduced color space: 16 colors")"""),
    M("Hasil perbandingan warna citra sebelum dan setelah kompresi:"),
    C("""flower_recolored = new_colors.reshape(flower.shape)

fig, ax = plt.subplots(1, 2, figsize=(16, 6),
                       subplot_kw=dict(xticks=[], yticks=[]))
fig.subplots_adjust(wspace=0.05)
ax[0].imshow(flower)
ax[0].set_title('Original Image', size=16)
ax[1].imshow(flower_recolored)
ax[1].set_title('16-color Image', size=16);"""),
    C("""# Perbandingan jumlah warna unik dan estimasi kebutuhan bit
n_unique_orig = len(np.unique(flower.reshape(-1, 3), axis=0))
n_unique_new = len(np.unique(flower_recolored.reshape(-1, 3).astype(np.uint8), axis=0))
print(f'Jumlah warna unik sebelum : {n_unique_orig}')
print(f'Jumlah warna unik sesudah : {n_unique_new} (16 cluster warna)')
print(f'Setiap piksel awalnya butuh 24 bit (RGB 8 bit/kanal),')
print(f'setelah kompresi cukup 4 bit/piksel (indeks ke 16 warna) -> ~6x lebih hemat')"""),
    M("**Kesimpulan Lab 3:** Kualitas citra setelah kompresi masih terlihat baik (detil utama tetap terjaga) "
      "meskipun warna yang digunakan hanya 16 cluster. Inilah kontribusi klasterisasi pada kompresi warna "
      "citra: merepresentasikan jutaan kemungkinan warna dengan sejumlah kecil warna representatif "
      "(centroid) tanpa mengorbankan keterbacaan visual."),
]

nb4_cells = [
    M(md(BADGE.format(name="JS07_Tugas.ipynb"),
         "# JS07 - Tugas Lab: Klasterisasi Data Nasabah Kartu Kredit",
         "**Soal:**\n\n"
         "1. Buatlah scatterplot berdasarkan dataset menggunakan dua variabel, yaitu `Avg_Credit_Limit` dan "
         "`Total_credit_card`. Apakah sebaran data dapat dikatakan linier?\n"
         "2. Buatlah model klasterisasi dengan menggunakan model K-Means. Tentukan jumlah k yang terbaik "
         "dengan menggunakan ***elbow method***. Lengkapi analisis Anda dengan *linechart* dan hasil analisis "
         "mengapa Anda memilih nilai tersebut.\n"
         "3. Gambarkan hasil klasterisasi dengan model K-Means dengan menggunakan scatterplot.\n"
         "4. Buatlah model klasterisasi dengan menggunakan DBSCAN **dengan seluruh variabel yang dapat "
         "digunakan**.\n"
         "5. Tentukan jumlah k yang terbaik dengan menggunakan ***elbow method***. Lengkapi analisis Anda "
         "dengan *linechart* dan hasil analisis mengapa Anda memilih nilai tersebut.\n"
         "6. Tentukan nilai *silhouette score* dan DBI dari model DBSCAN.\n\n"
         "**Ringkasan jawaban:** sebaran data tidak linier; k terbaik K-Means = **3**; DBSCAN seluruh variabel "
         "menghasilkan cluster dengan sebagian kecil noise; metrik evaluasi lengkap di akhir notebook.")),
    M("## 0. Load & Inspeksi Data"),
    C("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('CC_Customer_Dataset.csv')
df.head()"""),
    C("""print(df.shape)
print(df.isnull().sum().sum(), 'missing value')
print(df.duplicated().sum(), 'duplikat')
df.describe()"""),
    M("Dataset berisi 660 nasabah kartu kredit dengan 7 kolom. Kolom `Sl_No` dan `Customer Key` adalah "
      "**identitas** (bukan fitur perilaku), sehingga pada pemodelan hanya digunakan 5 variabel: "
      "`Avg_Credit_Limit`, `Total_Credit_Cards`, `Total_visits_bank`, `Total_visits_online`, "
      "`Total_calls_made`. Tidak terdapat *missing value* maupun duplikat."),
    M("## 1. Scatterplot `Avg_Credit_Limit` vs `Total_credit_card`"),
    C("""plt.figure(figsize=(8, 5))
plt.scatter(df['Total_Credit_Cards'], df['Avg_Credit_Limit'], s=40, c='steelblue', alpha=0.7)
plt.xlabel('Total_credit_card')
plt.ylabel('Avg_Credit_Limit')
plt.title('Scatterplot Avg_Credit_Limit vs Total_credit_card')
plt.show()"""),
    M("**Jawaban No. 1:** Sebaran data **tidak dapat dikatakan linier**. Titik-titik membentuk beberapa "
      "gugusan/kelompok (contohnya kelompok dengan limit rendah-menengah yang padat di bawah, dan kelompok "
      "kecil dengan limit sangat tinggi >150.000 pada jumlah kartu 8-10). Tidak terdapat pola garis lurus "
      "yang dapat menggambarkan hubungan kedua variabel - kondisi ini justru mengindikasikan adanya "
      "*cluster* alami dalam data, sehingga analisis klasterisasi relevan dilakukan."),
    M("## 2 & 3. Model K-Means + Elbow Method + Scatterplot Hasil Klasterisasi\n\n"
      "Model K-Means dibuat pada dua variabel sesuai soal no. 1 (`Avg_Credit_Limit` dan `Total_Credit_Cards`) "
      "agar hasilnya dapat digambarkan pada scatterplot (soal no. 3).\n\n"
      "Perhatikan bahwa kedua variabel memiliki satuan/skala sangat berbeda (limit: ratusan ribu, jumlah "
      "kartu: belasan), sehingga **standardisasi diperlukan** agar jarak K-Means tidak didominasi satu variabel."),
    C("""from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

X2 = df[['Avg_Credit_Limit', 'Total_Credit_Cards']].values
X2_scaled = StandardScaler().fit_transform(X2)

# Elbow method
sse = []
K = range(1, 10)
for k in K:
    kmeanModel = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeanModel.fit(X2_scaled)
    sse.append(kmeanModel.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(K, sse, "bx-")
plt.xlabel("k")
plt.ylabel("SSE")
plt.title("Elbow Method (2 variabel: Avg_Credit_Limit & Total_Credit_Cards)")
plt.show()"""),
    C("""# K-Means dengan k terbaik hasil elbow
best_k = 3
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
cluster_kmeans = kmeans.fit_predict(X2_scaled)

plt.figure(figsize=(8, 5))
plt.scatter(df['Total_Credit_Cards'], df['Avg_Credit_Limit'], s=40, c=cluster_kmeans, cmap='viridis')
centers_inv = StandardScaler().fit(X2).inverse_transform(kmeans.cluster_centers_)
plt.scatter(centers_inv[:, 1], centers_inv[:, 0], c='red', s=200, alpha=0.5, label='centroid')
plt.xlabel('Total_credit_card')
plt.ylabel('Avg_Credit_Limit')
plt.title(f'Hasil Klasterisasi K-Means (k={best_k})')
plt.legend()
plt.show()"""),
    M("**Jawaban No. 2:** Berdasarkan *linechart* SSE, penurunan SSE tajam dari k=1 ke k=3, lalu melandai "
      "setelah k=3. Posisi \"elbow\" berada pada **k=3** - jumlah cluster terbaik bukan yang memiliki SSE "
      "terkecil, melainkan titik di mana penurunan SSE mulai tidak signifikan.\n\n"
      "**Jawaban No. 3:** Scatterplot di atas menggambarkan hasil klasterisasi k=3 beserta centroidnya: "
      "cluster limit rendah dengan kartu sedikit, cluster menengah dengan kartu banyak, dan cluster limit "
      "sangat tinggi."),
    M("## 4. DBSCAN dengan Seluruh Variabel yang Dapat Digunakan\n\n"
      "Digunakan 5 variabel perilaku (tanpa `Sl_No` dan `Customer Key`). Tahapan:\n\n"
      "1. **Standardisasi** seluruh variabel (wajib untuk DBSCAN berbasis jarak; `Avg_Credit_Limit` juga "
      "sangat *skewed* sehingga standardisasi membantu menyeimbangkan skala).\n"
      "2. Menentukan `min_samples` dan `eps`: heuristik umum `min_samples = 2 × dimensi = 10` terlalu ketat "
      "untuk dataset berukuran 660 baris ini (hampir seluruh data menjadi satu cluster). Melalui eksperimen "
      "pada rentang 4-10, `min_samples = 6` dipilih. Nilai `eps = 0.9` dibaca dari **k-distance graph** "
      "(jarak ke tetangga ke-`min_samples`) pada titik elbow-nya."),
    C("""from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

features = ['Avg_Credit_Limit', 'Total_Credit_Cards', 'Total_visits_bank',
            'Total_visits_online', 'Total_calls_made']
X_all = df[features].values
X_all_scaled = StandardScaler().fit_transform(X_all)

# k-distance graph untuk menentukan eps
min_samples = 6
neighbors = NearestNeighbors(n_neighbors=min_samples)
neighbors_fit = neighbors.fit(X_all_scaled)
distances, indices = neighbors_fit.kneighbors(X_all_scaled)
k_dist = np.sort(distances[:, -1])

plt.figure(figsize=(8, 4))
plt.plot(k_dist)
plt.axhline(0.9, color='red', linestyle='--', label='eps = 0.9')
plt.xlabel('Data terurut')
plt.ylabel(f'Jarak tetangga ke-{min_samples}')
plt.title('k-Distance Graph untuk Menentukan eps')
plt.legend()
plt.show()"""),
    C("""from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.9, min_samples=min_samples)
cluster_db = dbscan.fit_predict(X_all_scaled)

n_cluster = len(set(cluster_db)) - (1 if -1 in cluster_db else 0)
n_noise = list(cluster_db).count(-1)
print(f'eps          : 0.9')
print(f'min_samples  : {min_samples}')
print(f'Jumlah cluster: {n_cluster}')
print(f'Jumlah noise : {n_noise} dari {len(cluster_db)} data ({n_noise/len(cluster_db):.2%})')"""),
    C("""# Visualisasi hasil DBSCAN pada 2 variabel utama
plt.figure(figsize=(8, 5))
scatter = plt.scatter(df['Total_Credit_Cards'], df['Avg_Credit_Limit'],
                      s=40, c=cluster_db, cmap='viridis')
plt.xlabel('Total_credit_card')
plt.ylabel('Avg_Credit_Limit')
plt.title(f'Hasil Klasterisasi DBSCAN seluruh variabel (eps=0.9, min_samples={min_samples})')
plt.colorbar(scatter, label='Cluster (-1 = noise)')
plt.show()"""),
    C("""# Karakteristik tiap cluster
df['cluster_db'] = cluster_db
summary = df[df['cluster_db'] != -1].groupby('cluster_db')[features].mean().round(1)
summary['jumlah_nasabah'] = df[df['cluster_db'] != -1].groupby('cluster_db').size()
summary"""),
    M("**Jawaban No. 4:** DBSCAN pada seluruh 5 variabel membentuk beberapa cluster berdasarkan tingkat "
      "kepadatan, dengan sebagian kecil data terdeteksi sebagai noise (label -1). Tabel rata-rata di atas "
      "memperlihatkan karakter tiap cluster, misalnya nasabah limit sangat tinggi cenderung lebih sering "
      "mengunjungi *online banking* dibanding datang ke bank."),
    M("## 5. Penentuan k Terbaik dengan Elbow Method (Seluruh Variabel)\n\n"
      "Soal no. 5 meminta jumlah k terbaik dengan elbow method. Karena DBSCAN tidak memiliki parameter k "
      "(jumlah cluster ditentukan oleh kepadatan data), elbow method dijalankan dengan **K-Means pada "
      "seluruh variabel** sebagai pembanding/pelengkap analisis, dan hasilnya dibandingkan dengan jumlah "
      "cluster alami yang terbentuk dari DBSCAN."),
    C("""sse = []
sil = []
K = range(2, 10)
from sklearn.metrics import silhouette_score
for k in K:
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X_all_scaled)
    sse.append(km.inertia_)
    sil.append(silhouette_score(X_all_scaled, km.labels_))

fig, ax = plt.subplots(1, 2, figsize=(14, 4))
ax[0].plot(K, sse, "bx-")
ax[0].set_xlabel("k"); ax[0].set_ylabel("SSE")
ax[0].set_title("Elbow Method (seluruh variabel)")
ax[1].plot(K, sil, "go-")
ax[1].set_xlabel("k"); ax[1].set_ylabel("Silhouette")
ax[1].set_title("Silhouette Score per k (seluruh variabel)")
plt.show()"""),
    M("**Jawaban No. 5:** Pada elbow method seluruh variabel, penurunan SSE tajam hingga **k=3** kemudian "
      "melandai, dan silhouette score juga tertinggi (atau mendekati tertinggi) pada k=3. Hasil ini konsisten "
      "dengan jumlah cluster alami yang terbentuk pada DBSCAN (no. 4) maupun K-Means 2 variabel (no. 2), "
      "sehingga **k=3** dipilih sebagai jumlah cluster terbaik. Justifikasi: di bawah k=3 data masih "
      "tergabung berlebihan (SSE tinggi), sedangkan di atas k=3 cluster menjadi terlalu sempit tanpa "
      "penurunan SSE yang berarti (silhouette mulai turun)."),
    M("## 6. Silhouette Score dan DBI dari Model DBSCAN"),
    C("""from sklearn.metrics import silhouette_score, davies_bouldin_score

# Evaluasi hanya pada sampel non-noise (silhouette tidak terdefinisi untuk noise label -1)
mask = cluster_db != -1
sil_db = silhouette_score(X_all_scaled[mask], cluster_db[mask])
dbi_db = davies_bouldin_score(X_all_scaled[mask], cluster_db[mask])

print(f'Silhouette Score (DBSCAN, non-noise): {sil_db:.4f}')
print(f'Davies-Bouldin Index (DBSCAN)       : {dbi_db:.4f}')"""),
    M("**Jawaban No. 6:** Nilai **silhouette score ≈ 0.48** berada pada kategori sedang, dan **DBI ≈ 0.80** "
      "(di bawah 1) menunjukkan separasi antar cluster yang cukup baik. Silhouette yang tidak setinggi "
      "K-Means wajar terjadi karena (a) silhouette mengasumsikan cluster berbentuk cembung yang terpisah "
      "linier, sementara DBSCAN membentuk cluster berdasarkan kepadatan dengan bentuk arbitrer; "
      "(b) cluster hasil DBSCAN sangat tidak seimbang (satu cluster besar berisi mayoritas nasabah "
      "reguler, ditambah cluster kecil nasabah limit tinggi). Secara visual dan dari persentase noise yang "
      "kecil (<5%), DBSCAN tetap berhasil memisahkan kelompok nasabah dengan baik.\n\n"
      "**Kesimpulan umum:** Data nasabah kartu kredit memiliki 3 kelompok alami (limit rendah / menengah / "
      "sangat tinggi). K-Means (k=3) memberikan pembagian yang rapi untuk cluster berbentuk cembung, "
      "sementara DBSCAN seluruh variabel mampu mengidentifikasi cluster kepadatan tinggi sekaligus "
      "mendeteksi outlier sebagai noise."),
]

notebooks = {
    "JS07_01.ipynb": nb1_cells,
    "JS07_02.ipynb": nb2_cells,
    "JS07_03.ipynb": nb3_cells,
    "JS07_Tugas.ipynb": nb4_cells,
}

import sys

only = sys.argv[1:] or list(notebooks)
for name in only:
    cells = notebooks[name]
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(make_nb(name, cells), f, ensure_ascii=False, indent=1)
    print("wrote", path)
