from node import Node


def isomorphic(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    var1 = isomorphic(root1.left, root2.left) and isomorphic(root1.right, root2.right)
    var2 = isomorphic(root1.right, root2.left) and isomorphic(root1.left, root2.right)

    return var1 or var2


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

    node11 = Node(1)
    node21 = Node(2)
    node31 = Node(3)
    node41 = Node(4)
    node51 = Node(5)
    node61 = Node(6)
    node71 = Node(7)

    node41.left = node61
    node21.left = node11
    node21.right = node31
    node41.right = node21
    node61.left = node71
    node61.right = node51
    print(isomorphic(node4, node41))


