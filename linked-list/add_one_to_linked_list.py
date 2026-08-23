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
    def create_linked_list(arr):
        if not arr: return None
        sll = SingleLinkedList()
        for val in arr:
            sll.append(val)
        return sll.head

    def linked_list_to_array(head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr

    test_cases = [
        ([1, 2, 3], [1, 2, 4]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([0], [1]),
        ([1, 9], [2, 0]),
        ([9, 1], [9, 2])
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (nums, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: nums = {nums}")
        head = create_linked_list(nums)
        
        try:
            new_head = solution.addOne(head)
            result_arr = linked_list_to_array(new_head)
            
            if result_arr == expected:
                print(f"  [+] PASS (Expected: {expected}, Got: {result_arr})")
            else:
                print(f"  [-] FAIL (Expected: {expected}, Got: {result_arr})")
                all_passed = False
        except NotImplementedError as e:
            print(f"  [-] ERROR: {e}")
            all_passed = False
        except Exception as e:
            print(f"  [-] ERROR: Exception thrown: {e}")
            all_passed = False
        print("-" * 30)
        
    if all_passed:
        print("\nResult: All test cases passed!")
    else:
        print("\nResult: Some test cases failed. Keep trying!")
