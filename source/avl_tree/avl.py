import node as nd


class avl_tree:

    def height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def balance(self, node):
        if node is None:
            return 0
        else:
            return self.height(node.left)-self.height(node.right)

    def minimumValueNode(self, node):
        if node is None or node.left is None:
            return node
        else:
            return self.minimumValueNode(node.left)

    def rotateR(self,node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        node.height = 1 + max(self.height(node.left),self.height(node.right))
        a.height = 1 + max(self.height(a.left),self.height(a.right))
        return a 

    def rotateL(self,node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        node.height = 1 + max(self.height(node.left),self.height(node.right))
        a.height = 1 + max(self.height(a.left),self.height(a.right))
        return a
    
    def insert(self, val, root):
        if root is None:
            return nd.node(val)
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        elif val > root.value:
            root.right = self.insert(val, root.right)
        root.height = 1 + max(self.height(root.left),self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root

    def delete(self,val, node):
        if node is None:
            return node
        elif val < node.value:
            node.left = self.delete(val, node.left)
        elif val > node.value:
            node.left = self.delete(val,node.right)
        else:
            if node.left is None:
                it = node.right
                node = None
                return it
            elif node.right is None:
                it = node.left
                node = None
                return it
            rgt = self.minimumValueNode(node.right)
            node.value = rgt.value
            node.right = self.delete(rgt.value,node.right)
        if node is None:
            return node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)
        if balance > 1 and self.balance(node.left) >= 0:
            return self.rotateR(node)
        if balance < -1 and self.balance(node.right) <= 0:
            return self.rotateL(node)
        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.rotateL(node.left)
            return self.rotateR(node)
        if balance < -1 and self.balance(node.right) > 0:
            node.right = self.rotateR(node.right)
            return self.rotateL(node)
        return node
    
    def preorder(self, root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def sort_list_by_avl(self,root):
        if root is None:
            return
        





