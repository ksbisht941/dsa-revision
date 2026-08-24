from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        merge = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                merge.next = list1
                list1 = list1.next
            else:
                merge.next = list2
                list2 = list2.next

            merge = merge.next

        merge.next = list1 if list1 else list2

        return dummy.next



if __name__ == "__main__":
    def create_linked_list(arr):
        if not arr: return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def linked_list_to_array(head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0])
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (l1_arr, l2_arr, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: list1 = {l1_arr}, list2 = {l2_arr}")
        list1 = create_linked_list(l1_arr)
        list2 = create_linked_list(l2_arr)
        
        try:
            result_head = solution.mergeTwoLists(list1, list2)
            result_arr = linked_list_to_array(result_head)
            
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
