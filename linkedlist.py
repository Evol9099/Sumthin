
class Node:
    def __init__(self, data):
        Node.data = data
        Node.pointer = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def find (self, subject):
        print(self.head)
        print(Llist.head.data)
        finder = self.head
        print(Llist.head.data)
        x = 0
        while finder.data != subject:
            finder = finder.pointer
            x += 1
        print(x)

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.pointer

Llist = Linkedlist()

Llist.head = Node("Nanh")
Second = Node("Phuuk")
Third = Node("Peter")

Llist.head.pointer = Second
Second.pointer = Third

print(Llist.head.data)
Llist.find("someone")

