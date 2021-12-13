from node import Node


def inorder_traversal(root, list):
    if root is None:
        return
    inorder_traversal(root.left, list)
    list.append(root.val)
    inorder_traversal(root.right, list)


def preorder_traversal(root, list):
    if root is None:
        return
    list.append(root.val)
    preorder_traversal(root.left, list)
    preorder_traversal(root.right, list)


def postorder_traversal(root, list):
    if root is None:
        return
    postorder_traversal(root.left, list)
    postorder_traversal(root.right, list)
    list.append(root.val)


def restore_inorder_preorder(inorder, preorder):
    if len(inorder) == 0:
        return None

    if len(inorder) == 1:
        return Node(inorder[0])

    root_val = preorder[0]
    root_index = 0
    while inorder[root_index] != root_val:
        root_index += 1
    left = restore_inorder_preorder(inorder[:root_index], preorder[1:root_index + 1])
    right = restore_inorder_preorder(inorder[root_index + 1:], preorder[root_index + 1:])
    root = Node(root_val)
    root.left = left
    root.right = right
    return root


def restore_inorder_postorder(inorder, postorder):
    if len(inorder) == 0:
        return None

    if len(inorder) == 1:
        return Node(inorder[0])

    root_val = postorder[-1]
    root_index = 1

    while inorder[root_index] != root_val:
        root_index += 1
    left = restore_inorder_postorder(inorder[:root_index], postorder[:len(postorder) - root_index - 1])
    right = restore_inorder_postorder(inorder[root_index + 1:], postorder[len(postorder) - root_index - 1:len(postorder)- 1])
    root = Node(root_val)
    root.left = left
    root.right = right
    return root


def check_trees_identical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return root1.val == root2.val and check_trees_identical(root1.left, root2.left) \
           and check_trees_identical(root1.right, root2.right)


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
    inorder = []
    preorder = []
    postorder = []
    inorder_traversal(node4, inorder)
    preorder_traversal(node4, preorder)
    postorder_traversal(node4, postorder)
    print(inorder)
    print(preorder)
    print(postorder)

    root1 = restore_inorder_preorder(inorder, preorder)
    root2 = restore_inorder_postorder(inorder, postorder)
    print(check_trees_identical(node4, root1))
    print(check_trees_identical(node4, root2))
