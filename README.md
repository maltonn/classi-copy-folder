# Classi copy-folders

Classiの共有フォルダをローカルにコピーするpythonスクリプトです

# 準備
1. chromedriveとseleniumのインストールが必要です

    ```
    pip install chromedriver-binary
    pip install selenium
    chromedriver-path 
    ```

    最後に```c:\users\user\appdata\local\programs\python\python36\lib\site-packages\chromedriver_binary```
    のような文字列が出力されるはずなので、 credentials.py の ```exe_dir=r"xx\xx\xx"``` のxx\xx\xx部分を書き換えます

2. credentials.py の ```uer_id='xxxx'``` と ```passward='xxxx'``` の部分を自分のものに書き換えます


# 実行
```
python main.py
```
数分かかる場合があります。コーヒーでも飲みながら気長に待ちましょう


# エラーが出たら
## SessionNotCreatedException
```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version ~~
```
chromeのバージョンとdriverのバージョンを合わせる必要があります。
chromeをアップデートすると治る場合が多いです。


## WebDriverException
```
selenium.common.exceptions.WebDriverException: Message: 'chromedriver.exe' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```
chromedriverが正常にインストールできていません。
credentials.py の```exe_dir=r'xx\xx\xx'```のところが正常に書き換わっているか確認してください。※```exe_dir=r'c:\users\user\appdata\local\programs\python\python36\lib\site-packages\chromedriver_binary'```のようになるのが正解です。

# 注意
pdfと動画のみ対応です。それ以外への対応は```.fa-2x.fa-file-pdf-o,.fa-2x.fa-file-video-o```あたりを変更することで可能です
