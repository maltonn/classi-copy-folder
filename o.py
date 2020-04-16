import os
import csv
dic={}
with open ('path_backup.csv','r',encoding='utf-8_sig') as f:
    for key,val in csv.reader(f):
        dic[key]=val.split('/')[-1]

dir_path='contents/new/'
for filename in [x.strip() for x in os.listdir(dir_path)]:
    os.rename(dir_path+filename,dir_path+dic[filename]) 