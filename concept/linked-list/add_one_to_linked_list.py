from single_linked_list import SingleLinkedList, Node

class Solution:
    def addOne(self, head: Node) -> Node:
        """
        Adds one to the number represented by the linked list.
        The most significant digit is at the head of the linked list.
        
        :type head: Node
        :rtype: Node
        """
        # Approach 1: Reversing the linked list
        # def reverse(head: Node) -> Node:
        #     prev = None
        # 
        #     while head is not None:
        #         next = head.next
        #         head.next = prev
        #         prev = head
        #         head = next
        # 
        #     return prev

        # head = reverse(head)
        #
        # carry = 1
        # current = head
        # prev = None
        #
        # while current is not None:
        #     total = current.data + carry
        #     current.data = total % 10
        #     carry = total // 10
        #
        #     if carry == 0:
        #         break
        #     
        #     prev = current
        #     current = current.next
        #
        # if carry > 0:
        #     new_node = Node(carry)
        #     prev.next = new_node
        # 
        # return reverse(head)
        
        # Approach 2: Recursive
        # def add(node) -> int:
        #     if node is None:
        #         return 1

        #     carry = add(node.next)

        #     total = node.data + carry
        #     node.data = total % 10
        #     return total // 10

        # carry = add(head)

        # if carry:
        #     new_node = Node(carry)
        #     new_node.next = head 
        #     head = new_node

        # return head

        # Approach 3
        last_not_9 = None
        current = head

        while current:
            if current.data != 9:
                last_not_9 = current
            current = current.next

        if last_not_9 is None:
            new_node = Node(1)
            new_node.next = head

            current = head
            while current:
                current.data = 0
                current = current.next
            return new_node

        last_not_9.data += 1

        current = last_not_9.next
        while current:
            current.data = 0
            current = current.next

        return head




if __name__ == "__main__":
    # Helper to convert list to linked list
    def create_linked_list(arr):
        if not arr: return None
        sll = SingleLinkedList()
        
        # We append directly to utilize existing methods, but our linked 
        # list append adds to the end. Let's just use it.
        for val in arr:
            sll.append(val)
        return sll.head

    # Helper to print linked list
    def print_linked_list(head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("END")

    test_cases = [
        [1, 2, 3], # Expected output: 1 -> 2 -> 4 -> END
        [9, 9, 9], # Expected output: 1 -> 0 -> 0 -> 0 -> END
        [0],       # Expected output: 1 -> END
        [1, 9],    # Expected output: 2 -> 0 -> END
        [9, 1]     # Expected output: 9 -> 2 -> END
    ]
    
    solution = Solution()
    for nums in test_cases:
        head = create_linked_list(nums)
        print(f"Input:    ", end="")
        print_linked_list(head)
        
        new_head = solution.addOne(head)
        
        print(f"Output:   ", end="")
        if new_head is None:
            print("Not implemented yet.")
        else:
            print_linked_list(new_head)
        print("-" * 25)
