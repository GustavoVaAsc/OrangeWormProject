class BTreeNode:
    def __init__(self,t,leaf):
        self.t = t
        self.keys = [None] * (2 * t - 1)
        self.C = [None] * (2 * t)
        self.n = 0
        self.leaf = leaf

    def insertNonFull(self,data):
        i = self.n - 1 
        if self.leaf: 
            while i >= 0 and self.keys[i].name > data.name: 
                self.keys[i+1] = self.keys[i] 
                i-=1 
            self.keys[i + 1] = data 
            self.n += 1 
        else: 
            while i >= 0 and self.keys[i].name > data.name: 
                i-=1 
            if self.C[i+1].n == 2 * self.t - 1:
                self.splitChild(i+1, self.C[i+1]) 
                if self.keys[i+1].name < data.name:
                    i+=1 
            self.C[i + 1].insertNonFull(data) 
    

    def splitChild(self,i,y):
        z = BTreeNode(y.t, y.leaf) 
        z.n = self.t - 1 
        for j in range (self.t-1): 
            z.keys[j] = y.keys[j + self.t]
        if not y.leaf: 
            for j in range(self.t): 
                z.C[j] = y.C[j + self.t]
        y.n = self.t -1
        
        for j in range(self.n, i , -1): 
            self.C[j + 1] = self.C[j] 
        
        self.C[i+1] = z
        for j in range(self.n -1,i-1, -1): 
            self.keys[j+1] = self.keys[j] 
            
        self.keys[i] = y.keys[self.t - 1] 
        self.n += 1 
    
    def traverse(self,l,user):
        for i in range(self.n):
            if not self.leaf: 
                self.C[i].traverse(l+1,user)
            if self.keys[i].name == user.username:
                print("\t"*l,l,self.keys[i],end = ' ')
            elif self.keys[i].access_level > user.access_level:
                print("\t"*l,"Hidden file")
            else:
                print("\t"*l,l,self.keys[i],end = ' ')
        print() 
        if not self.leaf: 
            self.C[i + 1].traverse(l+1,user) 
            
    def traverseStats(self,l):
        global y
        for i in range(self.n):
            y[self.keys[i].access_level-1] += 1
            if not self.leaf: 
                self.C[i].traverseStats(l+1)
        if not self.leaf: 
            self.C[i + 1].traverseStats(l+1) 
    
    def traverseSave(self,l,toSave):
        for i in range(self.n):
            if not self.leaf: 
                self.C[i].traverseSave(l+1,toSave)
            toSave.append(self.keys[i])
        if not self.leaf: 
            self.C[i + 1].traverseSave(l+1,toSave) 
        
    def search(self,k):
        i = 0 
        while i < self.n and k > self.keys[i].name: 
            i+=1 
        if i < self.n and k == self.keys[i].name:
            return self.keys[i] 
        if self.leaf:
            return None
        return self.C[i].search(k)
     
    def delete(self, key):
        i = 0
        while i < self.n and key > self.keys[i].name:
            i += 1

        if i < self.n and key == self.keys[i].name:
            if self.leaf:
                self.deleteFromLeaf(i)
            else:
                self.deleteFromNonLeaf(i)
        else:
            if self.leaf:
                return
            
            childExists = (i < self.n)

            if self.C[i].n < self.t:
                self.fillChild(i)

            if childExists and i > self.n:
                self.C[i].delete(key)
            else:
                self.C[i].delete(key)

    def deleteFromLeaf(self, i):
        for j in range(i, self.n - 1):
            self.keys[j] = self.keys[j + 1]
        self.n -= 1

    def deleteFromNonLeaf(self, i):
        key = self.keys[i]
        if self.C[i].n >= self.t:
            pred = self.getPredecessor(i)
            self.keys[i] = pred
            self.C[i].delete(pred)
        else:
            if self.C[i + 1].n >= self.t:
                succ = self.getSuccessor(i)
                self.keys[i] = succ
                self.C[i + 1].delete(succ)
            else:
                self.mergeChild(i)

    def getPredecessor(self, i):
        current = self.C[i]
        while not current.leaf:
            current = current.C[current.n]
        return current.keys[current.n - 1]

    def getSuccessor(self, i):
        current = self.C[i + 1]
        while not current.leaf:
            current = current.C[0]
        return current.keys[0]

    def fillChild(self, i):
        if i != 0 and self.C[i - 1].n >= self.t:
            self.borrowFromPrev(i)
        elif i != self.n and self.C[i + 1].n >= self.t:
            self.borrowFromNext(i)
        else:
            if i != self.n:
                self.mergeChild(i)
            else:
                self.mergeChild(i - 1)

    def borrowFromPrev(self, i):
        child = self.C[i]
        sibling = self.C[i - 1]

        for j in range(child.n, 0, -1):
            child.keys[j] = child.keys[j - 1]

        if not child.leaf:
            for j in range(child.n + 1, 0, -1):
                child.C[j] = child.C[j - 1]

        child.keys[0] = self.keys[i - 1]

        self.keys[i - 1] = sibling.keys[sibling.n - 1]

        child.n += 1
        sibling.n -= 1

    def borrowFromNext(self, i):
        child = self.C[i]
        sibling = self.C[i + 1]

        child.keys[child.n] = self.keys[i]

        if not child.leaf:
            child.C[child.n + 1] = sibling.C[0]
            self.keys[i] = sibling.keys[0]

        for j in range(1, sibling.n):
            sibling.keys[j - 1] = sibling.keys[j]

        if not sibling.leaf:
            for j in range(1, sibling.n + 1):
                sibling.C[j - 1] = sibling.C[j]

        child.n += 1
        sibling.n -= 1

    def mergeChild(self, i):
        child = self.C[i]
        sibling = self.C[i + 1]

        child.keys[self.t - 1] = self.keys[i]

        for j in range(sibling.n):
            child.keys[j + self.t] = sibling.keys[j]

        if not child.leaf:
            for j in range(sibling.n + 1):
                child.C[j + self.t] = sibling.C[j]

        for j in range(i + 1, self.n):
            self.keys[j - 1] = self.keys[j]

        for j in range(i + 2, self.n + 1):
            self.C[j - 1] = self.C[j]

        child.n += sibling.n + 1
        self.n -= 1
