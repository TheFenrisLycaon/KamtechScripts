import pandas as pd

q = []
a = []
b = []
c = []
d = []
s = []

for ff in ['txts/python-questions/python-mcqs-function-1.txt']:
    name = ff.split('/')[-1]
    with open(ff, 'r') as f:
        currTXT = f.readlines()
        currTXT = currTXT[:-6]

    # currTXT = [x.strip() for x in currTXT]
    # print(currTXT)

    with open(f'temp/{name}.txt', 'w') as f:
        for i in range(len(currTXT)):
            tq = ''
            ta = ''
            tb = ''
            tc = ''
            td = ''
            ts = ''
            try:
                int(currTXT[i][0])
                while currTXT[i][0] != 'a':
                    tq += currTXT[i]
                    f.write(currTXT[i])
                    i += 1
                    continue
                q.append(tq[3:])
                f.write('\n')
            except:
                try:
                    if currTXT[i][1] == ')':
                        if currTXT[i][0] == 'a':
                            while currTXT[i][0] != 'b':
                                ta += currTXT[i]
                                f.write(currTXT[i])
                                i += 1
                            a.append(ta[3:])
                            f.write('\n')
                        elif currTXT[i][0] == 'b':
                            while currTXT[i][0] != 'c':
                                tb += currTXT[i]
                                f.write(currTXT[i])
                                i += 1
                            b.append(tb[3:])
                            f.write('\n')
                        elif currTXT[i][0] == 'c':
                            while currTXT[i][0] != 'd':
                                tc += currTXT[i]
                                f.write(currTXT[i])
                                i += 1
                            c.append(tc[3:])
                            f.write('\n')
                        elif currTXT[i][0] == 'd':
                            while currTXT[i][1:] != '\n':
                                td += currTXT[i]
                                f.write(currTXT[i])
                                i += 1
                            d.append(td[3:])
                            f.write('\n')
                        else:
                            exit()
                    else:
                        if currTXT[i][1:] == '\n':
                            ts += currTXT[i]
                            f.write(currTXT[i])
                            f.write('\n')
                            s.append(ts)
                except:
                    pass
df = pd.DataFrame(list(zip(q, a, b, c, d, s)),
                  columns=['Questions', 'A', 'B', 'C', 'D', 'Answers'])
df = df.replace(r'\s', ' ', regex=True)
df.to_csv(f'./temp/k.csv', encoding='utf-8', index=False)
df.to_json(f'./temp/k.json')
print(len(a))
