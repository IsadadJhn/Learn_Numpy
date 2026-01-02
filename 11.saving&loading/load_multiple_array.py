import numpy as np

arrays =np.load("C:\\Users\\Nayanika\\Downloads\\multiple.npz") #load multiple array in file.npz
#1.ambil satu satu
# array1 = arrays["arr_0"] 
# array2 = arrays["arr_1"]
# print(array1)
#2.ambil banyak dgn menyimpan array  ke dalam list/tuple
data = [arrays["arr_0"],arrays["arr_1"]]
print(data)
