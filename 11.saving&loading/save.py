import numpy as np

array = np.array([[1,2,3],[4,5,6]])

# np.save("namafile",array) #tanpa path file akan disimpan di dalam folder default
np.save("C:\\Users\\Nayanika\\Downloads\\namafile",array) #kita bisa menyimpan file.npy ke direktori lain
print(" Numpy array was saved")