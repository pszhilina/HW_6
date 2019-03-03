# на основе цикла for
l = []
for i in [2, 4, 9, 16, 25]:
    l.append(pow(i, 0.5))
print(l)

# на основе функции map
print(list(map(lambda a: pow(a, 0.5), [2, 4, 9, 16, 25])))

# в виде генератора списка
L = [2, 4, 9, 16, 25]
l = [pow(i, 0.5) for i in L]
print(l)
