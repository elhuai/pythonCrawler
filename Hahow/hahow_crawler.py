import requests
import json
import pandas as pd

url = "https://api.hahow.in/api/products/search?category=COURSE&groups=programming&limit=8&mixedResults=false&page=0&sort=TRENDING"
headers_data = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

response  = requests.get(url, headers=headers_data)
if response.status_code == 200:
    data = response.json()
    products = data["data"]["courseData"]["products"]
    courses_list = []
    for product in products:
        singal_course = [
            product["title"],
            product["metaDescription"],
            product["price"],
            product["averageRating"],
            product["numRating"],
            product["owner"]["name"]
        ]
        courses_list.append(singal_course)
        
    # 將資料轉換為 DataFrame
    df = pd.DataFrame(courses_list, columns=["title", "metaDescription", "price", "averageRating", "numRating", "ownerName"])
    # 將資料寫入 Excel 檔案 
    df.to_excel("hahow_courses.xlsx", index=False, engine="openpyxl") # 將資料寫入 Excel 檔案
else:
    print(f"Error: {response.status_code}")


with open("hahow_courses.json", "w", encoding="utf-8") as f:
     json.dump(courses_list, f, ensure_ascii=False, indent=4) # 將資料寫入檔案