import numpy as np
#1.zeros = membuat semua elemen array jadi 0
zeros=np.zeros((2,3))

print(zeros)
#2.ones = membuat semua elemen array jadi 1
ones=np.ones((2,3))

print(ones)
#3.full= membuat array dengan elemen tertentu
full=np.full((2,3),5)

print(full)
#4.eye= membuat matriks identitas 
#diagonal utama = 1 ,sisanya 0
eye=np.eye(3)

print(eye)

#5.empty = array kosong(nilai sampah)
#membuat array tanpa inisialisasi nol
#isinya sampah memori bukan nol
empty = np.empty((2,3))
print(empty)

#6.arange = versi rangenya numpy (start,stop,step)
arange = np.arange(0,10,3)
print(arange)
#7.linspace = membuat jarak yang sama antar angka dari start ke stop
linspace = np.linspace(0,10,6) #angka 5 bukan step tapi banyak titik/data
print(linspace)
