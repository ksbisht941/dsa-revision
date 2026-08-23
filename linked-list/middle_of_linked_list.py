from single_linked_list import SingleLinkedList, Node

class Solution(object):
    def middleNode(self, head: Node) -> Node:
        """
        Given the head of a singly linked list, return the middle node of the linked list.
        If there are two middle nodes, return the second middle node.
        
        :type head: Node
        :rtype: Node
        """
        # TODO: Implement this method
        raise NotImplementedError("Implement your solution here")

if __name__ == "__main__":
    def create_linked_list(arr):
        if not arr: return None
        sll = SingleLinkedList()
        for val in arr:
            sll.append(val)
        return sll.head
        
    def print_linked_list(head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("END")

    test_cases = [
        # (array, expected_middle_node_value)
        ([1, 2, 3, 4, 5], 3),     # Odd length -> middle is 3
        ([1, 2, 3, 4, 5, 6], 4),  # Even length -> middle is 4 (the second middle node)
        ([1], 1),                 # Single element -> middle is 1
        ([1, 2], 2)               # Two elements -> middle is 2
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (arr, expected_val) in enumerate(test_cases):
        print(f"Test case {i+1}: arr = {arr}")
        head = create_linked_list(arr)
        
        try:
            result = solution.middleNode(head)
            actual_val = result.data if hasattr(result, 'data') else result
            
            if actual_val == expected_val:
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
