from BTreeNode import BTreeNode

class BTree:
    def __init__(self,t):
        self.root = None
        self.t = t
    
    def traverse(self,user):
        if self.root != None:
            self.root.traverse(0,user)
            
    def traverseStats(self):
        if self.root != None:
            self.root.traverseStats(0)
            
    def traverseSave(self,toSave):
        if self.root != None:
            self.root.traverseSave(0,toSave)
    
    def search(self,k):
        return None if self.root == None else self.root.search(k)
    
    def insert(self, data):
        if self.root == None: 
            self.root = BTreeNode(self.t,True) 
            self.root.keys[0] = data 
            self.root.n = 1 
        else:
            if self.root.n == 2 * self.t - 1: 
                s = BTreeNode(self.t,False) 
                s.C[0] = self.root 
                s.splitChild(0, self.root) 
                i = 0 
                if s.keys[0].name < data.name: 
                    i+=1 
                s.C[i].insertNonFull(data) 
                self.root = s 
            else: 
                self.root.insertNonFull(data) 
                
    def delete(self, key):
        if self.root is not None:
            self.root.delete(key)
            if self.root.n == 0:
                if self.root.leaf:
                    self.root = None
                else:
                    self.root = self.root.C[0]