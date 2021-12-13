from node import Node


def distance_k(root, node, k):
    def depth_k(root, distance):
        if root is None:
            return
        if distance == 0:
            print(root.val)
            return
        depth_k(root.left, distance - 1)
        depth_k(root.right, distance - 1)

    def util(root, node, k):
        if root is None:
            return False, 0

        if root is node:
            depth_k(root, k)
            return True, 1
        lf, ld = util(root.left, node, k)
        if lf:
            if ld == k:
                print(root.val)
            depth_k(root.right, k - ld - 1)

        rf, rd = util(root.right, node, k)
        if rf:
            if rd == k:
                print(root.val)
            depth_k(root.left, k - rd - 1)
        return lf or rf, max(ld, rd) + 1
    util(root, node, k)


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
    distance_k(node4, node1, 0)
    print("--------------")
    distance_k(node4, node1, 1)
    print("--------------")
    distance_k(node4, node1, 2)
    print("--------------")
    distance_k(node4, node1, 3)
    print("--------------")
    distance_k(node4, node1, 4)

