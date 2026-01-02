import numpy as np
# numpy = library yang digunakan untuk menjalankan operasi matematika salah satunya adalah array/matriks
# 1.tanpa array
my_list = [1,2,3,4]
my_list = my_list*2
print(my_list)
#hasil sama dengan = [1,2,3,4,1,2,3,4]
# 2. dengan array
array = np.array([1,2,3,4])
array = array*2
print(array)
print(type(array))
#hasil sama dengan = [2,4,6,8]

print(np.__version__) #cek versi numpy
