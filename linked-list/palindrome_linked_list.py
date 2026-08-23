from single_linked_list import SingleLinkedList, Node

class Solution(object):
    def isPalindrome(self, head):
        """
        Checks if a singly linked list is a palindrome.
        
        :type head: Optional[Node]
        :rtype: bool
        """
        # TODO: Implement this method
        raise NotImplementedError("Implement your solution here")

    def reverse(self, head):
        """
        Helper method to reverse a linked list.
        """
        # TODO: Implement this method (optional helper)
        raise NotImplementedError("Implement your solution here")

if __name__ == "__main__":
    # Helper to convert list to linked list
    def create_linked_list(arr):
        if not arr: return None
        sll = SingleLinkedList()
        for val in arr:
            sll.append(val)
        return sll.head

    # Helper to print linked list
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("END")

    test_cases = [
        ([1, 2, 2, 1], True), # Expected: True
        ([1, 2], False),       # Expected: False
        ([1, 0, 1], True),    # Expected: True
        ([1], True)           # Expected: True
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (nums, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: nums = {nums}")
        head = create_linked_list(nums)
        
        try:
            result = solution.isPalindrome(head)
            
            if result == expected:
                print(f"  [+] PASS (Expected: {expected}, Got: {result})")
            else:
                print(f"  [-] FAIL (Expected: {expected}, Got: {result})")
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
