from collections import deque

# Creating a deque
my_deque = deque([1, 2, 3, 4, 3])

# Adding elements
my_deque.append(5)
my_deque.appendleft(0)

# Iterating through the deque
for element in my_deque:
    print(element)

# Removing elements
rightmost_element = my_deque.pop()
leftmost_element = my_deque.popleft()

# Remove the first occurrence of value in the deque. Raises a ValueError if the value is not present.
my_deque.remove(3)

print(leftmost_element)

# Displaying the deque
print(my_deque)
