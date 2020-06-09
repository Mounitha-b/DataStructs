class DynamicArray(object):
    def __init__(self):
        self.length=0
        self.capacity=0
    def __init__(self,capacity):
        if(capacity<0):
            raise Exception("Sorry, capacity cant be negative")
        self.length=0
        self.capacity=capacity
        self.A=[None]*capacity
        
        
    def show(self):
        print(self.A)
        
    def append(self,value):
        if(self.length==self.capacity):
            self.capacity*=2
            B=[None]*(self.capacity)
            for i in range(self.length):
                B[i]=self.A[i]
            B[self.length]=value
            self.A=B
            self.length+=1
        else:
            self.A[self.length]=value
            self.length+=1
            
            
        
        
        
    def size(self):
        return self.length
    def isempty(self):
        return self.size()==0;
    def get(self,value):
        return self.A[value]
    def set(self,ind,value):
        if(ind>self.length or ind<0):
            raise Exception("Sorry, out of range")
        self.A[ind]=value
    def clear(self):
        for i in range(self.length):
            self.A[i]=None
        self.length=0
            
    def removeAt(self,ind):
        B=[None]*self.length
        for i,j in zip(range(self.length),range(self.length)):
            
            if(i==ind):
                j=j-1
            else:
                B[j]=self.A[i]
            B[j]=self.A[i]
        self.A=B
        return self.A
        
            
        
        
        
    
  
        
A=DynamicArray(2)
print(A.isempty())
A.show()
print(A.size())
A.append(1)
A.show()
print(A.size())
A.append(2)
A.show()
print(A.size())
A.append(3)
A.show()
print(A.size())
A.append(4)
A.show()
print(A.size())
print(A.isempty())
A.set(3,5)
A.show()
A.removeAt(3)
A.show()


        


