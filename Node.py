class Node:
    def __init__(self,d):
        self.data = d
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.data)

    def append(self,d):
        if not self.next:
            self.next = Node(d)
            self.next.prev = self
        else:
            self.next.append(d)

    def printList(self):
        print(self.data,end=' ')
        if self.next:
            self.next.printList()

    def find(self,d):
        if self.data == d:
            return True
        else:
            if self.next:
                return self.next.find(d)
            else:
                return False

    def delete(self,d):
        if self.data == d:
            if self.next:
                self.next.prev = self.prev
            if self.prev:
                self.prev.next = self.next
            return True
        else:
            if self.next:
                return self.next.delete(d)
            else:
                return False
