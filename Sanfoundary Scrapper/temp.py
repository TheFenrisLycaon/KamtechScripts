import pandas as pd
import os
dirs = 'txts/sqlserver-mcqs/'
txtfile = os.listdir(dirs)
txtfile = [x for x in txtfile if '.txt' in x]
# print(txtfile)
currTXT = []
q = []
a = []
b = []
c = []
d = []
s = []
# txtfile = ['python-questions-answers-sets-4.txt']
for ff in txtfile:
    with open(dirs+ff, 'r') as f:
        curTXT = f.readlines()
        curTXT = curTXT[:-6]
    print(f'{ff}')
    currTXT += curTXT
    # print(curTXT)

for i in range(len(currTXT)):
    if currTXT[i] == 'Join Sanfoundry@YouTube':
        currTXT = currTXT[:i]+currTXT[i:]

for i in range(len(currTXT)):
    tq = ''
    ta = ''
    tb = ''
    tc = ''
    td = ''
    ts = ''
    try:
        int(currTXT[i].split('.')[0])
        if '\n' in currTXT[i].split('.')[0]:
            raise TypeError

        while currTXT[i][0] != 'a':
            tq += currTXT[i]
            i += 1
            continue
        q.append(tq[3:])
    except:
        try:
            if currTXT[i][1] == ')':
                if currTXT[i][0] == 'a':
                    while currTXT[i][0] != 'b':
                        ta += currTXT[i]
                        i += 1
                    a.append(ta[3:])
                elif currTXT[i][0] == 'b':
                    while currTXT[i][0] != 'c':
                        tb += currTXT[i]
                        if currTXT[i].lower()[-6:] == 'false\n':
                            if currTXT[i+1][:3] != 'c)':
                                s.append(currTXT[i+1])
                                c.append('')
                                d.append('')
                                i += 1
                                break
                            else:
                                tb = currTXT[i]
                        i += 1
                    b.append(tb[3:])
                elif currTXT[i][0] == 'c':
                    while currTXT[i][0] != 'd':
                        tc += currTXT[i]
                        i += 1
                    c.append(tc[3:])
                elif currTXT[i][0] == 'd':
                    while currTXT[i][1:] != '\n':
                        td += currTXT[i]
                        i += 1
                    d.append(td[3:])
                else:
                    exit()
            else:
                if currTXT[i][1:] == '\n':
                    ts += currTXT[i]
                    s.append(ts)
                    i += 1
        except:
            pass
    

df = pd.DataFrame(list(zip(q, a, b, c, d, s)),
                columns=['Questions', 'opt1', 'opt2', 'opt3', 'opt4', 'Answers'])
df = df.replace(r'\s', ' ', regex=True)
df.to_csv(f'./temp/{ff}1.csv', encoding='utf-8', index=False)
