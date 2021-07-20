import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

url = 'https://www.sanfoundry.com/java-mcqs-integer-floating-data-types/'
flag = 1
count = 0

questions = []
answers = []
opt1 = []
opt2 = []
opt3 = []
opt4 = []

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
            
            with open(".temp", "w") as f:
                f.writelines('\n'.join(filtered))
                f.write('\n')
            
            with open('.temp', 'r') as currFile:
                # print(currFile.readlines())
                filtered = currFile.readlines()
                filtered = filtered[:-6]

            for i in range(len(filtered)):
                try:
                    int(filtered[i][0])
                    if filtered[i][1] == '.' or filtered[i][2] == '.':
                        q = [filtered[i][3:]]
                        if 'output' in filtered[i] and 'following' in filtered[i]:
                            while 'a)' not in filtered[i]:
                                q.append(filtered[i+1])
                                i += 1
                        questions.append(
                            '\n'.join(q[:-1])) if len(q) > 1 else questions.append('\n'.join(q))
                except Exception:
                    if filtered[i][0].lower() in ['a', 'b', 'c', 'd']:
                        if filtered[i][1:] == '\n':
                            answers.append(filtered[i])
                        else:
                            if filtered[i][0] == 'a':
                                try:
                                    opt1.append(filtered[i][3:])
                                    if 'true' in filtered[i].lower():
                                        opt2.append('False')
                                        opt3.append('')
                                        opt4.append('')
                                        i += 1
                                        continue
                                    opt2.append(filtered[i+1][3:])
                                    opt3.append(filtered[i+2][3:])
                                    opt4.append(filtered[i+3][3:])
                                    i += 3
                                except Exception as e:
                                    print(e)

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

df = pd.DataFrame(list(zip(questions, opt1, opt2, opt3, opt4, answers)),
                  columns=['Questions', 'A', 'B', 'C', 'D', 'Answers'])

df.to_csv('java_main.csv', encoding='utf-8')
