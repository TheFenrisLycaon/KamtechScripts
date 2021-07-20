from bs4 import BeautifulSoup

data = open('/home/fenris/work/Internshit/Kamtech/out/Bike Rental System.html','r')
soup = BeautifulSoup(data, 'lxml')
inner_ul = soup.find_all('ul')
lists = {}
for ultag in soup.find_all('ul'):
    temp = []
    for litag in ultag.find_all('li'):
        temp.append(litag.text.split)
    lists[ultag.text] = temp

print(lists)
