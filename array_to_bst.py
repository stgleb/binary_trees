from node import Node


def array_to_bst(arr):
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return Node(arr[0])
    mid = len(arr) // 2
    root = Node(arr[mid])
    left = array_to_bst(arr[:mid])
    right = array_to_bst(arr[mid + 1:])
    root.left = left
    root.right = right
    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = array_to_bst(arr)
    inorder(root)
