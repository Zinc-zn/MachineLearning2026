> For the complete documentation index, see [llms.txt](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-mah/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-mah/js07-klasterisasi/lab-3.md).

# Lab 3

Klasterisasi Pada Kompresi Citr

## Pengantar

Klasterisasi tidak hanya dapat digunakan pada data tabular. Pada konteks citra, kita dapat menggunakan klasterisasi untuk mengidentifkasi kesamaan warna dari sebuah citra sehingga kita mendapatkan area-area tertentu untuk identifikasi lebih lanjut. Kasus lainnya adalah kompresi warna citra. Pada kompresi warna citra, kita akan meminimalkan penggunaan rentang citra untuk mendapatkan citra dengan ukuran data yang lebih rendah.

## Langkah 0 - Import Library

{% code lineNumbers="true" %}

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
```

{% endcode %}

## Langkah 1 - Load Data Citra

Kita akan mencoba menggunakan 1 data citra dari dataset yang telah disediakan

{% code lineNumbers="true" %}

```python
from sklearn.datasets import load_sample_image
flower = load_sample_image("flower.jpg")
ax = plt.axes(xticks=[], yticks=[])
ax.imshow(flower)
```

{% endcode %}

Hasilnya adalah,

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FX4qwmQ2Ke6PPOHLTOs7A%2Fimage.png?alt=media&amp;token=8e40253b-d913-4d1a-945c-003b067d9a81" alt=""><figcaption></figcaption></figure>

## Langkah 2 - Preprocessing

Selanjutnya kita akan melakukan pengecekan ukuran citra dan normalisasi warna

{% code lineNumbers="true" %}

```python
# Check shape
print(flower.shape)

# Normalize color
data = flower / 255.0

# Reshape
data = data.reshape(427 * 640, 3) # turn to 1D

print(data.shape)
```

{% endcode %}

## Langkah 3 - Cek Sebaran Warna

Buat fungsi berikut,

{% code lineNumbers="true" %}

```python
def plot_pixels(data, title, colors=None, N=10000):
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

    fig.suptitle(title, size=20);
```

{% endcode %}

Panggil fungsi untuk mengetahui sebaran warna,

{% code lineNumbers="true" %}

```python
plot_pixels(data, title='Input color space: 16 million possible colors')
```

{% endcode %}

Akan muncul grafik seperti di bawah ini,

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FKKGXmgsvEKhD7vLmXmJV%2Fimage.png?alt=media&amp;token=7ec1a41c-306c-4c8b-9e48-c863661fa641" alt="" width="563"><figcaption></figcaption></figure>

## Langkah 4 - Klasterisasi Warna

Pada tahap ini kita akan melakukan klasterisasi hanya dengan 16 warna saja.

{% code lineNumbers="true" %}

```python
from sklearn.cluster import MiniBatchKMeans

kmeans = MiniBatchKMeans(16)
kmeans.fit(data)
new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

plot_pixels(data, colors=new_colors,title="Reduced color space: 16 colors")
```

{% endcode %}

Didapatkan,

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FtbGPQ7LEuPBHWvIczhuU%2Fimage.png?alt=media&amp;token=734cbca2-3c1e-46c2-a614-969757fd6d3d" alt="" width="563"><figcaption></figcaption></figure>

Hasil perbandingan warna citra sebelum dan setelah kompresi adalah sebagai berikut,

{% code lineNumbers="true" %}

```python
flower_recolored = new_colors.reshape(flower.shape)

fig, ax = plt.subplots(1, 2, figsize=(16, 6),
                       subplot_kw=dict(xticks=[], yticks=[]))
fig.subplots_adjust(wspace=0.05)
ax[0].imshow(flower)
ax[0].set_title('Original Image', size=16)
ax[1].imshow(flower_recolored)
ax[1].set_title('16-color Image', size=16);
```

{% endcode %}

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FUL4FCAACsTfGEHlx42jl%2Fimage.png?alt=media&amp;token=eec3bb4a-f8bd-4397-83dd-c466f2205ce4" alt="" width="563"><figcaption></figcaption></figure>
