import requests
import time
import pandas as pd

url = "https://www.cpbl.com.tw/box/index?gameSno=1&year=2024&kindCode=A"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=headers)

print(response.status_code)
# print(len(response.text))
# print(response.text[:1000])

data = []

year = 2024

for game_sno in range(1, 361):

    url = (
        f"https://www.cpbl.com.tw/box/index"
        f"?gameSno={game_sno}&year={year}&kindCode=A"
    )

    response = requests.get(url, headers=headers)

    print(year, game_sno, response.status_code)

    if response.status_code == 200:

        data.append({
            "year": year,
            "game_sno": game_sno,
            "url": url
        })

    # time.sleep(0.5)

df = pd.DataFrame(data)

display(df.head())