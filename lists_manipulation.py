a = [9,8,7,6,5,4,3,2,1]
b = ['a','b','c','d','e','f','g']
a.append(0)
print(a)
a.sort()
print(a)
c = b[2:]
print(c)
d = b.pop(6)
print(d)
del(a[9])
print(a)
e = a + b
print(e)
e[0] = False
e[1] = True
print(e)
