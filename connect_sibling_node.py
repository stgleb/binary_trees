from node import Node


def connect(root):
    if root is None:
        return
    if root.left and root.right:
        root.left.next = root.right
        next = root.right
    elif root.right:
        next = root.right
    elif root.left:
        next = root.left
    else:
        return
    p = root.next
    while p:
        if p.left:
            next.next = p.left
            break
        if p.right:
            next.next = p.right
            break
        p = p.next
    connect(root.left)
    connect(root.right)


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
    connect(node4)
    p = node4
    while p:
        cur = p
        while cur:
            print(cur.val)
            cur = cur.next
        if p.left:
            p = p.left
        else:
            p = p.right
        print("----------")
