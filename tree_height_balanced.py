from node import Node


def height(root):
    if root is None:
        return -1

    return max(height(root.left), height(root.right)) + 1


def is_balanced(root):
    def util(root):
        if root is None:
            return 0
        lh = util(root.left)
        rh = util(root.right)
        if lh == -1 or rh == -1:
            return -1
        if abs(rh - lh) > 1:
            return -1
        return max(lh, rh) + 1
    return util(root) != -1


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
    print(height(node4))
    print(is_balanced(node4))
