class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        
        self.arr=[None]*k
        self.size=k
        self.head=-1
        self.tail=-1
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        
        if(self.isEmpty()):
            self.head=0
            self.tail=0
            self.arr[0]=value
            return True
        if(self.isFull()):
            return False
        self.tail=(self.tail+1)%self.size
        self.arr[self.tail]=value
        print (self.arr[self.tail])
        return True
        
            
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if(self.isEmpty()):
            return False
        if(self.head==self.tail):
            self.head=self.tail=-1
            return True
        self.arr[self.head]=None
        self.head=(self.head+1)
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if(self.isEmpty()):
            return -1
        else:
            return self.arr[self.head]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if(self.isEmpty()):
            return -1
        else:
            return self.arr[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.head==-1 and self.tail==-1:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if((self.tail+1)%self.size == self.head):
            return True
        else: return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
