class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        new_node = Node(data)
        if head is None :
            head = new_node
        else :
            LastNode = head
            while True :
                if LastNode.next is None :
                    break
                LastNode = LastNode.next
            LastNode.next = new_node
        
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
