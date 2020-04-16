from credentials import *
import shutil
import os
import csv
def main():
    with open ('path_backup.csv','r',encoding='utf-8_sig') as f:
        current_backup=f.read()
    with open ('path.csv','r',encoding='utf-8_sig') as f:
        new_backup=f.read()
    
    with open ('path_backup.csv','w',encoding='utf-8_sig') as f:
        f.write(current_backup+'\n'+new_backup)

    with open ('path.csv','r',encoding='utf-8_sig') as f:
        for name,path in csv.reader(f):
            dir_path='contents/'
            for d in path.split('/')[:-1]:
                if d not in [x.strip() for x in os.listdir(dir_path)]:
                    os.mkdir(dir_path+d+'/')
                dir_path+=d+'/'
            
            if name not in [x.strip() for x in os.listdir(dir_path)]:
                shutil.copy(default_download_dir+name, 'contents/new/'+path.split('/')[-1])

            shutil.move(default_download_dir+name, 'contents/'+path)

if __name__ == '__main__':
    main()