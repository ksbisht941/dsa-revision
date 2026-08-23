class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    """A singly linked list implementation."""
    def __init__(self, head=None):
        self.head = head


    def append(self, data):
        """Appends a new node with the given data to the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        

    def prepend(self, data):
        """Prepends a new node with the given data to the beginning of the list."""
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        
    
    def insert_after(self, insert_value, target_value):
        """Inserts a new node with insert_value after the first node with target_value."""
        
        current = self.head
        new_node = Node(insert_value)

        while current is not None:
            if current.data == target_value:
                next = current.next
                current.next = new_node
                new_node.next = next

            current = current.next


    def delete(self, target_value):
        """Deletes the first node with the given target_value."""
        current = self.head
        previous = None
        while current is not None:

            if current.data == target_value:
                if previous is None:
                    self.head = self.head.next
                else:
                    previous.next = current.next

            previous = current    
            current = current.next

    
    def isPalindrome(self):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        reversed = self.reverse(slow)

        print("START", end=" -> ")
        current = reversed
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("END")

        while slow is not None:
            if slow.data != reversed.data:
                print(slow.data, reversed.data)
                return False

            slow = slow.next
            reversed = reversed.next

        return True


    def reverse(self, head):
        previous = None

        while head is not None:
            next_node = head.next
            head.next = previous
            previous = head

            head = next_node
            
        return previous


    def printLinkedList(self):
        """Prints the elements of the linked list from head to end."""
        current = self.head

        print("START", end=" -> ")

        if current is None:
            print("Empty List")
            return

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("END")
        
    


if __name__ == "__main__":
    sll = SingleLinkedList()

    sll.append(7)
    sll.append(7)
    sll.append(7)
    sll.append(7)
    sll.append(7)

    # sll.prepend(0)
    # sll.prepend(-10)
    # sll.prepend(-20)
    # sll.prepend(-30)

    # sll.insert_after(15, 10)
    # sll.insert_after(25, 20)
    # sll.insert_after(35, 30)

    # sll.insert_after(-15, -20)
    # sll.insert_after(-25, -30)
    # sll.prepend(-35)
    
    sll.delete(7)
    # sll.delete(-25)
    # sll.delete(-15)
    # sll.delete(15)
    # sll.delete(25)
    # sll.delete(35)

    sll.printLinkedList()





        
    