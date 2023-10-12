# Tugas 2 PSO
Terdapat dua tugas, yaitu tugas utama dan tugas tambahan yang diberikan oleh Pak Dhani ketika di kelas. 

## Tugas Utama
Tugas utama merupakan mengimplementasikan konvolusi dari dua sinyal 1 dimensi dengan ketentuan hanya menggunakan bahasa Python dasar dan tidak boleh menggunakan library apapun kecuali numpy untuk memvalidasi hasil konvolusi.
Berikut kode Python-nya:
```py
import numpy as np
def convolve(x, y):
   
    if not isinstance(x, list) or not isinstance(y, list):
        raise ValueError("Sinyal harus 1 dimensi.")

    n = len(x) + len(y) - 1

    z = [0] * n

    for i in range(n):
        for j in range(len(x)):
            if i - j >= 0 and i - j < len(y):
                z[i] += x[j] * y[i - j]

    return z

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = convolve(x, y)
z_numpy = np.convolve(x, y)

assert np.allclose(z, z_numpy)

print("Nama : Alfa Naufal Afif Lintang Madani")
print("NRP : 5009211062")
```
### Penjelasan 
- Pertama, program mengimpor modul numpy untuk melakukan operasi matematika dan pemrosesan array.
- Kedua, program mendefinisikan sebuah fungsi bernama convolve yang menerima dua parameter x dan y, yang merupakan dua sinyal 1 dimensi berupa list.
- Ketiga, fungsi tersebut melakukan beberapa hal:
    + Fungsi tersebut memeriksa apakah parameter x dan y adalah list. Jika tidak, fungsi tersebut akan mengeluarkan ValueError dengan pesan “Sinyal harus 1 dimensi.”
    + Fungsi tersebut menghitung panjang dari sinyal hasil konvolusi, yaitu n = len(x) + len(y) - 1.
    + Fungsi tersebut membuat sebuah list kosong berisi nol sepanjang n, yang akan diisi dengan nilai-nilai konvolusi.
    + Fungsi tersebut menggunakan loop bersarang untuk menggeser salah satu sinyal di atas yang lain dan menghitung jumlah produk pada setiap posisi.
    + Fungsi tersebut mengembalikan list yang berisi nilai-nilai konvolusi sebagai hasilnya.
- Keempat, program mendefinisikan dua sinyal 1 dimensi sebagai contoh, yaitu x = [1, 2, 3, 4, 5] dan y = [6, 7, 8, 9, 10].
- Kelima, program mencetak sinyal-sinyal tersebut.
- Keenam, program menghitung dan mencetak konvolusi antara x dan y menggunakan fungsi yang telah didefinisikan, yaitu z = convolve(x, y).
- Ketujuh, program menghitung dan mencetak konvolusi antara x dan y menggunakan fungsi bawaan dari modul numpy, yaitu z_numpy = np.convolve(x, y).
- Kedelapan, program memeriksa apakah hasil konvolusi dari kedua fungsi tersebut sama dengan menggunakan fungsi np.allclose(z, z_numpy). Jika sama, program akan mencetak “True”, jika tidak sama, program akan mencetak “False”.

### Screenshot
