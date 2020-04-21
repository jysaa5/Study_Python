#트리 노드
class Node:
    data = 0
    left = None
    right = None

    def __init__(self):
        self.left = Node
        self.right = Node

#트리 클래스
class Tree:

    def __init__(self):
        self.root = Node()

    def setRoot(self, node):
        self.root = node
    
    def getRoot(self):
        return self.root
    
    def makeNode(self, left, data, right):
        node = Node()
        node.data = data
        node.left = left
        node.right = right
        return node
    
    #inorder: 중위 순회
    def inorder(self, node):
        if (node != None):
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    
    #preorder: 전위 순회 
    def preorder(self, node):
        if(node != None):
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
    
    #postorder: 후위 순회
    def postorder(self, node):
        if(node != None):
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)


#
#     (1)
#    ↙  ↘
#   (2)  (3)
#  ↙ ↘
# (4)  (5)
# Inorder (Left, Root, Right): 4 2 5 1 3
# Preorder (Root, Left, Right): 1 2 4 5 3
# Postorder (Left, Right, Root): 4 5 2 3 1
#    
#
#메인 실행

t = Tree()
n4 = t.makeNode(None, 4, None)
n5 = t.makeNode(None, 5, None)
n2 = t.makeNode(n4, 2, n5)
n3 = t.makeNode(None, 3, None)
n1 = t.makeNode(n2, 1, n3)
t.setRoot(n1)
t.postorder(t.getRoot())


