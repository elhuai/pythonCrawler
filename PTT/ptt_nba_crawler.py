import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.ptt.cc/bbs/Stock/index.html"
headers_data = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

response  = requests.get(url, headers=headers_data)
soup = BeautifulSoup(response.text, "html.parser") #用 html 的解析器 分析 response.text
articles = soup.find_all("div", class_="r-ent") # 找到所有 class 為 r-ent 的 div 標籤
title_data =[]
day_data =[]
popularity_data = []

all_data = []
for a in articles:

    # 整理每篇文章的資料
    singal_article = {}

    # 取出每篇文章的標題
    title = a.find("div", class_="title")
    title_a = title.find("a") 
    if title_a: # 如果有 a 標籤
        title = title.a.text.strip() # 取出標題
        singal_article["title"] = title
    else:
        singal_article["title"] = None


    # 取出每篇文章的日期
    day = a.find("div", class_="date")
    if day: # 如果有日期
        day = day.text.strip() # 取出日期
        singal_article["day"] = day
    else:
        singal_article["day"] = None

    # 取出每篇文章的熱門程度
    popularity = a.find("div", class_="nrec") #<div class="nrec"><span>爆</span></div>
    if popularity and popularity.span: 
        popularity = popularity.span.text.strip() # 取出熱門程度 #寫strip()是因為有空格
        singal_article["popularity"] = popularity
    else:
        singal_article["popularity"] = None
    all_data.append(singal_article) # 將每篇文章的資料加入列表

print(all_data) # 印出所有資料

# with open("ptt_data.json", "w", encoding="utf-8") as f:
#     json.dump(all_data, f, ensure_ascii=False, indent=4) # 將資料寫入檔案

df = pd.DataFrame(all_data) # 將資料轉換為 DataFrame
df.to_excel("ptt_data.xlsx", index=False,engine="openpyxl") # 將資料寫入 Excel 檔案
