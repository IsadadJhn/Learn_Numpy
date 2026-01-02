import numpy as np
# Aggregate functions = fungsi agregat untuk meringkas data
# dan biasanya menghasilkan satu nilai
array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.sum(array))      # Menjumlahkan seluruh elemen array
print(np.mean(array))     # Menghitung nilai rata-rata seluruh elemen
print(np.std(array))      # Menghitung standar deviasi (tingkat sebaran data)
print(np.var(array))      # Menghitung varians (kuadrat dari standar deviasi)
print(np.min(array))      # Mengambil nilai terkecil
print(np.max(array))      # Mengambil nilai terbesar
print(np.argmin(array))   # Mengambil posisi index (flattened) dari nilai terkecil
print(np.argmax(array))   # Mengambil posisi index (flattened) dari nilai terbesar

print(np.sum(array, axis=0))  # Menjumlahkan elemen per kolom (vertikal)
print(np.sum(array, axis=1))  # Menjumlahkan elemen per baris (horizontal)
