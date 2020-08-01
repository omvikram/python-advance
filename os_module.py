#lets create a practice file which we will delete at the end
#f = open('practice.txt', 'w+')
#f.write("HELLO WORLD")
#f.close()

import os
path = os.getcwd()
print(path)
for each in os.listdir(path):
    print(each)


source = (path + "/source")
destination = (path + "/destination")

f1 = open(source + "/test1.txt", 'w+')
f1.write("TEST 1 FILE IN SOURCE")
f1.close()

f2 = open(destination + "/test2.txt", 'w+')
f2.write("TEST 1 FILE IN DESTINATION")
f2.close()

# lets delete the practice file you created in the beginning
#os.unlink('practice.txt')

#list down everyhing in the path 
for each in os.walk(path):
    print(each)


import shutil
#shutil.move(source + "/test1.txt",destination)
shutil.move(destination + "/test1.txt",source)
