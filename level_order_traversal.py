from node import Node


def compute_levels(root):
    q = [root]
    levels = dict()
    levels[root.val] = 0
    while q:
        cur = q.pop()
        if cur.left:
            q.append(cur.left)
            levels[cur.left.val] = levels[cur.val] + 1
        if cur.right:
            q.append(cur.right)
            levels[cur.right.val] = levels[cur.val] + 1

    return levels


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
    print(compute_levels(node4))
