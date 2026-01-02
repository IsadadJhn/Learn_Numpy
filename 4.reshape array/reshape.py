import numpy as np
#reshape  = mengubah bentuk arrray tanpa menghapus elemennya
array = np.array([1,2,3,4,5,6,7,8,9,10])
# print(array)
# print(array.shape)
# print("sesudah di reshape")
# array = array.reshape([5,2])
# print(array)
# print(array.shape)

array = array.reshape(1,-1)
print(array.shape)
print(array)
array = array.reshape(-1,1) #1 kolom
print(array.shape)
print(array)
