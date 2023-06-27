## Given the head pointers of two linked lists where each linked list represents an integer number (each node is a digit), 
## add them and return the resulting linked list. Here, 
## the first node in a list represents the least significant digit.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        
        self.head = new_node
    
    def printList(self): 
      temp = self.head
      
      while(temp): 
        print(temp.data) 
        temp = temp.next
    
    def getList(self): 
      temp = self.head
      tempList = []
      
      while(temp): 
        tempList.append(temp.data) 
        temp = temp.next
        
      return tempList

def addTwoLinkedLists(list1, list2):
    resultList = LinkedList()
    templist1 = []
    templist2 = []
    minlength = 0
    maxlength = 0
    
    templist1 = list1.getList()
    templist2 = list2.getList()
    
    if (len(templist1) > len(templist2)):
        minlength = len(templist2)
        maxlength = len(templist1)
    if (len(templist1) < len(templist2)):
        minlength = len(templist1)
        maxlength = len(templist2)
    if (len(templist1) == len(templist2)):
        minlength = maxlength = len(templist1)
        
    for x in range(maxlength):
        if (x < minlength):
            temp_sum = templist1[x] + templist2[x]
            ##temp_mod = sum % 10
            resultList.push(temp_sum)
            
    return resultList
            
    

v1 = LinkedList()
v1.push(2)
v1.push(8)
v1.push(5)

## v1.printList()

v2 = LinkedList()
v2.push(3)
v2.push(1)
v2.push(2)

## v2.printList()

v3 = addTwoLinkedLists(v1, v2)
v3.printList()