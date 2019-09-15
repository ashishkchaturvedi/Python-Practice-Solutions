motorcycles=['Yamaha', 'Honda', 'Ducati', 'Suzuki']
print(motorcycles)

motorcycles.append('Kawasaki')
print(motorcycles)

motorcycles.insert(0, 'Triumph')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycle = motorcycles.pop()
print(motorcycle)
print(motorcycles)

motorcycles.remove('Honda')
print(motorcycles)
