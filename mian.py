import requests
from bs4 import BeautifulSoup

url = "https://thetechnicalera.000webhostapp.com/home.html"

r = requests.get(url)
# GETTING DATA
htmlcontent = r.content
# print(htmlcontent)

# PARSING DATA -  in html format

soup = BeautifulSoup(htmlcontent, 'html.parser')

# print(soup)
# print(soup.prettify)

# TRAVERSING HTML TREE

title = soup.title

# print(title)
# print(type(title))


# Commonly used types if object in bs4
    # -> Tag
    # -> NavigableString
    # -> BeautifulSoup
    # -> Comment

paras = soup.find_all('p')
# print(paras)

first_para = soup.find('p')
# print(first_para)

first_para_class = soup.find('p')['class']
# print(first_para_class)

# Find all the elements with a specific class 

get_a_class = soup.find_all('p', class_='lead')
# print(get_a_class)

all_text = soup.get_text()
# print(all_text)

anchors = soup.find_all('a')
# print(anchors)

all_links = set()

for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://thetechnicalera.000webhostapp.com/home.html/" + link.get('href')
        all_links.add(link)
        # print(linkText)

# COMMENT OBJECT

markup = "<p><!-- This is a comment --></p>"
soup2 = BeautifulSoup(markup, features="html5lib")

# print(soup2.p.string)
# print(type(soup2.p.string))

navPlay = soup.find(id="navbarMenu")

# Method - 1
for ele in navPlay.contents:
    # print(ele)
    pass

# Method - 2
for ele in navPlay.children:
    # print(ele)
    pass

for item in navPlay.strings:
    # print(item)
    pass

for item in navPlay.stripped_strings:
    # print(item)
    pass

# print(navPlay.parent)
# print(navPlay.parents)

for item in navPlay.parents:
    # print(item)
    # print(item.name)
    pass

# To get element of a specific id or class

# we get a list if there are multiple elements
element = soup.select('.jumbotron')
# print(element)