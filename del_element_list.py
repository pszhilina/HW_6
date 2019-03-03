names = ['John', 'Paul', 'George', 'Ringo']
names = list(filter(lambda x: x == 'John' or 'Paul' == x, names))
print(names)