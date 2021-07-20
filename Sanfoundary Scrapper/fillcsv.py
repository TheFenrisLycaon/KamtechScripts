import os
import pandas as pd
dirPath = './txts/'
dirs= ['python-questions']
for folder in dirs:
    path = dirPath + folder + '/'
    txtfiles = os.listdir(path)
    txtfiles = [x for x in txtfiles if '.txt' in x]

    q = []
    a = []
    b = []
    c = []
    d = []
    s = []
    currTXT = []
    
    for ff in txtfiles:
        
        with open(path+ff, 'r') as f:
            curTXT = f.readlines()
            curTXT = curTXT[:-6]
    
            currTXT += curTXT

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
            int(currTXT[i][0])
            if currTXT[i].split(' ')[0][-1] != '.':
                raise TypeError
            while currTXT[i][0:2] != 'a)':
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
                        f.write('\n')
                    elif currTXT[i][0] == 'b':
                        while currTXT[i][0] != 'c':
                            tb += currTXT[i]
                            if currTXT[i].lower() == 'b) true\n' or currTXT[i].lower() == 'b) false\n':
                                s.append(currTXT[i+1])
                                c.append('')
                                d.append('')
                                i += 2
                                break
                            i += 1
                        b.append(tb[3:])
                        f.write('\n')
                    elif currTXT[i][0] == 'c':
                        while currTXT[i][0] != 'd':
                            tc += currTXT[i]
                            i += 1
                        c.append(tc[3:])
                        f.write('\n')
                    elif currTXT[i][0] == 'd':
                        while currTXT[i][1:] != '\n':
                            td += currTXT[i]
                            i += 1
                        d.append(td[3:])
                        f.write('\n')
                    else:
                        exit()
                else:
                    if currTXT[i][1:] == '\n':
                        ts += currTXT[i]
                        f.write('\n')
                        s.append(ts)
                        i += 1
            except:
                pass

    df = pd.DataFrame(list(zip(q, a, b, c, d, s)),
                        columns=['Questions', 'opt1', 'opt2', 'opt3', 'opt4', 'Answers'])
    df = df.replace(r'\s', ' ', regex=True)
    df.to_csv(f'./Out/{folder}.csv', encoding='utf-8', index=False)
    print(f"Done with {folder}")
