import numpy as np
# intinya dalam broadcasting jika ingin mengoperasi array 
# dengan ukuran yang beda ,maka ukuran array yang lebih kecil akan 
# disesuaikan dengan array yang lebih besar lalu kedua array bisa dioperasikan

"""
1.Kalau mau operasi antar array yang ukurannya beda,
2.array yang lebih kecil “diperluas” (di-broadcast) supaya nyamain array yang lebih besar,
3.SELAMA masih memenuhi aturan broadcasting NumPy.

"""
"""
1️/Maksud “dibandingkan dari kanan ke kiri” itu apa?

Shape itu kayak ini:

(4, 3)


Artinya:

kiri → dimensi besar (baris)

kanan → dimensi kecil (kolom)

👉 Broadcasting ngecek mulai dari yang PALING KANAN dulu
"""

"""
aturan utama broadcasting:
1.ukurannya sama
2.salah satunya 1
"""

"""
A.shape = (2, 3, 4)
B.shape = (1, 4)
------------
samain dulu
------------
A: (2, 3, 4)
B:    (1, 4)

Cek dari kanan:

4 vs 4 → ✅

3 vs 1 → ✅

2 vs (anggap 1) → ✅

🔥 Aman → bisa broadcasting
"""


array1 = np.array([1,2,3,])
array2 = np.array([10])
print(array1.shape) #dimensi 3
print(array2.shape) #dimensi 1
print(array1+array2)


array3 = np.array([[1,2,3,4]])
array4 = np.array([[1],[2],[3],[4]])
print(array3.shape) #dimensi (1,4)
print(array4.shape) #dimensi (4,1)
print(array3*array4)