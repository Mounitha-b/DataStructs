class Node(object):
    def __init__(self,data):
        self.pref =None
        self.nref=None
        self.data=data
    
class DoublyLinkedList(object):
    def __init__(self):
        self.start_node=None
    
    def traverse(self):
        n=self.start_node
        if n is None:
            print ("List is empty")
            return
        while n is not None:
            print(n.data)
            n=n.nref
            
        
    def insert_at_beg(self,data):
        new_node=Node(data)
        n=self.start_node
        if n is None:
            self.start_node=new_node
        else:
            new_node.nref=self.start_node
            self.start_node.pref=new_node
            self.start_node=new_node
     
    def insert_at_end(self,data):
        new_node=Node(data)
        n=self.start_node
        if n is None:
            self.start_node=new_node
            return
        while n.nref is not None:
            n=n.nref
        
        n.nref=new_node
        new_node.pref=n
        
    def insert_after_item(self,data,lookup):
        new_node=Node(data)
        n=self.start_node
        
        while n is not None:
            if(n.data ==lookup):
                new_node.prev=n
                new_node.nref=n.nref
                n.nref=new_node
                n.nref.prev=new_node
            n=n.nref
        
            
list1=DoublyLinkedList()
list1.traverse()
list1.insert_at_beg(2)
list1.insert_at_beg(1)
list1.insert_at_beg(8)
list1.insert_at_end(6)
list1.traverse()

print("-----")
list1.insert_after_item(3,6)
list1.traverse()
