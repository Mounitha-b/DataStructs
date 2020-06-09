class Node(object):
    def __init__(self,value):
        self.item=value
        self.ref=None


class SinglyLinkedList(object):
    def __init__(self):
        self.start_node=None

    
    def insert_at_start(self,data):
        new_node=Node(data)
        new_node.ref=self.start_node
        self.start_node=new_node
        
    def insert_at_end(self,data):
        new_node=Node(data)
        n=self.start_node
        if n is None:
            self.start=new_node
            return
        while n.ref is not None:
            n=n.ref
        n.ref=new_node
        
    def insert_after_item(self,data,search):
        new_node=Node(data)
        n=self.start_node
        
        while n is not None:
            if(n.item==search):
                
                break
            n=n.ref
           
        
    def traverse(self):
        n=self.start_node
        if n is None:
            print("List is empty")
            return
        
        while n is not None:
            print(n.item)
            n=n.ref
            
            
            
            
            

test=SinglyLinkedList()
test.insert_at_start(1)
test.insert_at_start(2)
test.insert_at_end(5)
test.traverse()
        
