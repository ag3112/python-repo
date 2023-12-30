class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.key = val


def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.key, end=' ')
        inOrderTraversal(root.right)


def preOrderTraversal(root):
    if root:
        print(root.key, end=' ')
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)


def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.key, end=' ')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print('In Order Traversal: ')
    inOrderTraversal(root)

    print('\nPre Order Traversal: ')
    preOrderTraversal(root)

    print('\n Post Order Traversal: ')
    postOrderTraversal(root)