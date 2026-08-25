from single_linked_list import SingleLinkedList

def reverse_sll(linked_list):
    """Reverses the linked list in place and updates linked_list.head."""
    current = linked_list.head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    linked_list.head = prev


if __name__ == "__main__":
    def linked_list_to_array(sll):
        arr = []
        curr = sll.head
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr

    test_cases = [
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], [])
    ]
    
    all_passed = True
    
    for i, (nums, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: nums = {nums}")
        sll = SingleLinkedList()
        for num in nums:
            sll.append(num)
            
        try:
            reverse_sll(sll)
            result_arr = linked_list_to_array(sll)
            
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
