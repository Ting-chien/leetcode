from functools import reduce


a = lambda x, y: x*y
print(a)
print(a(3, 4))

# map()
arr = [50, 12, 22, 3, 17]
result = map(lambda x: x*20, arr)
print(list(result))

# reduce()
arr = [50, 12, 22, 3, 17]
result = reduce(lambda x, y: x + y, arr)
print(result)

# filter()
arr = [50, 12, 22, 3, 17]
result = filter(lambda x: x > 20, arr)
print(list(result))

# sorted()
drinks = [
    ('bubble milk tea', 70),
    ('black tea', 30),
    ('milk tea', 50),
]
result = sorted(drinks, key=lambda drink: drink[1])
print(result)