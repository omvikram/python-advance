import requests
target_url = "https://www.messivsronaldo.app/"

result = requests.get(target_url)

print(type(result))

#print(result.text)

import bs4
soup = bs4.BeautifulSoup(result.text, "lxml")

#print(soup)
print(soup.select("title"))
print(soup.select("title")[0])
print(soup.select("title")[0].getText())
print(soup.select("h1"))
print(soup.select("h1")[0])
print(soup.select("h1")[0].getText())

print("Let's capture the all time images of Messi and Ronaldo")
images = soup.select("img")
print(images)
print(len(images))

# for each in images:
#     print(each["src"])

messi_image_src = images[3]["src"]
ronaldo_image_src = images[1]["src"]

print(messi_image_src)
print(ronaldo_image_src)

messi_image = requests.get(target_url + messi_image_src)
ronaldo_image = requests.get(target_url + ronaldo_image_src)

import os
os.mkdir("images")

# f1 = open("images/messi.png","wb")
# f1.write(messi_image.content)
# f1.close()

# f2 = open("images/ronaldo.png", "wb")
# f2.write(ronaldo_image.content)
# f2.close()

