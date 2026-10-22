> For the complete documentation index, see [llms.txt](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-mah/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-mah/js07-klasterisasi/k-means.md).

# K-Means

## Apa itu K-Means?

Salah satu metode *unsupervised learning* yang digunakan untuk masalah klasterisasi adalah K-means. *Unsupervised learning* menggunakan kumpulan data dengan label atau kelas yang tidak diketahui. Tujuan *unsupervised learning* adalah untuk menemukan pola data berdasarkan kemiripan data. Gambar 1. menunjukkan ilustrasi kelompok (cluster) yang dibentuk dengan menggunakan algoritma KMeans.

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FlJG0CxIFC8DmQlYSM39C%2Fimage.png?alt=media&amp;token=106262c1-f015-464c-b1ae-62b8c78a0552" alt="" width="375"><figcaption><p>Gambar 1. Hasil pengelompokan data dengan KMeans</p></figcaption></figure>

Simbol $$k$$ pada algoritma K-Means menandakan jumlah kelompok atau *cluster* yang digunakan. *Cluster* mengacu pada kumpulan titik data yang dikumpulkan bersama karena kesamaan tertentu. Jika $$k=2$$, maka akan ada 2 *cluster*, dan jika $$k=3$$ maka terdapat 3 *cluster*, dan seterusnya.

Algoritma K-Means mengambil dataset yang tidak berlabel sebagai input, kemudian membagi dataset menjadi sejumlah $$k$$ *cluster*, dan mengulangi proses tersebut sampai tidak menemukan *cluster* terbaik. Nilai $$k$$ harus ditentukan sebelumnya dalam algoritma ini.

Algoritma K-Means melakukan dua tugas utama, yaitu,

1. Menentukan nilai terbaik untuk titik pusat atau ***centroid*** dengan proses iteratif (perulangan).
2. Menetapkan setiap titik data ke centroid terdekat. Titik-titik data yang dekat dengan centroid tertentu akan menjadi data dalam satu kelompok atau *cluster*.

Proses ini akan dilakukan secara berulang hingga data di dalam satu kelompok tidak lagi berubah (stabil) atau sudah melewati batas iterasi tertentu yang ditentukan diawal. Oleh karena itu setiap cluster memiliki titik data dengan beberapa kesamaan, dan cukup jauh dari cluster lainnya. Gambar 2 menunjukkan ilustrasi cara kerja K-Means.

<figure><img src="https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin/~gitbook/image?url=https%3A%2F%2F1473714265-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fhh7WzzoZbeFX9VC0bZSU%252Fuploads%252F0Y0LeBoA8LTXkJpq3fgS%252FGambar%25207.2%2520k-means-clustering-algorithm-in-machine-learning.png%3Falt%3Dmedia%26token%3Dc5d80432-33b9-4436-a0c8-f69ee1a6322b&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=57eb3eb4&#x26;sv=2" alt=""><figcaption><p>Gambar 2. Proses klasterisasi dengan KMeans</p></figcaption></figure>

Anda dapat melihat video dari Josh Starmer.

{% embed url="<https://www.youtube.com/watch?v=4b5d3muPQmA>" %}

*Centroid* digunakan untuk mewakili titik pusat *cluster* dalam K-Means. Pada iterasi pertama, *centroid* dipilih secara acak dari sekumpulan $$k$$ *centroid*. Nilai $$k$$, harus berupa bilangan bulat positif kurang dari jumlah *instance* atau data. Terkadang, konteks masalah yang akan diselesaikan dengan algoritma *clustering* memengaruhi jumlah *cluster*.

> Sebagai contoh, managemen toko retail telah mendefinisikan konsumen ke dalam 4 jenis, yaitu, Platinum, Gold, Silver, dan Bronze. Dikarenakan kelompok sudah ditentukan, maka nilai $$k=4$$.

Setelah iterasi pertama, titik *centroid* ditentukan ulang dengan cara mencari nilai rata-rata jarak antara titik-titik data yang ditunjuk sebagai anggota *cluster* dengan titik *centroid*. Selain itu, akan ditentukan seberapa dekat data tambahan ke *centroid* menyerupai *centroid*. Algoritma K- Means kemudian memilih data dengan kemiripan terbaik antara *centroid* dan *non-centroid* untuk menentukan anggota *cluster*.&#x20;

*Euclidean distance* merupakan salah satu cara untuk menghitung jarak pada algoritma K-Means. Perhitungan jarak dapat dimodifikasi agar sesuai dengan situasi. Selanjutnya, metode *cosine similarity* dapat digunakan saat melakukan pengelompokan data.&#x20;

## Menentukan Nilai $$k$$

Meskipun kita dapat menentukan jumlah *cluster* ( $$k$$ ) diawal sebelum melakukan proses klasterisasi, terkadang kita juga belum mengetahui atau menentukan jumlah cluster dalam sebuah data. Kondisi biasanya terjadi ketika kita ingin melakukan kajian awal terkait dengan kelompok-kelompok data yang mungkin ada di dalam dataset. ***Elbow method*** adalah metode yang populer untuk menentukan nilai $$k$$ yang ideal. Elbow method bekerja dengan memonitoring nilai evaluasi performa dari setiap nilai $$k$$ dalam pembentukan cluster. **Performa model klasterisasi dapat diukur dengan menggunakan metode&#x20;*****sum of square root*****&#x20;(SSE)**. Metode-metode yang didapat digunakan untuk mengetahui performa model dikenal juga sebagai *cost function* (fungsi biaya). Gambar 3 merupakan ilustrasi penentuan nilai $$k$$ menggunakan *elbow method*.

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FLKlsJ9xleZlZYVbadpGU%2Fimage.png?alt=media&amp;token=40db1d33-b491-41c6-86d7-e47d1226757e" alt=""><figcaption><p>Gambar 3. Penentuan nilai k dengan <em>elbow method</em></p></figcaption></figure>

Sumbu $$y$$ merupakan nilai inersia atau nilai *cost function,* dalam konteks ini menggunakan SSE. Semakin tinggi nilai inersia semakin buruk performa model klasterisasi pada jumlah cluster $$k$$. Sumbu $$x$$ menunjukkan jumlah *cluster* yang digunakan. **Jumlah&#x20;*****cluster*****&#x20;terbaik ditunjukkan pada posisi "siku" yang menunjukkan titik awal performa yang stabil.** Untuk mengetahui daerah "siku" kita perlu melakukan pengamatan terhadap nilai SSE. Sebagai contoh pada Gambar 3, nilai $$k=3$$ mulai menunjukkan penurunan yang cukup signifikan dibandingkan dengan $$k=2$$. Selanjutnya, jika diamati nilai SSE pada $$k=5$$ hingga 8, penurunan nilai SSE cenderung lebih stabil setiap penambahan jumlah *cluster*. Penurunan tajam terakhir yang terjadi adalah pada $$k=4$$. Sehingga, jumlah cluster yang ideal pada kasus ini adalah 4.

NB: **Ingat, nilai SSE yang kecil tidak menggambarkan performa yang ideal pada KMeans!**

## Proses Algoritma K-Means

Proses langkah per langkah algoritma K-Means dapat dipelajari pada tautan [berikut](https://docs.google.com/spreadsheets/d/16C2HxTFicQ5tS7aXc1Uvlu1kyvk20LSA_P-E2p47kLY/edit?usp=sharing).

## Evaluasi dengan Silhouette Coefficient

Meskipun *elbow method* dapat dengan cepat dan mudah dalam menentukan jumlah *cluster*, metode ini terkesan kasar menurut Aurélien Géron, pada bukunya yang berjudul Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow. Hal ini dikarenakan *elbow method* menggunakan SSE yang berfokus kepada ***intra cluster***. Artinya, SSE hanya melakukan evaluasi terhadap anggota didalam *cluster*. Evaluasi yang lebih presisi dapat dilakukan dengan menggunakan metode **silhouette coefficient**. Keunggulan utama silhouette coefficient adalah, kalkulasi performa cluster di hitung dengan **mempertimbangkan&#x20;*****intra*****&#x20;dan&#x20;*****inter cluster***. Perhatikan Gambar 4.

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FtWVTZm1BfcXSqg8NZf7m%2Fimage.png?alt=media&amp;token=d380d1a3-fb3d-4cc3-b240-62d9f77d645f" alt="" width="534"><figcaption><p>Gambar 4. Ilustrasi proses evaluasi silhoutte coefficient<br>(<a href="https://medium.com/@ashutoshb418?source=post_page---byline--e976bb81d10c---------------------------------------">Ashutosh Bhardwaj</a> via <a href="mailto:undefined">Medium</a>)</p></figcaption></figure>

Nilai *silhouette coefficient* dihitung dengan menggunakan persamaan,

$$
s(i) = \frac{b(i)-a(i)}{max(a(i),b(i))}
$$

Dimana,

* $$a$$ adalah jarak rata-rata titik $$i$$  dengan titik yang lain dalam cluster (*intra cluster*)&#x20;
* $$b$$ adalah jarak rata-rata titik $$i$$ dengan titik yang lain dengan cluster terdekat (*inter cluster*)&#x20;
* $$s(i)$$ adalah *silhouette score* untuk titik $$i$$

Selanjutnya, untuk mengetahui kualitas dari cluster, rentang *silhouette score* yang menjadi acuan adalah,

* $$+1$$ merupakan nilai yang terbaik karena setiap data terhubung dengan cluster yang tepat.
* $$0$$ merupakan nilai yang menggambarkan terdapat titik dengan jarak yang sama dengan titik intra dan inter cluster (*borderline cluster*).
* $$-1$$ merupakan nilai yang dihindari karena menggambarkan titik memiliki jarak yang lebih dekat dengan cluster lain dibanding dengan titik di dalam cluster.

Contoh proses *silhouette coefficient* dapat dipelajari pada tautan berikut.

Kita juga dapat melakukan visualisasi terhadap nilai *silhouette score* untuk proses analisis lebih lanjut. Visualisasi dilakukan dengan menggunakan silhouette diagram / silhouette plot seperti pada Gambar 5.

<figure><img src="https://1812311909-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYHOv2XH8FJMJSMsnhwNa%2Fuploads%2FJVMLYgnYja4GvBs7gkBZ%2Fimage.png?alt=media&amp;token=d6c3f725-3a63-421b-9d33-391ec2f9a0da" alt="" width="563"><figcaption><p>Gambar 5. Ilustrasi silhouette plot</p></figcaption></figure>

Silhouette plot memperlihatkan nilai nilai *silhouette score* pada intra cluster dan intercluster yang diurutkan dari nilai terbesar hingga terkecil. Garis vertikal merah menunjukkan nilai score secara rata-rata keseluruhan. Semakin mendekati $$+1$$ semakin baik. **Anda dapat menggunakan visualisasi ini untuk menilai jumlah&#x20;*****cluster*****&#x20;yang terbaik**.
