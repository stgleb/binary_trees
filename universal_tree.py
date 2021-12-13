from node import Node


def count_inversal_trees(root):
    universal_trees = []

    def util(root, universal_trees):
        if root is None:
            return True
        l = util(root.left, universal_trees)
        r = util(root.right, universal_trees)

        if root.left:
            if l and root.left.val != root.val:
                universal_trees.append(root.left)
                l = False

        if root.right:
            if r and root.right.val != root.val:
                universal_trees.append(root.right)
                r = False

        if l and r:
            return True

        return False

    util(root, universal_trees)
    return universal_trees


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(1)
    node3 = Node(1)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(5)
    node7 = Node(5)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node6
    node6.left = node5
    node6.right = node7
    print(count_inversal_trees(node4))
