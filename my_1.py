s = [1, 6, 15, 9, 17, 35]
print(s)
# list will print

# you can change number in list like this
s[3] = 11
# you can add number in the list
print(s + [3, 99, 132, 174])

# next

s.append(233) # add the cube of 6
print(s)
s.append(5 ** 3) # and the cube of 7
print(s)
s.append(9*2) # and the cube of 8
print(s)

# ----------------------
# print letter
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# will change letter in the list to another
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list from all the elements
# and make it empty
letters[:] = []
print(letters)
# lenght list
letters = ['a', 'b', 'c', 'd']
print(len(letters))

# ---------------------
# a = [1, 2, 3, 4] = b
a = [1, 2, 3, 4] 
b = a
a[2] = 10
b
print(b) # will a after edit 

# ---------------------
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x

print(n[0]) # print 1
print(a[2]) # print c
print(x[0]) # print ['a', 'b', 'c']
print(x[0][1]) # print b

# The value of i is 65536
i = 256*256
print('The value of i is', i)

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# another
a, b = 0, 1
while a < 1000:
    print(a, end=', ')
    a, b = b, a+b