import json

data = {"name": " 배영모", "birth": "0723", "age":28}

with open("myinfo2.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)