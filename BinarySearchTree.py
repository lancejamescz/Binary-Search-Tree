


class Node:
        def __init__(self,key):
            self.left = None
            self.right = None
            self.val = key 

def insert(root,node):
        if root is None:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

l=[16,9,22,14,19,5,6]
print("Original unsorted array is:", l)
r = Node(l[0])
insert(r,Node(l[1]))
insert(r,Node(l[2]))
insert(r,Node(l[3]))
insert(r,Node(l[4]))
insert(r,Node(l[5]))
insert(r,Node(l[6]))
print("Insertion of unsorted list into a Binary Search Tree"); inorder(r)
print("Binary Search Tree after insertion of 8"); insert(r,Node(8)); inorder(r)

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root, key):

    if root is None:
        return root
    if key < root.val:
        root.left = deleteNode(root.left, key)
  
    elif(key > root.val):
        root.right = deleteNode(root.right, key)
  
    else:
        if root.left is None :
            temp = root.right
            root = None
            return temp
        elif root.right is None :
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right , temp.val)
  
    return root
print("Binary Search Tree after deletion of 9"); deleteNode(r,9); inorder(r)

    




