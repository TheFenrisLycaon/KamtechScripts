import requests
from bs4 import BeautifulSoup
import os

with open('links.txt', 'r') as f:
    urls = f.readlines()

for url in urls:
# url = 'https://www.sanfoundry.com/java-mcqs-integer-floating-data-types/'

    flag = 1
    count = 0

    topicName = '-'.join(url.split('/')[3].split('-')[0:2])

    os.makedirs(os.path.join('Task3/', topicName), exist_ok = True)

    while flag:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'lxml')
            g_data = soup.find_all("div", {"class": "entry-content"})
            for i in g_data:
                filtered = i.text.split('\n')
                filtered = [x for x in filtered[2:]
                            if 'Explanation:' not in x]
                filtered = [x for x in filtered
                            if 'advertisement' not in x]
                filtered = [x for x in filtered
                            if x != '']
                for x in range(len(filtered)):
                    if 'View Answer' in filtered[x]:
                        filtered[x] = filtered[x][-1]

                with open(f"./Task3/{topicName}/{url.split('/')[-2]}.txt", "w") as f:
                    f.writelines('\n'.join(filtered))
                    f.write('\n')
                count += 1
                print(f"{count}:  Success    {url}")
                try:
                    div = soup.find_all('div', attrs={'class': 'sf-nav-bottom'})
                    for tag in div:
                        atag = tag.find('a')
                    url = atag.get("href")
                except Exception as e:
                    flag = 0
                    break
                if url == None:
                    break

        except Exception as e:
            flag = 0
            print(e)
