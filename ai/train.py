import json
import pandas as pd
from model import train_model

with open("../data/logs.json") as f:
    logs = json.load(f)

df = pd.json_normalize(logs)
features = df.select_dtypes(include=['number']).fillna(0)

train_model(features)

print("AI model trained successfully")
