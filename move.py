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
        f.write(current_backup+new_backup)

    with open ('path.csv','r',encoding='utf-8_sig') as f:
        for line in csv.reader(f):
            try:
               filename,path=line
            except:
                print('no data in line')
                continue
            
            dir_path='C:/Users/user/OneDrive/Classi/'
            for d in path.split('/')[:-1]:
                if d not in [x.strip() for x in os.listdir(dir_path)]:
                    os.mkdir(dir_path+d+'/')
                dir_path+=d+'/'
            name=path.split('/')[-1]
            if name not in [x.strip() for x in os.listdir(dir_path)]:
                shutil.copy(default_download_dir+filename,'C:/Users/user/OneDrive/Classi/new/'+name)
            
            shutil.move(default_download_dir+filename,dir_path+name)
    
    with open ('path.csv','w') as _:
        pass

if __name__ == '__main__':
    main()