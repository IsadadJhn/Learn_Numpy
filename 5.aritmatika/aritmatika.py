import numpy as np

#scalar arimatika

array =np.array([1,2,3,4])
print(np.shape(array)) # output 4 elemen karena array/matriks = 1 dimensi
print(array+1)
print(array-2)
print(array*3)
print(array/4)
print(array**5)

#vectorized math function
"""
Vectorized math function = fungsi matematika yang langsung bisa diaplikasikan
ke seluruh array / vector tanpa perlu pakai loop for
"""
print(np.sqrt(array)) #akar kuadrat 2
array_b = np.array([1.023123,1.344324,2.7634242])
print(np.round(array_b)) #pembulatan umum : x>=5 keatas , x<=5 kebawah
print(np.ceil(array_b)) #pembulatan ke atas
print(np.floor(array_b)) #pembulatan ke atas
print(np.pi) #pi = konstanta bawaan python 

#latihan 
jari2 = np.array([4,5,6])
print(np.pi*jari2**2)

#operasi aritmatika per elemen
array1 = np.array([[1,5,8,4]])
array2 = np.array([[2,3,6,7]])

print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)

#comparison operator
scores=np.array([100,90,30,40,89,22])
print(scores == 100)
print(scores >= 60)