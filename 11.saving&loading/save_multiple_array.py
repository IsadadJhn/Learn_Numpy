import numpy as np

array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[1.1,2.2,3.3],[4.4,5.5,6.6]])

np.savez("C:\\Users\\Nayanika\\Downloads\\multiple",array1,array2) #disimpan dalam bentuk "file.npz"
# np.savez_compressed("C:\\Users\\Nayanika\\Downloads\\multiple",array1,array2) #ukuran lebih kecil karena dikompres
print("numpy arrays were saved")