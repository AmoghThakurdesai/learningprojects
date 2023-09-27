class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

s = Stack()
def rev_string(mystr):
    for i in mystr:
        s.push(i)
    rev = []
    for i in range(s.size()):
        rev.append(s.peek())
        s.pop()
    return ''.join(rev)

print(rev_string('jive with me'))