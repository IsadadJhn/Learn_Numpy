import numpy as np
#integer
rng = np.random.default_rng(seed=1) #nilai array akan sama jika seednya tidak diubah
# size = ukuran dimensi
print(rng.integers(low=1,high=101,size=(4,3))) 
#float
print(np.random.uniform())


#random shuffle (acak)
rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)
#choice (pilih)
foods = np.array(["sate","nasgor","migor","seblak","mieayam"])
food = rng.choice(foods,size=3)
print(food)