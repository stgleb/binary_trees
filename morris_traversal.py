from node import Node


def morris_traversal(root):
    while root:
        if root.left:
            l = root.left
            while l.right and l.right != root:
                l = l.right
            if l.right == root:
                l.right = None
                print(root.val)
                root = root.right
            else:
                l.right = root
                root = root.left
        else:
            print(root.val)
            root = root.right


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
    print(morris_traversal(node4))
