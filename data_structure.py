# to delete elements form list
a = ['a', 'b', 'c']
print(a)
del a[1]
print(a)

# how many number it in the list
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('orange'))

# how to remove last element in the list
fruits = ["apple", "banana", "orange", "grape"]
removed_fruit = fruits.pop()

print("Removed fruit:", removed_fruit)
print("Updated list:", fruits)

# move last element
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
stack.pop()
stack.pop()
print(stack)

# first element
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # Terry arrives
queue.append("Graham") # Graham arrives
queue.popleft() # The first to arrive now leaves
queue.popleft()
print(queue)

