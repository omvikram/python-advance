##bootcamp file for practice
## Given an integer array, move all elements that are 0 to the left while 
## maintaining the order of other elements in the array. 
## The array has to be modified in-place.
def move_zeros_to_left(arr):
    if len(arr) < 1:
        return arr
        
    tempArr = []
    readIndex = 0
    
    for i in range(0, len(arr)):
        if(arr[i] == 0):
            tempArr.append(i)
            
    for j in range(0, len(tempArr)):
        index = tempArr[j]
        print(index)
        arr.pop(index)
        arr.insert(0,0)

v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print("Original Array:", v)

move_zeros_to_left(v)

print("After Moving Zeroes to Left: ", v)


