import json
import pandas as pd

with open("ratings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []
for entry in data:
    timestamp = entry["timestamp"]
    for idx, scores in enumerate(entry["ratings"]):
        rows.append({
            "Timestamp": timestamp,
            "ImageID": idx + 1,
            "Q1": scores[0],
            "Q2": scores[1],
            "Q3": scores[2],
            "Q4": scores[3]
        })

df = pd.DataFrame(rows)
df.to_csv("ratings.csv", index=False, encoding="utf-8-sig")
