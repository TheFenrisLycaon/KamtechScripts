import requests
from bs4 import BeautifulSoup

url = "https://www.sanfoundry.com//"
urls = []
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
g_data = soup.find_all("div", {"class": "entry-content"})
for i in g_data:
    topics = i.text.split('\n')
    topics = [x for x in topics[2:-15]
                if  x != '']
    topics = [x for x in topics
                if '1000' in x]
    topics = [x for x in topics
                if 'MCQ' in x]
    topics = [x for x in topics
              if 'Class' not in x]


# print('\n'.join(topics))

# print(soup)
for tag in soup.find_all("div", {"class": "front-page"}):
    urls = tag.find_all('a')
urldict = {}
for i in urls:
    if i.text in topics:
        urldict[i.text[5:]] = i.get('href')

for i in urldict:
    r = requests.get(urldict[i])
    soup = BeautifulSoup(r.content, 'lxml')
    x =[]
    div = soup.find_all('div', {'class': 'sf-section'})
    # print(div)
    for tag in div:
        linktag = tag.find('a')
        if linktag != None:
            link = linktag['href']
            if link:
                x.append(link)
    
    linkList = [i for i in x if '1000' not in x[0]]
    # linkList = [i for i in linkList if i]
    with open('links.txt', 'a') as f: 
        if linkList:
            f.writelines(linkList[0])
            f.writelines('\n')
