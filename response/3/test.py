
import pandas as pd

def load_data():
    return pd.read_csv("merged_pilot3_responses.csv")


df = load_data()

print(df.info())