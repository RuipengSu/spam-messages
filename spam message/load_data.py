# coding=utf-8 
from numpy import *
import json
import csv

# 加载原始数据，进行分割
def load_message():
    content = []
    lines = []
    label = []

    with open('D:\Document\CS\Program\py program\spam messages\spam_train.txt', encoding = 'utf-8') as fr:
        for i in range(10000):
            line = fr.readline()
            lines.append(line)
        num_train = len(lines)
        for i in range(num_train):
            message = lines[i].split('\t')
            label.append(message[0])
            content.append(message[1])

    with open('D:\Document\CS\Program\py program\spam messages\spam_test.txt', encoding = 'utf-8') as fr:
        for i in range(100000):
            line = fr.readline()
            lines.append(line)
            content.append(line)
        num = len(lines)
    return num, content, label


# 将分割后的原始数据存到json
def data_storage(content, label):
    with open('D:\Document\CS\Program\py program\spam messages\spam_content.json', 'w') as f:
        json.dump(content, f)
    with open('D:\Document\CS\Program\py program\spam messages\spam_label.json', 'w') as f:
        json.dump(label, f)

if '__main__' == __name__:
   num, content, label = load_message()
   data_storage(content, label)
