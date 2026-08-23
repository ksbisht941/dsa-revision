class Node:
    def __init__(self, data=0, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Appends a new node to the end of the doubly linked list."""
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        """Prepends a new node to the beginning of the doubly linked list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        

    def insert_after(self, target_data, data):
        """Inserts a new node with 'data' after the first node containing 'target_data'."""
        if self.head is None:
            return

        current = self.head
        while current:
            if current.data == target_data:
                break 
            current = current.next

        new_node = Node(data)
        next = current.next

        current.next = new_node
        new_node.prev = current
        new_node.next = next
        
        if next is not None:
            next.prev = new_node
        else:
            self.tail = new_node

        

    def delete(self, target_data):
        """Deletes the first node that contains 'target_data'."""
        if self.head is None:
            return

        if self.head.data == target_data:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return

        current = self.head
        while current:
            if current.data == target_data:
                break

            current = current.next

        if current is None:
            return
        
        
        current.prev.next =  current.next

        if current.next is not None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev


    def print_forward(self):
        """Prints the list from head to tail."""
        print("START", end=" <-> ")
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("END")

    def print_backward(self):
        """Prints the list from tail to head."""
        print("START", end=" <-> ")
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("START")


if __name__ == "__main__":
    def get_forward_list(dll):
        result = []
        curr = dll.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result
        
    def get_backward_list(dll):
        result = []
        curr = dll.tail
        while curr:
            result.append(curr.data)
            curr = curr.prev
        return result

    def assert_state(dll, expected_forward, test_name):
        actual_forward = get_forward_list(dll)
        actual_backward = get_backward_list(dll)
        expected_backward = expected_forward[::-1]
        
        passed = (actual_forward == expected_forward) and (actual_backward == expected_backward)
        status = "✅ PASS" if passed else "❌ FAIL"
        
        print(f"{status} | {test_name}")
        if not passed:
            print(f"   Expected Forward:  {expected_forward}")
            print(f"   Actual Forward:    {actual_forward}")
            print(f"   Expected Backward: {expected_backward}")
            print(f"   Actual Backward:   {actual_backward}")
            print()

    print("--- Exhaustive Testing Doubly Linked List ---")
    
    dll = DoubleLinkedList()
    
    dll.append(10)
    assert_state(dll, [10], "[Edge Case 1] Append to Empty List")
    
    dll = DoubleLinkedList()
    dll.prepend(10)
    assert_state(dll, [10], "[Edge Case 2] Prepend to Empty List")

    dll = DoubleLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.prepend(0)
    assert_state(dll, [0, 10, 20, 30], "[Normal Cases] Building a list")
    
    dll.insert_after(0, 5)
    assert_state(dll, [0, 5, 10, 20, 30], "[Edge Case 3] Insert after HEAD (0 -> insert 5)")
    
    dll.insert_after(30, 40)
    assert_state(dll, [0, 5, 10, 20, 30, 40], "[Edge Case 4] Insert after TAIL (30 -> insert 40)")

    dll.insert_after(20, 25)
    assert_state(dll, [0, 5, 10, 20, 25, 30, 40], "[Edge Case 5] Insert after Middle (20 -> insert 25)")

    dll.delete(20)
    assert_state(dll, [0, 5, 10, 25, 30, 40], "[Edge Case 6] Delete Middle node (20)")
    
    dll.delete(0)
    assert_state(dll, [5, 10, 25, 30, 40], "[Edge Case 7] Delete HEAD node (0)")
    
    dll.delete(40)
    assert_state(dll, [5, 10, 25, 30], "[Edge Case 8] Delete TAIL node (40)")
    
    dll.delete(5)
    dll.delete(10)
    dll.delete(25)
    dll.delete(30)
    assert_state(dll, [], "[Edge Case 9] Delete the ONLY node left (after deleting everything else)")
