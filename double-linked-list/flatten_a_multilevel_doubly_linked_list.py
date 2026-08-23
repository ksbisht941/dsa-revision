class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Flattens a multilevel doubly linked list.
        
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        stack = [head]
        prev = None

        while stack:
            current = stack.pop()

            if prev:
                prev.next = prev
                current.prev = prev

            if current.next:
                stack.append(current.next)

            if current.child:
                stack.append(current.child)
                current.child = None

            prev = current

        return head


if __name__ == "__main__":
    def create_multilevel_list_1():
        # Level 1
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n1.next, n2.prev = n2, n1
        n2.next, n3.prev = n3, n2
        n3.next, n4.prev = n4, n3
        n4.next, n5.prev = n5, n4
        n5.next, n6.prev = n6, n5
        
        # Level 2
        n7 = Node(7)
        n8 = Node(8)
        n9 = Node(9)
        n10 = Node(10)
        n7.next, n8.prev = n8, n7
        n8.next, n9.prev = n9, n8
        n9.next, n10.prev = n10, n9
        n3.child = n7
        
        # Level 3
        n11 = Node(11)
        n12 = Node(12)
        n11.next, n12.prev = n12, n11
        n8.child = n11
        
        return n1
        
    def create_multilevel_list_2():
        n1 = Node(1)
        n2 = Node(2)
        n1.next, n2.prev = n2, n1
        n3 = Node(3)
        n1.child = n3
        return n1
        
    def flatten_to_array(head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

    test_cases = [
        (create_multilevel_list_1(), [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]),
        (create_multilevel_list_2(), [1, 3, 2]),
        (None, [])
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (head, expected_arr) in enumerate(test_cases):
        print(f"Test case {i+1}:")
        
        try:
            result_head = solution.flatten(head)
            result_arr = flatten_to_array(result_head)
            
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
