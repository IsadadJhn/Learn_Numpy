import numpy as np
#dtype = keyword argument yang digunakan untuk memberitahu tipe data apa yang disimpan dalam array
#numpy akan menebak secara otomatis tipe data,tapi
array = np.array([1,2,3,4,5], dtype=np.int8) #set dtype secara manual lebih efisien untuk program dengan dataset besar

print(array) #print array
print(array.dtype) #cek tipe data
print(f"{array.nbytes} bytes") #cek memori yang terpakai
