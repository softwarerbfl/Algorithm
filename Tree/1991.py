import sys
n=int(sys.stdin.readline())
tree={}
visited=[]
#전위 순회 : root를 먼저 방문
def preorder(tree, key):
    ch1,ch2=tree[key]
    print(key,end="")
    if ch1 == '.' and ch2 == '.':
        return
    elif ch1 != '.' and ch2 == '.':
        preorder(tree, ch1)
    elif ch1 == '.' and ch2 != '.':
        preorder(tree, ch2)
    elif ch1 != '.' and ch2 != '.':
        preorder(tree, ch1)
        preorder(tree, ch2)
# 중위 순회: 왼쪽 자식, 루트, 오른쪽 자식 순서로 방문
def inorder(tree, key):
    ch1, ch2 = tree[key]
    if ch1!='.' and ch2 !='.':
        inorder(tree,ch1)
        print(key,end="")
        inorder(tree,ch2)
    elif ch1=='.' and ch2=='.':
        print(key,end="")
        return
    elif ch1!='.' and ch2=='.':
        inorder(tree, ch1)
        print(key,end="")
    elif ch1=='.' and ch2!='.':
        print(key,end="")
        inorder(tree,ch2)

# 후위 순회: 왼쪽 자식, 오른쪽 자식, 루트 순서로 방문
def postorder(tree, key):
    ch1, ch2 = tree[key]
    if ch1!='.' and ch2 !='.':
        postorder(tree,ch1)
        postorder(tree,ch2)
        print(key,end="")
    elif ch1=='.' and ch2=='.':
        print(key,end="")
        return
    elif ch1!='.' and ch2=='.':
        postorder(tree, ch1)
        print(key,end="")
    elif ch1=='.' and ch2!='.':
        postorder(tree, ch2)
        print(key, end="")
for i in range(n):
    v1, v2, v3 = list(sys.stdin.readline().split())
    tree[v1]=[v2, v3]
preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree,'A')
