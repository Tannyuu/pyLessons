import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

load_url=https:http://www.higashiyama.city.nagoya.jp/04_zoo/friend/2018/02/post-21.html
res=requests.get(load_url)
res.encoding=res.apparent_encoding
soup=BeautifulSoup(res.text,'html.parser')

#フォルダ作成
out_folder=Path('downloaded_higasiyama')
out_folder.mkdir(exist_ok=True)

#img要素を全部取得
imgs=soup.select('img')

for img in imgs:
    src=img.get('src')

    #相対パスを絶対パスに変更
    img_url=urllib.parse.urljoin(load_url,src)

    #画像ロード
    loaded_img=requests.get(img_url)

    #ファイル名取得
    file_name=img.get('src').

    #保存画像パス
    out_path=out_folder.joinpath(file_name)

    with open(out_path,"wb") as file:
        file.write(loaded_img.content)

    time.sleep(1)
