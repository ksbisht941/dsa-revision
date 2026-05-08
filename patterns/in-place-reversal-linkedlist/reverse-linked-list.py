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

    previous = None
    current = head

    while current is not None:
        # Save the next node before changing the current node's next pointer.
        next_node = current.next

        # Reverse the link so current points to the previous node.
        current.next = previous

        # Move previous and current one step forward.
        previous = current
        current = next_node

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
