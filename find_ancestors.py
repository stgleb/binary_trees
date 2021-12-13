from node import Node


def find_ancestors(root, node):
    ancestors = []

    def traverse(root):
        if root is None:
            return False
        if root is node:
            return True
        lf = traverse(root.left)
        if lf:
            ancestors.append(root.val)
            return True
        rf = traverse(root.right)
        if rf:
            ancestors.append(root.val)
            return True
        return False

    traverse(root)
    return ancestors


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
    print(find_ancestors(node4, node3))
    print(find_ancestors(node4, node5))
