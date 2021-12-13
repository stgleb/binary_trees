from node import Node


def diameter(root):
    def util(root):
        if root is None:
            return 0, 0

        lh, ld = util(root.left)
        rh, rd = util(root.right)

        return max(lh, rh) + 1, max(ld, rd, lh + rh + 1)
    _, d = util(root)
    return d - 1


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)

    node4.left = node2
    node2.left = node1
    node2.right = node3

    node3.right = node5
    node5.right = node6
    node6.right = node7
    node1.right = node8
    print(diameter(node4))
