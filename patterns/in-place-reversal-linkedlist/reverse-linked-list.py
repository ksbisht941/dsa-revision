# https://leetcode.com/problems/reverse-linked-list/
from typing import List, Optional


class ListNode:
    """Node used to build a singly linked list."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list in place.

    This uses three pointers. For each node, we save the next node, point the
    current node backward to the previous node, then move both pointers forward.

    Args:
        head (Optional[ListNode]): Head node of the linked list

    Returns:
        Optional[ListNode]: New head node after reversing the list

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
        
    previous = None                     # prev = None
    current = head                  # current = 1

    while current is not None:
        # Save the next node before changing the current node's next pointer.
        next_node = current.next    # Iteration 1: next = 2
                                    # Iteration 2: next = 3
                                    # Iteration 3: next = 4
                                    # Iteration 4: next = None

        # Reverse the link so current points to the previous node.
        current.next = previous     # Iteration 1: 1 -> None
                                    # Iteration 2: 2 -> 1
                                    # Iteration 3: 3 -> 2
                                    # Iteration 4: 4 -> 3

        # Move previous and current one step forward.
        previous = current          # Iteration 1: prev = 1
                                    # Iteration 2: prev = 2
                                    # Iteration 3: prev = 3
                                    # Iteration 4: prev = 4

        current = next_node         # Iteration 1: current = 2
                                    # Iteration 2: current = 3
                                    # Iteration 3: current = 4
                                    # Iteration 4: current = None

    return previous


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list and return its head."""
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert a linked list into a Python list for easy printing."""
    values = []
    current = head

    while current is not None:
        values.append(current.val)
        current = current.next

    return values


if __name__ == "__main__":
    examples = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [],
    ]

    for values in examples:
        head = build_linked_list(values)
        reversed_head = reverse_list(head)
        print(f"reverse_list({values}) = {linked_list_to_list(reversed_head)}")
