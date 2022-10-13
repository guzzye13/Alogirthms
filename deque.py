# Deque
# O(1)
# Initialize queue class and set a empty list
class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):  # Check if list is empty
        return self.items == []

    def add_front(self, item):  # Insert a new element at the front
        self.items.append(item)

    def add_rear(self, item):  # Insert a new element at the rear
        self.items.insert(0, item)

    def remove_front(self):  # Remove at the front
        return self.items.pop()

    def remove_rear(self):  # Remove at the rear
        return self.items.pop(0)

    def size(self):  # Check size of a deque (finally, how may elements are stored)
        return len(self.items)


dqObj = Deque()  # Create an object and try basic operation
# Check if list is empty
print(dqObj.is_empty())
# Add an element at the front
dqObj.add_front(1)
# Add another element at the front
dqObj.add_front(2)
# Add an element at the rear
dqObj.add_rear(9)
# Add another element at the rear
dqObj.add_rear(10)
# Check again if empty
print(dqObj.is_empty())
# Check size
print(dqObj.size())
# show items
print(dqObj.items)
# Remove from front
print(dqObj.remove_front())
# Remove from rear
print(dqObj.remove_rear())
# Check again items
print(dqObj.items)
