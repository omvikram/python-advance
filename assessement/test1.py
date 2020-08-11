import os
import re

path = os.getcwd()
print(path)

f = open("input.txt") #works with python
f = open("input.txt", "r") #works with python3
text = f.read()
print(text)

##############################################

mylist = ["Surprise","efficiency","spanish"]
text = "Nobody expects the Spanish Inquisition! Our chief weapon is surprise... surprise and fear... fear and surprise... our two weapons are fear and surprise... and ruthless efficiency... Our three weapons are fear, surprise, and ruthless efficiency... and an almost fanatical devotion... Our four... no... amongst our weapons.... amongst our weaponry...are such elements as fear, surprise.... I'll come in again."
mystrcountlist =[]

myDict = {"Surprise" : 0, "efficiencey" : 0, "spanish" : 0}
## find the word in the sentence and replace it with number for eg. 1,2,3
## find all the numbers in the text
## count the numbers 


myregex = '%.%,%d '

for each in mylist:
    counter = 0
    mystrlist = text.split(" ")
    for mystr in mystrlist:
        #tempStr = mystr.index(".")
        if(mystr.find(".") or mystr.find(",")):
            #if(mystr.index(".") > -1):
                tempList = mystr.split(".")
            #elif(mystr.index(",") > -1):
                tempList = mystr.split(",")
        
        if(each.lower() == tempList[0].lower()):
            counter = counter +1
        
    mystrcountlist.append(counter)


#print(mystrcountlist) => 5,1,2
#sorting and reverse
# 1,2,5
# 5,2,1
# [0]
# [1]




