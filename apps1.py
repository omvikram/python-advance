## You are given an array (list) of interval pairs as input where each interval has a start and end timestamp. The input array is sorted by starting timestamps. 
## You are required to merge overlapping intervals and return a new output array.
## Consider the input array below. Intervals (1, 5), (3, 7), (4, 6), (6, 8) are overlapping so they should be merged to one big interval (1, 8). 
## Similarly, intervals (10, 12) and (12, 15) are also overlapping and should be merged to (10, 15).

class Pair:
  def __init__(self, first, second):
    self.first = first
    self.second = second

def merge_intervals(arr):
  result = []
  minFirst = 0
  maxLast = 0
  
  if len(arr) < 1:
      return arr[0]
      
  for x in range(0, len(arr)):
    if(x < len(arr)-1):   
        tempPair = arr[x]
        tempNextPair = arr[x+1]
    
        if(tempPair.first < tempNextPair.first and x == 0):
            minFirst = tempPair.first
        
        if(tempPair.second < tempNextPair.second):
            maxLast = tempNextPair.second
  
  result.append(Pair(minFirst, maxLast))
  return result
  
  
v = [Pair(1, 5), Pair(3, 1), Pair(4, 6), 
     Pair(6, 8), Pair(10, 12), Pair(11, 15)]

resultPair = merge_intervals(v)

print("The merged interval is " + str(resultPair[0].first) + ":" + str(resultPair[0].second) )