class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def generate_tree():
    """Build a sample binary tree for traversal demonstrations."""
    root = Node(1)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(8)
    return root


def pre_order(root):
    """Visit the current node, then left subtree, then right subtree."""
    if root is None:
        return []
    return [root.data] + pre_order(root.left) + pre_order(root.right)


def in_order(root):
    """Visit the left subtree, then current node, then right subtree."""
    if root is None:
        return []
    return in_order(root.left) + [root.data] + in_order(root.right)


def post_order(root):
    """Visit the left subtree, then right subtree, then current node."""
    if root is None:
        return []
    return post_order(root.left) + post_order(root.right) + [root.data]


def display_tree(root, prefix="", is_left=True):
    """Render the binary tree structure in the terminal."""
    if root is None:
        return

    if root.right is not None:
        display_tree(root.right, prefix + ("│   " if is_left else "    "), False)

    connector = "└── " if is_left else "┌── "
    print(prefix + connector + str(root.data))

    if root.left is not None:
        display_tree(root.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    root = generate_tree()

    print("Generated tree structure:")
    display_tree(root)

    print("\nDisplay Pre-Order:")
    print(pre_order(root))

    print("Display In-Order:")
    print(in_order(root))

    print("Display Post-Order:")
    print(post_order(root))
