import collections

from node import Node


def zig_zag(root):
    q = collections.deque()
    q.append(root)
    order = True
    levels = []
    while q:
        next_level = collections.deque()
        level = []
        for v in q:
            if v:
                level.append(v.val)
        if level:
            levels.append(level)
        while q:
            if order:
                cur = q.popleft()
                if not cur:
                    continue
                next_level.append(cur.left)
                next_level.append(cur.right)
            else:
                cur = q.pop()
                if not cur:
                    continue
                next_level.append(cur.right)
                next_level.append(cur.left)
        q = next_level
        order = not order
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
    print(zig_zag(node4))
