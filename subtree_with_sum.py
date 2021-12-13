from node import Node


def subtree_with_sum(root, k):
    preorder = []
    subtrees = []

    def preorder_traversal(root):
        if root is None:
            return
        preorder.append(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)
    preorder_traversal(root)
    i, j = 0, 0
    count = 0

    while i < len(preorder):
        if count < k:
            count += preorder[i]
            i += 1
        elif count > k:
            count -= preorder[j]
            j += 1
        else:
            subtrees.append(preorder[j:i])
            count += preorder[i]
            i += 1
    return subtrees


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
    print(subtree_with_sum(node4, 6))
