from node import Node


def largest_independent_set(root):
    def util(root, take):
        if root is None:
            return 0
        if take:
            return root.val + util(root.left, False) + util(root.right, False)
        return util(root.left, True) + util(root.right, True)

    if root is None:
        return 0

    return max(util(root, True), util(root, False))


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
    print(largest_independent_set(node4))



