from single_linked_list import SingleLinkedList, Node

class Solution(object):
    def detectCycle(self, head: Node) -> Node:
        """
        Given the head of a linked list, return the node where the cycle begins. 
        If there is no cycle, return None.
        
        :type head: Node
        :rtype: Node
        """
        # TODO: Implement this method
        raise NotImplementedError("Implement your solution here")

if __name__ == "__main__":
    def create_list_with_loop(arr, pos):
        """
        Helper to create a linked list with a loop.
        'pos' is the 0-indexed position of the node where the tail connects.
        If pos is -1, there is no loop.
        Returns (head, cycle_start_node)
        """
        if not arr: return None, None
        sll = SingleLinkedList()
        for val in arr:
            sll.append(val)
            
        if pos == -1:
            return sll.head, None
            
        loop_node = sll.head
        for _ in range(pos):
            loop_node = loop_node.next
            
        curr = sll.head
        while curr.next:
            curr = curr.next
            
        # Connect tail to the loop_node
        curr.next = loop_node
        
        return sll.head, loop_node

    test_cases = [
        # (array, loop_start_index)
        ([3, 2, 0, -4], 1), # Cycle connects to index 1 (value 2)
        ([1, 2], 0),        # Cycle connects to index 0 (value 1)
        ([1], -1),          # No cycle
        ([], -1)            # Empty list, no cycle
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (arr, pos) in enumerate(test_cases):
        print(f"Test case {i+1}: arr = {arr}, pos = {pos}")
        head, expected_node = create_list_with_loop(arr, pos)
        
        try:
            result = solution.detectCycle(head)
            
            expected_val = expected_node.data if expected_node else "None"
            actual_val = result.data if hasattr(result, 'data') else result
            
            if expected_node == result:
                print(f"  [+] PASS (Expected: {expected_val}, Got: {actual_val})")
            else:
                print(f"  [-] FAIL (Expected: {expected_val}, Got: {actual_val})")
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
