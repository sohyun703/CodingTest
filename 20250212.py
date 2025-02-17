https://www.acmicpc.net/problem/1991

N = int(input())
inputs=[]

for _ in range(N):
    inputs.append(input().split())


class Node():
    def __init__(self,item,left,right):
        self.item = item
        self.left = left
        self.right = right


#전위
def preorder(node):
    print(node.item,end='')
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

#중위
def inorder(node):
    if node.left !='.':
        inorder(tree[node.left])
    print(node.item, end="")
    if node.right !='.':
        inorder(tree[node.right])


#후위
def postorder(node) :
    if node.left != '.':
        postorder(tree[node.left])
    if node.right !='.':
        postorder(tree[node.right])

    print(node.item,end='')

tree = {}

for item,left,right in inputs:
    tree[item] =Node(item,left,right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])