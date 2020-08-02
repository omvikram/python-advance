base_url = "http://quotes.toscrape.com/"
page_url = "http://quotes.toscrape.com/page/{}"

# Need to find all the authors of the quoets listed in the target website

# loop through all the pages in the website unless the page is 404

# loop through each div element with class "quote"

# check for the class "author" and get the text, store in the list
import requests
import bs4

authors_list = []
next_page = True
n = 1

while next_page:
    if(n>1):
        try:
            res = requests.get(page_url.format(n))
            soup = bs4.BeautifulSoup(res.content, "lxml")
            for each in quotes_list:
                authors_list.append(each.select(".author")[0].getText()) 
            n= n+1
        except:
            next_page = False
            break
    else:
        res = requests.get(base_url)
        soup = bs4.BeautifulSoup(res.content, "lxml")
        quotes_list = soup.select(".quote")
        for each in quotes_list:
            authors_list.append(each.select(".author")[0].getText()) 
        n= n+1

print("Number of pages = {}".format(n))
print(len(authors_list))

for author in authors_list:
    print(authors_list)

