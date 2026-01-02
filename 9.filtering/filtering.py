import numpy as np
# filtering = proses memeilih elemen tertentu dari array yang memenuhi suatu kondisi
# seleksi data berdasarkan kondisi.
ages = np.array([[21,16,18,19,25,15,],
                 [39,28,40,65,99,13]])

teenagers = ages [ages<18]
adults = ages[(ages>=18) & (ages<65)]
seniors = ages[ages>=65]
evens = ages[ages%2 == 0]
odds = ages[ages%2 != 0]
print(teenagers)

#function where
adults = np.where(ages>=18 ,ages,0) #yang kurang dari 18 diganti dengan 0

print(adults)