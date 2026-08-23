from single_linked_list import SingleLinkedList, Node

class Solution(object):
    def getIntersectionNode(self, headA: Node, headB: Node) -> Node:
        """
        Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
        
        :type head1, head1: Node
        :rtype: Node
        """

        # lenA = get_length(headA)
        # lenB = get_length(headB)
        
        # currentA = headA
        # currentB = headB

        # if lenA > lenB:
        #     for _ in range(lenA - lenB):
        #         currentA = currentA.next
        # else:
        #     for _ in range(lenB - lenA):
        #         currentB = currentB.next

        # while currentA and currentB:
        #     if currentA is currentB:
        #         return currentA

        #     currentA = currentA.next
        #     currentB = currentB.next

        # return None

        # Approch 2
        currentA = headA
        currentB = headB

        while currentA is not currentB:
            currentA = headB if currentA is None else currentA.next
            currentB = headA if currentB is None else currentB.next

        return currentA

if __name__ == "__main__":
    def create_intersecting_lists(listA_vals, listB_vals, intersect_vals):
        """Helper to create two linked lists that merge at intersect_vals."""
        sll_a = SingleLinkedList()
        sll_b = SingleLinkedList()
        
        for val in listA_vals:
            sll_a.append(val)
        for val in listB_vals:
            sll_b.append(val)
            
        intersect_head = None
        if intersect_vals:
            sll_intersect = SingleLinkedList()
            for val in intersect_vals:
                sll_intersect.append(val)
            intersect_head = sll_intersect.head
            
            # Attach to end of A
            if sll_a.head is None:
                sll_a.head = intersect_head
            else:
                curr = sll_a.head
                while curr.next:
                    curr = curr.next
                curr.next = intersect_head
                
            # Attach to end of B
            if sll_b.head is None:
                sll_b.head = intersect_head
            else:
                curr = sll_b.head
                while curr.next:
                    curr = curr.next
                curr.next = intersect_head
                
        return sll_a.head, sll_b.head, intersect_head

    def print_linked_list(head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("END")

    test_cases = [
        # (listA_prefix, listB_prefix, intersection_part)
        ([4, 1], [5, 6, 1], [8, 4, 5]),  # Intersects at 8
        ([1, 9, 1], [3], [2, 4]),        # Intersects at 2
        ([2, 6, 4], [1, 5], []),         # No intersection
        ([], [], [1])                    # Intersects at head
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (prefix_a, prefix_b, intersect) in enumerate(test_cases):
        print(f"Test case {i+1}: prefix_a = {prefix_a}, prefix_b = {prefix_b}, intersect = {intersect}")
        headA, headB, expected_node = create_intersecting_lists(prefix_a, prefix_b, intersect)
        
        try:
            result = solution.getIntersectionNode(headA, headB)
            
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
