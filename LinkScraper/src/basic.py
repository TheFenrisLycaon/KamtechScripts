from bs4 import BeautifulSoup, SoupStrainer
import requests
html = open('./test.html', 'r')
for link in BeautifulSoup(html, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        page = requests.get(link['href'])
        soup = BeautifulSoup(page.content, 'lxml')
        name = str(soup.find_all('h1')[0])[4:-5]
        div = soup.find('div', {'class': "field-item even", 'property': "schema:description content:encoded"})
        with open(f'out/{name}.html', 'w') as f:
            f.writelines(str(div))
        f.close()
