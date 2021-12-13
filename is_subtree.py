from node import Node


def has_subtree(root, subtree_root):
    def is_subtree(root, subtree_root):
        if subtree_root is None:
            return True
        if root is None:
            return False
        return root.val == subtree_root.val and is_subtree(root.left, subtree_root.left) \
               and is_subtree(root.right, subtree_root.right)
    stack = [root]
    while stack:
        cur = stack.pop()
        if is_subtree(cur, subtree_root):
            return True
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return False


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node6
    node6.left = node5
    node6.right = node7

    subtree = Node(2)
    subtree_leaf = Node(3)
    subtree.right = subtree_leaf
    print(has_subtree(node4, subtree))
