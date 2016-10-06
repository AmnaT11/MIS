L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

print(L[0][0])
print(L[2][2])
print(L[1][2][1])


my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)



print([0]*4)
print(['Tom Brady', 'Bill Belichick']*3)

t = ['a', 'b', 'c', 'd', 'e', 'f']
# ['b','c']
print(t[3:6])

a = [66.25, 333, 333, 1, 1234.5]
a.insert(2, -1)
print(a)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
a


