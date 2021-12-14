from node import Node


def convert(root):
    if root is None:
        return None, None

    l_start, l_end = convert(root.left)
    r_start, r_end = convert(root.right)
    root.left = l_end
    root.right = r_start
    if l_end:
        l_end.right = root
    if r_start:
        r_start.left = root

    if not l_start:
        l_start = root
    if not r_end:
        r_end = root

    return l_start, r_end


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
    start, _ = convert(node4)
    while start:
        print(start.val)
        start = start.right

