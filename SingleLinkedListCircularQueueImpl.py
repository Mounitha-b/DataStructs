class Node:
    def __init__(self, value):
        self.val=value
        self.next=None
        

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.head=None
        self.tail=None
        self.maxsize=k
        self.size=0
        
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        node=Node(value)
        if(self.isFull()):
            return False
        if(self.isEmpty()):
            self.head=node
            self.tail=node
            self.size+=1
            
            return True
        else:
            
            # while(n.next is not None and n.next.val!=None):
            #     n=n.next
            self.tail.next=node
            self.tail=node
            if(self.tail.next is not None):
                self.tail.next.val=value
                self.tail=self.tail.next
                self.size+=1
                return True
            
            
            self.size+=1
            if(self.size==self.maxsize):
                self.tail.next=self.head
            
            return True
            
                
           
            
        
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if(self.isEmpty()):
            return False
        
        
        if(self.head==self.tail):
            self.head=None
            self.tail=None
            self.size=0
            
            return True
        n=self.head.next 
        self.head.val=None
        self.head=n
        self.size-=1
        
        
        return True
        
        
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if(self.isEmpty()):
            return -1
        return self.head.val

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if(self.isEmpty()):
            return -1
        print(self.tail.val)
        return self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if(self.head is None):
            return True
        else:
            return False
            
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if(self.size==self.maxsize):
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
