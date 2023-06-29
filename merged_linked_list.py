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

def mergeTwoLinkedLists(linkedlist1, linkedlist2):
    resultList = []
    resultLinkedList = LinkedList()

    list1 = linkedlist1.getList()
    list2 = linkedlist2.getList()
    
    for i in range (0, len(list1)):
        resultList.append(list1[i])
        
    for j in range (0, len(list2)):
        resultList.append(list2[j])
        
    resultList.sort(reverse = True)
    
    for k in range (0, len(resultList)):
        resultLinkedList.push(resultList[k])

    return resultLinkedList


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

v3 = mergeTwoLinkedLists(v1, v2)
v3.printList()