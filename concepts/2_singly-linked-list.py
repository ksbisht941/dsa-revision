class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        """Insert a new node with value at the end of the list."""
        temp = Node(value)

        # If the list is empty, the new node becomes the head.
        if self.head is None:
            self.head = temp
            return

        # Otherwise traverse to the last node.
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = temp

    def prepend(self, value):
        """Insert a new node with value at the beginning of the list."""
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insert_after(self, value, target):
        """Insert a new node with value after the first node containing target."""
        current = self.head

        while current is not None:
            if current.data == target:
                temp = Node(value, current.next)
                current.next = temp
                return
            
            current = current.next

        raise ValueError(f"Value {target} not found in the list.")

    def delete(self, value):
        """Delete the first node that contains the given value."""
        current = self.head
        previous = None

        while current is not None:
            if current.data == value:
                if previous is None:
                    # Deleting the head node.
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

        raise ValueError(f"Value {value} not found in the list.")

    def print_list(self):
        """Print all node values in list order."""
        current = self.head
        if current is None:
            print("List is empty")
            return

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print(None)


if __name__ == "__main__":
    linkedList = SinglyLinkedList()
    linkedList.append(50)
    linkedList.append(60)
    linkedList.append(70)

    linkedList.prepend(30)
    linkedList.prepend(20)
    linkedList.prepend(10)
    linkedList.prepend(0)

    linkedList.insert_after(40, 30)
    
    linkedList.delete(100)
    
    linkedList.print_list()