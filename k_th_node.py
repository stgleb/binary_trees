from node import Node


def kth_node(root, k):
    count = 0
    result = []

    def util(root):
        nonlocal count
        if root is None:
            return None

        util(root.right)
        count += 1
        if count == k:
            result.append(root)
        util(root.left)
    util(root)
    return result[0]


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
    result = kth_node(node4, 4)
    print(result.val)
