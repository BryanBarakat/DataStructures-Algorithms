class Node:
    
    value = 0
    left_child = None
    right_child = None
    
    def __init__(self, value):
        self.value = value
        
        
class Tree:
    
    root = None
    
    def insert(self,value):
        root = self.root
        if(root == None):
            root = Node(value)
            return
        
        while(True):
            if(value < root.value):
                if(root.left_child != None):
                    root = root.left_child
                else:
                    root.left_child = Node(value)
                    break
            elif(value > root.value):
                if(root.right_child != None):
                    root = root.right_child
                else:
                    root.right_child = Node(value)
                    break
                
    def find(self,value):
        while(root != None):
            if(root.value < value):
                root = root.right_child
            elif(value < root.value):
                root = root.left_child
            else:
                return True
        return False
    
    def traversePreOrder(self,root):
        if(root == None):
            return
        
        print(root.value)
        self.traversePreOrder(root.left_child)     
        self.traversePreOrder(root.right_child)
        
    def preOrderTraversal(self):
        self.traversePreOrder(root)
        
        
    def height_tree(self,root):
        if(root is None):
            return -1
        
        return 1 + math.max(self.height_tree(root.left_child),self.height_tree(root.right_child))
    
    
    def min_binarysearch_tree(self,root):
        if(root is None):
            raise exception("cannot fetch data")
        while(root is not None):
            last = root
            root = root.left_child
        return last.value
    
    def min_tree(self,root):
        if(root.left_child is None and root.right_child is None):
            return root.value
        
        left = self.min_tree(root.left_child)
        right = self.min_tree(root.right_child)
        
        return math.min(math.min(left,right),root.value)
    
    
    def equals(self,root1,root2):
        if(root1 is None and root2 is None):
            return True
        elif(root1 is not None and root2 is not None):
            return root1.value == root2.value and self.equals(root1.left_child,root2.left_child) and self.equals(root1.right_child,root2.right_child)
        return False
    

    def bst(self,root,min,max):
        if(root == None):
            return True
        
        if(max < root.value or min > root.value):
            return False
        
        return self.bst(root.left_child,min,root.value-1) and self.bst(root.right_child,root.value+1,max)
    
    
    def kthNode(self,root,distance): 
        if(root == None):
            return
        
        if(distance == 0):
            return root.value
        
        self.kthNode(root.left_child,distance - 1)
        self.kthNode(root.right_child,distance - 1)
        
        
    def kth(self,distance):
        self.kthNode(self.root,distance)
        
        
    
    def traverseLevelOrder(self):
        for i in range(self.height_tree()):
            for val in self.kth(i):
                print(val)
                
                
    def size(self,root):
        if(root == None):
            return 0       
        return 1 + sum(self.size(root.left_child),self.size(root.right_child))
    
    
    def leaves(self,root):
        if(root == None):
            return 0
        
        if(root.left_child == None and root.right_child == None):
            return 1
        
        return self.leaves(root.left_child) + self.leaves(root.right_child)
    
    
    def max_tree(self,root):
        if(root == None):
            raise Exception("cannot fetch data")
        
        if(root.left_child == None and root.right_child is None):
            return root.value
        
        left = self.max_tree(root.left_child)
        right = self.max_tree(root.right_child)
        
        return math.max(math.max(left,right),root.value)
    
    
    def max_binarysearch_tree(self,root):
        if(root is None):
            raise Exception('cannot fetch data')
        else:
            while(root.right_child is not None):
                root = root.right_child     
            return root.value
        
        
    def contains(self,root,data):  #TODO
        if(root is None):
            return False
        
        if((root.left_child is None and root.right_child is None) and root.value != data):
            return False
        
        left = contains(root.left_child,data)
        right = contains(root.right_child,data)
        
        return left.find(data) or right.find(data)
    
    
    def siblings0(self,root,data1,data2):
        if(root is None):
            raise Exception('cannot fetch data')

        for i in range(self.height_tree()):
            for val in self.kth(i):
                if(val == data1):
                    last_one = i
                if(val == data2 and i == last_one + 1):
                    return True
        return False
    
    
    def siblings(self,root,data1,data2):
        if(root is None):
            raise Exception('cannot fetch data')
        
        if(root.left_child is None and root.right_child is None):
            return False
        
        left = self.siblings(root.left_child,data1,data2)
        right = self.siblings(root.right_child,data1,data2)
        
        return ((left == data1) and (right == data2)) or ((right == data1) and (left == data2))
    
    
    def getAncestors(self,root,data): #didn't understand #TODO
        if(root is None):
            raise Exception('cannot fetch data')
        if(root.value is data):
            return True
        
        
        #geeksforgeeks code
        
        # and returns true, otherwise returns false
        def printAncestors(root, target):
            
            # Base case
            if root == None:
                return False
            
            if root.data == target:
                return True
        
            # If target is present in either left or right subtree
            # of this node, then print this node
            if (printAncestors(root.left, target) or
                printAncestors(root.right, target)):
                print(root.data,end=' ')
                return True
        
            # Else return False
            return False
        