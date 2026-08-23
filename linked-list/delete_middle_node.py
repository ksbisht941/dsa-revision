from single_linked_list import SingleLinkedList, Node

class Solution(object):
    def deleteMiddle(self, head: Node) -> Node:
        """
        Delete the middle node of the linked list and return the head of the modified linked list.
        If there are two middle nodes, delete the second middle node.
        
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

    def linked_list_to_array(head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr

    test_cases = [
        # (array, expected_array_after_deletion)
        ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),  # Odd length -> delete 7 (index 3)
        ([1, 2, 3, 4], [1, 2, 4]),                    # Even length -> delete 3 (index 2)
        ([2, 1], [2]),                                # Length 2 -> delete 1 (index 1)
        ([1], [])                                     # Length 1 -> delete 1 (becomes empty)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (arr, expected_arr) in enumerate(test_cases):
        print(f"Test case {i+1}: arr = {arr}")
        head = create_linked_list(arr)
        
        try:
            result = solution.deleteMiddle(head)
            result_arr = linked_list_to_array(result)
            
            if result_arr == expected_arr:
                print(f"  [+] PASS (Expected: {expected_arr}, Got: {result_arr})")
            else:
                print(f"  [-] FAIL (Expected: {expected_arr}, Got: {result_arr})")
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
