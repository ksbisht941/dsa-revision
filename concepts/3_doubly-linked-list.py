class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Insert a new node with value at the end of the list."""
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = temp
        temp.prev = current

    def prepend(self, value):
        """Insert a new node with value at the beginning of the list."""
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_after(self, value, target):
        current = self.head

        while current is not None:
            if current.data == target:
                break
            
            current = current.next

        temp = Node(value)
        temp.next = current.next
        current.next = temp
        temp.prev = current

    def delete(self, value):
        raise ValueError(f"Value {value} not found in the list.")

    def print_list(self):
        """Print all node values in list order."""
        current = self.head

        if current is None:
            print("List is empty")
            return

        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" <--> ", end="")
            current = current.next

        print()


if __name__ == "__main__":
    linkedList = DoublyLinkedList()
    linkedList.append(50)
    linkedList.append(60)
    linkedList.append(70)

    linkedList.prepend(30)
    linkedList.prepend(20)
    linkedList.prepend(10)
    linkedList.prepend(0)

    linkedList.insert_after(40, 30)
    
    linkedList.delete(0)
    
    linkedList.print_list()