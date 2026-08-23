from double_linked_list import Node

class Solution(object):
    def deleteAllOccurrences(self, head: Node, x: int) -> Node:
        """
        Delete all occurrences of a given key in a doubly linked list.
        
        :type head: Node
        :type x: int
        :rtype: Node
        """
        # TODO: Implement this method
        raise NotImplementedError("Implement your solution here")

if __name__ == "__main__":
    def create_dll(arr):
        if not arr: return None
        head = Node(arr[0])
        curr = head
        for val in arr[1:]:
            new_node = Node(val)
            curr.next = new_node
            new_node.prev = curr
            curr = new_node
        return head

    def get_forward_list(head):
        result = []
        curr = head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result
        
    def get_backward_list(head):
        if not head: return []
        curr = head
        # Go to the tail
        while curr.next:
            curr = curr.next
        
        # Traverse backwards
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.prev
        return result

    def assert_state(head, expected_forward, test_name):
        actual_forward = get_forward_list(head)
        actual_backward = get_backward_list(head)
        expected_backward = expected_forward[::-1]
        
        passed = (actual_forward == expected_forward) and (actual_backward == expected_backward)
        status = "[+] PASS" if passed else "[-] FAIL"
        
        print(f"{status} | {test_name}")
        if not passed:
            print(f"   Expected Forward:  {expected_forward}")
            print(f"   Actual Forward:    {actual_forward}")
            print(f"   Expected Backward: {expected_backward}")
            print(f"   Actual Backward:   {actual_backward}")
            print()
        return passed

    print("--- Testing Delete All Occurrences ---")
    
    test_cases = [
        # (array, target_key, expected_array)
        ([2, 2, 10, 8, 4, 2, 5, 2], 2, [10, 8, 4, 5]), # Multiple occurrences including head and tail
        ([1, 2, 3], 4, [1, 2, 3]),                     # Key not present
        ([2, 2, 2], 2, []),                            # All elements are the key (list becomes empty)
        ([2], 2, []),                                  # Single element which is the key
        ([1], 2, [1]),                                 # Single element not the key
        ([], 2, [])                                    # Empty list
    ]
    
    solution = Solution()
    all_passed = True
    for i, (arr, x, expected) in enumerate(test_cases, 1):
        head = create_dll(arr)
        try:
            result_head = solution.deleteAllOccurrences(head, x)
            if not assert_state(result_head, expected, f"Test Case {i}: Delete {x} from {arr}"):
                all_passed = False
        except NotImplementedError as e:
            print(f"[-] ERROR: {e} | Test Case {i}: Delete {x} from {arr}")
            all_passed = False
        except Exception as e:
            print(f"[-] ERROR: Exception thrown: {e} | Test Case {i}: Delete {x} from {arr}")
            all_passed = False
            
    if all_passed:
        print("\nResult: All test cases passed!")
    else:
        print("\nResult: Some test cases failed. Keep trying!")
