# Implementing a stack

class Stack:
    def __init__(self):
        self.items = [] # empty list

    def is_empty(self):
        return self.items == [] # return -> true or false

    def push(self, item):
        self.items.append(item) # add items in list

    def pop(self): # last item remove
        return self.items.pop()

    def peek(self): # how many item left
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

"""

s = Stack()

# check stack list
print(s.is_empty())

# add item
s.push("A")
s.push("B")
s.push("C")
s.push("D")

# last item
print(s.peek())
print(s.size())
print(s.items)

# pop last item
print(s.pop())
print(s.pop())
print(s.pop())

print(s.peek())
print(s.size())
print(s.items)

"""





