from single_linked_list import SingleLinkedList, Node

class Solution(object):
    def hasCycle(self, head: Node) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        Return true if there is a cycle in the linked list. Otherwise, return false.
        
        :type head: Node
        :rtype: bool
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
        # (array, loop_start_index, expected_has_cycle)
        ([3, 2, 0, -4], 1, True), # Cycle connects to index 1 (value 2)
        ([1, 2], 0, True),        # Cycle connects to index 0 (value 1)
        ([1], -1, False),         # No cycle
        ([], -1, False)           # Empty list, no cycle
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (arr, pos, expected_result) in enumerate(test_cases):
        print(f"Test case {i+1}: arr = {arr}, pos = {pos}")
        head = create_list_with_loop(arr, pos)
        
        try:
            result = solution.hasCycle(head)
            
            if result == expected_result:
                print(f"  [+] PASS (Expected: {expected_result}, Got: {result})")
            else:
                print(f"  [-] FAIL (Expected: {expected_result}, Got: {result})")
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
