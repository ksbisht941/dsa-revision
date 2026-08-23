from single_linked_list import SingleLinkedList, Node

class Solution(object):
    def countNodesinLoop(self, head: Node) -> int:
        """
        Function to find the length of a loop in the linked list.
        Returns 0 if there is no loop.
        
        :type head: Node
        :rtype: int
        """
        # TODO: Implement this method
        raise NotImplementedError("Implement your solution here")

if __name__ == "__main__":
    def create_list_with_loop(arr, pos):
        """
        Helper to create a linked list with a loop.
        'pos' is the 0-indexed position of the node where the tail connects.
        If pos is -1, there is no loop.
        """
        if not arr: return None
        sll = SingleLinkedList()
        for val in arr:
            sll.append(val)
            
        if pos == -1:
            return sll.head
            
        loop_node = sll.head
        for _ in range(pos):
            loop_node = loop_node.next
            
        curr = sll.head
        while curr.next:
            curr = curr.next
            
        # Connect tail to the loop_node
        curr.next = loop_node
        
        return sll.head

    test_cases = [
        # (array, loop_start_index, expected_loop_length)
        ([25, 14, 19, 33, 10, 21, 39, 90, 58, 45], 3, 7), # Loop starts at 33, size is 7
        ([1, 2, 3], 0, 3),                                # Loop connects to head, size is 3
        ([1, 2, 3, 4], -1, 0),                            # No loop, size is 0
        ([1], 0, 1),                                      # Single node points to itself
        ([1, 2], 1, 1)                                    # Tail points to itself
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (arr, pos, expected_length) in enumerate(test_cases):
        print(f"Test case {i+1}: arr = {arr}, pos = {pos}")
        head = create_list_with_loop(arr, pos)
        
        try:
            result = solution.countNodesinLoop(head)
            
            if result == expected_length:
                print(f"  [+] PASS (Expected: {expected_length}, Got: {result})")
            else:
                print(f"  [-] FAIL (Expected: {expected_length}, Got: {result})")
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
