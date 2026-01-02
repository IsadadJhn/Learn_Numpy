import numpy as np
"""Numpy bisa buat array sampai dimensi berapapun = gak ada batas maksimal (selama RAM kuat)"""
#array 0 dimensi
array_0 = np.array(5) 
print(array_0.ndim)
#array 1 dimensi
array_1 = np.array([]) 
print(array_1.ndim)
 #array 2 dimensi
array_2= np.array([[1,2,3],
                   [3,4,5],
                   [6,7,8]
                  ])
print(array_2.ndim)
print(array_2.shape) #cek bentuk matriks = (3,3) = 3 baris 3 kolom
print(array_2[0,]) #index dibaca dari 0
"""     kolom 0,kolom 1,kolom2
baris 0 = [1,2,3]
baris 1 = [3,4,5]
baris 2 = [6,7,8] """
#array 3 dimensi
array_3= np.array([[[1,2,3],
                   [4,5,6],
                   [7,8,9]]]) 
print(array_3.ndim)
print(array_3.shape) #cek bentuk matriks = (1,3,3) = 1 lapis 3 baris 3 kolom
