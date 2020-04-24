from credentials import *
import move

try:#気にしないで
    from credentials_secret import *
except:
    pass

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os,random,string,csv,time

def MarkURL(url):
    with open ('urls.txt','a') as f:
        f.write(url+'\n')

def WaitUntilPageChange():
    while True: 
        with open ('urls.txt','r') as f:
            previous_url=f.readlines()[-1].strip()
        new_url=driver.current_url
        if previous_url!=new_url:
            MarkURL(new_url)
            time.sleep(5) #URLが変わっているが画面が数秒遷移しないことがあるので念のため。
            return new_url
        else:
            time.sleep(5)


def FolderExplorer(path):
    url=WaitUntilPageChange()#クリックしてから遷移までに時間がかかるので、URLが変わるまで待つ
    try:
        WebDriverWait(driver,wait_limit).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.contentsListTable tr .fa-2x')))
    except:#待ってもコンテンツが現れない→フォルダがから→return
        return
    
    
    folders_length=len(driver.find_elements_by_css_selector('.fa-2x.fa-folder'))
    files_length=len(driver.find_elements_by_css_selector('.fa-2x.fa-file-pdf-o'))+len(driver.find_elements_by_css_selector('.fa-2x.fa-file-video-o'))
    
    for i in range(files_length):
        driver.get(url)
        MarkURL(url)
        WebDriverWait(driver,wait_limit).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fa-2x.fa-file-pdf-o,.fa-2x.fa-file-video-o')))
        elm=(driver.find_elements_by_css_selector('.fa-2x.fa-file-pdf-o')+driver.find_elements_by_css_selector('.fa-2x.fa-file-video-o'))[i]
        name=driver.find_elements_by_class_name('td-fileName')[i].text.replace('/','-')
        
        if path+name not in already_downloaded:
            elm.click()
            FileDownload(path)

    for i in range(folders_length):
        driver.get(url)
        MarkURL(url)
        WebDriverWait(driver,wait_limit).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fa-2x.fa-folder')))
        elm=driver.find_elements_by_css_selector('.fa-2x.fa-folder')[i]
        dirname=driver.find_elements_by_class_name('td-fileName')[i+files_length].text.replace('/','-')#ファイル→フォルダの順に並んでいるため
        elm.click()
        FolderExplorer(path+dirname+'/')


def FileDownload(path):
    while True:
        url=driver.current_url
        with open ('urls.txt','r') as f:
            if f.readlines()[-1].strip()!=url:
                time.sleep(5)
                break
            else:
                time.sleep(5)

    with open ('urls.txt','a') as f:
        f.write(url+'\n')

    WebDriverWait(driver, wait_limit).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-ng-click="entryDetailVm.showDownloadModal()"]')))
    driver.find_elements_by_css_selector('button[data-ng-click="entryDetailVm.showDownloadModal()"]')[0].click()
    WebDriverWait(driver, wait_limit).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-ng-click="download()"]')))
    driver.find_elements_by_css_selector('button[data-ng-click="download()"]')[0].click()
    name=driver.find_element_by_tag_name('h2').text.replace('/','-')
    filename=''.join([random.choice(string.ascii_letters) for i in range(15)])
    time.sleep(5)

    while True:#ダウンロードが終わるまで待つ
        try:
            os.rename(default_download_dir+name,default_download_dir+filename)#重複を避けるためファイル名はランダムに
            break
        except FileNotFoundError:
            time.sleep(10)

    with open ('path.csv','a',encoding='utf-8_sig') as f:
        f.write(filename+','+path+name+'\n')


def main():
    driver.get('https://auth.classi.jp/students')
    
    id_input = driver.find_element_by_id('classi_id')
    pw_input = driver.find_element_by_id('password')
    id_input.send_keys(user_id)
    pw_input.send_keys(password)
    pw_input.submit()
    
    driver.get('https://platform.classi.jp/contentsbox#/directories/7efd1f36d30b806dd626b7f0844c949a8c5a953c?page=1&sort=shared_at&direction=desc&area=2&content_category=2')
    
    FolderExplorer('')

    
if __name__ == '__main__':
    exe_path=exe_dir+'\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=exe_path)
    wait_limit=15 #コンテンツが無いことを判断するまでの待機時間

    already_downloaded=[] #すでにダウンロード済みのものはスキップしたい。
    with open ('path_backup.csv','r',encoding='utf-8_sig') as f:
        for line in csv.reader(f):
            if len(line)==2:
                key,val=line
                already_downloaded.append(val)
            else:
                print('k')
    with open ('urls.txt','a') as f:
        f.write('----\n')
    with open ('path.csv','w',encoding='utf-8_sig') as f:
        pass

    main()
    move.main()
    
