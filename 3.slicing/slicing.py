import numpy as np 
"""Slicing pada NumPy adalah cara mengambil sebagian data dari array
tanpa harus mengambil semuanya."""

"""Ibaratnya:

array itu kue 🎂, slicing itu motong sebagian kue sesuai yang kita mau."""

"""Definisi singkat

Slicing = teknik mengakses potongan array dengan rentang index tertentu"""
#array 2 dimensi
array_2= np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12]
                  ])
#1.pemilihan baris
#start:stop:step
print('2.pemilihan baris')
print(array_2[0:2]) # baris 1 dan 2 saja 
print(array_2[0:4:2]) # atau print(array_2[::2])  = baris 1 dan 3 saja
print(array_2[::-1]) # dibalik urutannya dari yang bawah
print('2.pemilihan kolom')
#2.pemilihan kolom
print(array_2[:,0])  #semua baris dan kolom 1 saja
print(array_2[:,0:2]) #semua baris dengan kolom 1 dan 2 saja
print(array_2[:,0:1]) #semua baris, kolom pertama saja
print(array_2[:,0::2]) #semua baris, kolom pertama dan ketiga

print(array_2[0:2,0:2]) # ambil baris 1 dan 2 ,ambil kolom 1 dan 2