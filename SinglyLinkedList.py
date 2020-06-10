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
        flag=False
        while n is not None:
            if(n.item==search):
                flag=True
                new_node.ref=n.ref
                n.ref=new_node
                break
            n=n.ref
        if(not flag):
            print("Element not found")
    # def insert_after_item(self, x, data):

    #     n = self.start_node
    #     print(n.ref)
    #     while n is not None:
    #         if n.item == x:
    #             break
    #         n = n.ref
    #     if n is None:
    #         print("item not in the list")
    #     else:
    #         new_node = Node(data)
    #         new_node.ref = n.ref
    #         n.ref = new_node
           
    
    
    
    def insert_before_item(self,data,search):
        new_node=Node(data)
        n=self.start_node
        
        if n is None:
            print("List is empty")
            return
        if n.item==search:
            new_node.ref=n
            self.start_node=new_node
            return
        
        while n.ref is not None:
            if(n.ref.item==search):
                
                break
            n=n.ref
            
        if n.ref is None:
            print("Element not found")
        else:
            new_node.ref=n.ref
            n.ref=new_node
                
    def insert_at_index(self,index,data):
        new_node=Node(data)
        n=self.start_node
        count=1
        if (index==1):
            new_node.ref=n
            self.start_node=new_node
            return
        
        while n is not None:
            # print("c",count)
            if(count==index-1):
                break
            n=n.ref
            count+=1
            
        if n is None:
            print("index out of bound")
        else:    
            new_node.ref=n.ref
            n.ref=new_node
        
        
        
    def traverse(self):
        n=self.start_node
        if n is None:
            print("List is empty")
            return
        
        while n is not None:
            print(n.item)
            n=n.ref
    
    def getCount(self):
        n=self.start_node
        
        count=0
        while n is not None:
            count+=1
            n=n.ref
        return count
        
            
    def search_item(self,num):
        n=self.start_node
        while n is not None:
            if n.item==num:
                return True
            n=n.ref
        return False
    
    def delete_at_start(self):
        n=self.start_node
        if n is None:
            print ("List is empty. Nothing to delete")
            return
        else:
            self.start_node=n.ref
            n.ref=None
        
    def delete_at_end(self):
        n=self.start_node
        if n is None:
            print ("List is empty. Nothing to delete")
            return
        
        if(n.ref is None):
            self.start_node=None
        
        while n.ref is not None:
            if(n.ref.ref is None):
                n.ref=None
                break
            n=n.ref
            
    def delete_value(self,data):
        n=self.start_node
        
        if n is None:
            print ("Enpty list")
            return
        if self.start_node==data:
            self.start_node=n.ref
        
        while n.ref is not None:
            if n.ref.item==data:
                break
            n=n.ref
        
        if n.ref is None:
            print ("Item not found")
            
        else:
            n.ref=n.ref.ref
            
    def reverse_list(self):
        n=self.start_node
        prev=None
        while n is not None:
            next=n.ref
            n.ref=prev
            prev=n
            n=next
            
        self.start_node=prev
        
        
        

test=SinglyLinkedList()
test.insert_at_start(1)
test.insert_at_start(2)
test.insert_at_end(5)
test.insert_after_item(7,4)
test.insert_before_item(8,5)
test.insert_before_item(8,2)
test.traverse()
print("-----")

# test.insert_at_index(8,55)
# test.traverse()
# print("-----")
# print(test.getCount())
# print("-----")
# print(test.search_item(84))
# test.delete_at_start()
# print("-----")
# test.traverse()

# test.delete_at_end()


# print("-----")
# test.traverse()

# print("-----")
# test.delete_value(1)
# test.traverse()
# # test2 =SinglyLinkedList()

test.reverse_list()
test.traverse()
# # test2.make_new_list()
