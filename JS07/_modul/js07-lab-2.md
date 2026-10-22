> For the complete documentation index, see [llms.txt](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-mah/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-mah/js07-klasterisasi/lab-2.md).

# Lab 2

Bagaimana jika data non-linear?

## Pengantar

Pada pratikum sebelumnya kita telah mengetahui proses klasterisasi dengan menggunakan metode KMeans. Kebetulan, data yang digunakan dapat dengan mudah dipisahkan secara linear. Bagaimana jika data tidak dalam bentuk sebaran yang dapat dipisahkan secara linier (setidaknya pada visualisasi 2 dimensi)?

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FUSfocuYIpZBW023IfGuu%2Fimage.png?alt=media&amp;token=ea5e8802-c705-4331-b546-a23588eb03ae" alt="" width="563"><figcaption><p>Originaly from GeeksforGeeks</p></figcaption></figure>

KMeans tidak dapat melakukan tugas ini dengan baik. Oleh karena itu, pada praktikum ini, kita akan menggunakan algoritma DBSCAN untuk melakukan klasterisasi pada data non-linear.

## Langkah 0 - Import Library

Import library yang dibutuhkan

{% code lineNumbers="true" %}

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
```

{% endcode %}

## Langkah 1 - Membuat Dataset Sintentis

Kali ini kita akan membuat data sintentis untuk tujuan pembelajaran. Data yang akan kita buat akan berbentuk spiral untuk menyimulasikan kondisi non linear.

{% code lineNumbers="true" %}

```python
from sklearn.datasets import make_moons

X, y = make_moons(200, noise=.05, random_state=0)
```

{% endcode %}

Lakukan proses plotting data untuk mengetahui hasil dataset yang telah dibuat.

{% code lineNumbers="true" %}

```python
plt.scatter(X[:, 0], X[:, 1])
```

{% endcode %}

Maka Anda akan mendapatkan hasil,

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FETgNqyLICFekcts30HUd%2Fimage.png?alt=media&amp;token=40a324ee-6bc0-48ec-b815-50e8c43f64e6" alt="" width="425"><figcaption></figcaption></figure>

Jika diamati secara visual, terdapat dua cluster di dalam dataset. Namun apakah KMeans dapat bekerja dengan baiki dalam kasus ini, mari kita buktikan.

## Langkah 2 - Klasterisasi dengan K-Means

Buat model KMeans dan lakukan plotting ulang hasil klasterisasi

{% code lineNumbers="true" %}

```python
from sklearn.cluster import KMeans

kmeans = KMeans(2, random_state=0)
cluster = kmeans.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=cluster, s=50, cmap='viridis')
```

{% endcode %}

Anda akan mendapatkan hasil seperti,

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FtJKX0mKdhnTe2uNT8TdW%2Fimage.png?alt=media&amp;token=aca21c0f-0495-4ed7-9498-87e0988c1987" alt="" width="425"><figcaption></figcaption></figure>

Terdapat beberapa data yang tidak terklasterisasi secara tepat. Anda dapat dengan mudah membayangkan garis imager linear yang digunakan untuk memisahkan 2 *cluster* data. Lakukan evaluasi lebih lanjut dengan menggunakan *silhouette coefficient*.

{% code lineNumbers="true" %}

```python
from sklearn.metrics import silhouette_score

print(silhouette_score(X, cluster))
```

{% endcode %}

Anda akan mendapatkan nilai berkisar,

```
0.49215648268306905
```

Nilai ini menunjukkan bahwa data tidak terklasterisasi dengan cukup baik.

## Langkah 3 - Klasterisasi dengan DBSCAN

Selanjutnya, kita akan melakukan klasterisasi dengan DBSCAN. ***Ingat, DBSCAN sangat sensitif terhadap parameter epsilon dan minimal sampel!***

{% code lineNumbers="true" %}

```python
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.3, min_samples=2)
cluster_db = dbscan.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=cluster_db, s=50, cmap='viridis')
```

{% endcode %}

Hasilnya adalah,

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2F7jWYV9W8mpVvFqYckMRo%2Fimage.png?alt=media&amp;token=49640c5a-b677-4715-bce9-9c3ef0ba225c" alt="" width="425"><figcaption></figcaption></figure>

Berdasarkan scatterplot, data dapat terklasterisasi dengan sangat baik. Untuk memastikannya, kita perlu melakukan evaluasi kembali dengan *silhouette score*.

{% code lineNumbers="true" %}

```python
from sklearn.metrics import silhouette_score

print(silhouette_score(X, cluster_db))

# Hasil 0.32585318950197517
```

{% endcode %}

Hasil silhouette score menunjukkan hasil yang tidak optimal. Padahal cluster terbentuk dengan baik secara visual. Mengapa demikian? Silhouette coefficient berasumsi cluster dapat terpisah dengan baik dalam bentuk linier, sehingga jika bentuknya distribusi data acak, evaluasi silhouette coefficient tidak dapat bekerja dengan baik. Lalu evaluasi apa yang bisa kita lakukan? Secara sederhana,

1. Prosentase data noise
2. Inspeksi visual

Secara metric dapat menggunakan,

1. Davies-Bouldin Index (DBI) --> **fokus pada separasi indeks, semakin kecil semakin baik, rentang 0 hingga tak hingga.**

{% code lineNumbers="true" %}

```python
from sklearn.metrics import davies_bouldin_score

# Compute and print Davies-Bouldin Index
db = davies_bouldin_score(X, cluster_db)

print(f"Davies-Bouldin Index: {db}")

# Hasilnya
# Davies-Bouldin Index: 1.1622685374061352
```

{% endcode %}
