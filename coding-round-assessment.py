"""
A user is holding a wedding ceremony in San Francisco next month. 
They want to show all available listings near the wedding location on a map so their guests can book stays during the wedding. There are lots of listings in San Francisco, 
but we want to show only the top K listings that are closest to the wedding location.


Input:

* K: Integer
* listingLocations: A list of listing’s geos
    * A listing’s geo is represented as [x, y]
    * Both x and y are integers
    * total number of listings is N
* Assuming wedding location’s geo is [0, 0]

Output:

* A list of listing’s geos, with size K. Listings can be in any order
* The K listings in the output should be the closest listings to the wedding location
* The distance between two locations is Euclidean distance

Euclidean distance between (x1,y1) (x2,y2) = Sqrt ((x1-x2)^2 + (y1-y2)^2)

listingArr = [[0,0], [10,20], [20,30], [10, 15], [20,35]]
source = [0,0]
lengthOfListingArr = 0
tempDistanceArr = []
tempDistance = 0.0
##
## 
def calculateEDistance(source, destination):
    edistance = 0
     
    if(source != None and destination != None):
        x1 = source[0]
        y1 = source[1]
        x2 = destination[0]
        y2 = destination[1]
    
    ##(x1,y1) (x2,y2) = Sqrt ((x1-x2)^2 + (y1-y2)^2)
    temp = float((x1 - x2)*2 + (y1-y2)*2)
    edistance = temp
    
    return edistance
    
## Bubble Sort
## Quick Sort
def sortAndFindKthList(listArr, k):
    resultArr = []
    tempVar = 0
    totalLength = len(listArr)-1
    
    for j in totalLength:
        if(listArr[i] > listArr[i+1]):
               tempVar = listArr[i]
               listArr[i] = listArr[i+1] 
               listArr[i+1] = tempVar
               resultArr.append(listArr[i])
        
    for i in len(resultArr):
        if(i < k ):
        elif (i >= K):
            resultArr.pop()
            
    return resultArr
    
    
k = str(input("Please enter the kth element for listing :"))

lengthOfListingArr = len(listingArr)

## Loop through each element in the listingArr and calculate the Edistance w.r.t source lat long
for i in range (lengthOfListingArr):
    tempDestination = listingArr[i]

    tempDestination =  calculateEDistance (source, tempDestination)
    tempDistanceArr.append(tempDestination)
    
## Sort the temporary distance array and pick the kth elements from the list

resultArr = sortAndFindKthList(tempDistanceArr, k)

## print all the elements from resultArr which is the kth nearest lsitings

