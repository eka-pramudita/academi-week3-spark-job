import os.path
import pandas as pd

fileList = []
path = 'dataset'
for filenames in os.walk(path):
    fileList.append(filenames)

for i in range(len(filenames[2])):
    a = 26 + i
    data = pd.read_json('dataset/' + filenames[2][i], encoding='utf-8', lines=True)
    data['flight_date'] = '2021-04-' + str(a)
    data.to_csv("./output/2021-04-"+ str(a+1) +".csv", index=False, header=True)