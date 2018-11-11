class Node:
    def __init__(self, data):
        Node.data = data
        Node.pointer = None

    def find(self,subject):
        temp = self.data
        if temp == subject:
            print(temp)

something = Node("something")
something.pointer = "blabla"
nothing = something

something.find("something")
