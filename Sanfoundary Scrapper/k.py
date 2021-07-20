import os
import pandas as pd


for ff in ['txts/php-questions/php-coding-questions-answers-arrays-1.txt']:
    # for ff in path:
    questions = []
    opt1 = []
    opt2 = []
    opt3 = []
    opt4 = []
    answers = []
    with open(ff, 'r') as currFile:
        currTXT = currFile.readlines()
        currTXT = currTXT[:-6]
        # currTXT += currTXT

    for i in range(len(currTXT)):
        if currTXT[i] == 'Join Sanfoundry@YouTube':
            currTXT = currTXT[:i]+currTXT[i:]

    currTXT = currTXT
    for i in range(len(currTXT)):
        pass
