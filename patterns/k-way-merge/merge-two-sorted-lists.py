# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import List, Optional


class ListNode:
    """Node used to build a singly linked list."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def merge_two_lists(
    list1: Optional[ListNode],
    list2: Optional[ListNode],
) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted linked list.

    This uses a dummy node to simplify building the merged list. At each step,
    we compare the current nodes from both lists and attach the smaller one.

    Args:
        list1 (Optional[ListNode]): Head node of the first sorted linked list
        list2 (Optional[ListNode]): Head node of the second sorted linked list

    Returns:
        Optional[ListNode]: Head node of the merged sorted linked list

    Time Complexity: O(n + m)
    Space Complexity: O(1)
    """

    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        # Attach the smaller current node to the merged list.
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        # Move the merged-list pointer to the node we just attached.
        current = current.next

    # Attach the remaining nodes from the list that still has values.
    current.next = list1 if list1 is not None else list2

    return dummy.next


# LeetCode uses camelCase for this function name.
def mergeTwoLists(
    list1: Optional[ListNode],
    list2: Optional[ListNode],
) -> Optional[ListNode]:
    """Merge two sorted linked lists into one sorted linked list."""
    return merge_two_lists(list1, list2)


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
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0]),
        ([2, 5, 8], [1, 3, 7, 9]),
    ]

    for values1, values2 in examples:
        list1 = build_linked_list(values1)
        list2 = build_linked_list(values2)
        merged_head = merge_two_lists(list1, list2)
        print(
            f"merge_two_lists({values1}, {values2}) = "
            f"{linked_list_to_list(merged_head)}"
        )
