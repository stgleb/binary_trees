from node import Node


def threaded_tree(root):
    def walk(root, prev, order):
        if root is None:
            return

        if root.left is None and root.right is None:
            if order:
                root.left = prev
            else:
                root.right = prev
            return

        if order:
            walk(root.left, prev, order)
            walk(root.right, root, order)
        else:
            walk(root.right, root, order)
            walk(root.left, prev, order)
    # walk(root, None, True)
    walk(root, None, False)


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
    threaded_tree(node4)

