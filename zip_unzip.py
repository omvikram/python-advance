import zipfile
import os
import pdb
import shutil

path = os.getcwd()
print(path)

print("Create a new folder myzip") 
#path = path + "/myzip/"
#os.mkdir(path + "/myzip")

print("Create 2 files in a new folder myzip") 
# f1 = open(path + "file1.txt","w")
# f1.write("I am file1.txt")
# f1.close()

#pdb.set_trace()

# f2 = open(path + "file2.txt","w")
# f2.write("I am file2.txt")
# f2.close()

print("How to compress/extract the files using zipfile") 
# zz = zipfile.ZipFile(path+"myzip.zip", "w")
# zz.write(path+"file1.txt", compress_type=zipfile.ZIP_DEFLATED)
# zz.write(path+"file2.txt", compress_type=zipfile.ZIP_DEFLATED)
# zz.close()

#zzz = zipfile.ZipFile("unzip_me_for_instructions.zip","r")
#zzz.extractall("")
#print(zzz)


print("Using shutil to unzip the files")
# zip_file = shutil.make_archive("unzip_me", "zip", path)
# unzip_files = shutil.unpack_archive("unzip_me_for_instructions.txt", path, "zip")

f = open("extracted_content/Instructions.txt","r")
print(f.read())

import re
import time
print("Create a function for searching pattern of telephone number")
def search_mobile_number(file,pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

start_time = time.time()
print("Started search in {}".format(start_time))
results = []
for folder , sub_folders , files in os.walk(path+"/extracted_content"):
    
    for f in files:
        file_path = folder+'/'+f
        results.append(search_mobile_number(file_path))

end_time = time.time()
print("Started search in {}".format(end_time))
for r in results:
    if r != '':
        print(r.group())