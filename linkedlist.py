
class Node:
    def __init__(self, data1,data2):
        self.name = data1
        self.age = data2
        self.pointer = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def findname (self, subject):
        finder = self.head
        x = 0
        while finder.name != subject:
            finder = finder.pointer
            x += 1
        print(x,finder)
        return(finder)

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.name,temp.age)
            temp = temp.pointer

    '''def delete (node):'''




Llist = Linkedlist()

Llist.head = Node("Nanh",1)
Second = Node("Phuuk",6)
Third = Node("Peter",999)

Llist.head.pointer = Second
Second.pointer = Third

Llist.findname("Peter")
Llist.printList()
