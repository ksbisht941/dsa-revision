class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertatEnd(self, value):
        temp = Node(value)

        if (self.head == None):
            self.head = temp
            return

        t1 = self.head

        while (t1.next != None):
            t1 = t1.next

        t1.next = temp


    def insertAtBeg(self, value):
        temp = Node(value)

        if (self.head == None):
            self.head = temp
            return
        
        temp.next = self.head
        self.head = temp


    def insertInBtw(self, value, x):
        temp = Node(value)
        t1 = self.head

        while (t1.next != None):

            if (t1.data == x):
                temp.next = t1.next
                t1.next = temp

            t1 = t1.next


    def deleteLL(self, value):
        t1 = self.head
        prev = t1

        if (self.head.data == value):
            self.head = t1.next
            return

        while (t1.next != None):

            if (t1.data == value):
                prev.next = t1.next
                break
            
            prev = t1
            t1 = t1.next

        if (t1.data == value):
            prev.next = None



    def printLL(self):
        t1 = self.head

        while (t1.next != None):
            print(t1.data, end=" ")
            t1 = t1.next
        
        print(t1.data)



linkedList = SinglyLinkedList()
linkedList.insertatEnd(50)
linkedList.insertatEnd(60)
linkedList.insertatEnd(70)

linkedList.insertAtBeg(30)
linkedList.insertAtBeg(20)
linkedList.insertAtBeg(10)
linkedList.insertAtBeg(0)

linkedList.insertInBtw(40, 30)

linkedList.deleteLL(70)

linkedList.printLL()