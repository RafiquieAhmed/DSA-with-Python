class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None


class CircularDoubleLL:
    def __init__(self):
        self.head = None

    # Insert at End
    def insertAtEnd(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            temp.next = temp
            temp.prev = temp
            return

        last = self.head.prev

        last.next = temp
        temp.prev = last
        temp.next = self.head
        self.head.prev = temp

    # Insert at Beginning
    def insertAtBegin(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            temp.next = temp
            temp.prev = temp
            return

        last = self.head.prev

        temp.next = self.head
        temp.prev = last
        last.next = temp
        self.head.prev = temp
        self.head = temp

    # Insert at Middle (after value x)
    def insertAtMiddle(self, value, x):
        if self.head is None:
            return

        t = self.head
        while True:
            if t.data == x:
                break
            t = t.next
            if t == self.head:
                return  # value not found

        temp = Node(value)

        temp.next = t.next
        temp.prev = t
        t.next.prev = temp
        t.next = temp

    # Delete a Node
    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        t = self.head

        while True:
            if t.data == value:
                # only one node
                if t.next == t:
                    self.head = None
                    return

                t.prev.next = t.next
                t.next.prev = t.prev

                if t == self.head:
                    self.head = t.next
                return

            t = t.next
            if t == self.head:
                break

    # Print List
    def printLL(self):
        if self.head is None:
            print("List is empty")
            return

        t = self.head
        while True:
            print(t.data, end=" <--> ")
            t = t.next
            if t == self.head:
                break
        print(t.data)
        
obj = CircularDoubleLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBegin(5)
obj.insertAtMiddle(50, 20)
obj.delete(40)
obj.printLL()

