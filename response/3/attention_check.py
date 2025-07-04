
import pandas as pd
import random
def load_data():
    return pd.read_csv("sub.csv")


df = load_data()

print(df.info())  # Shows column names, non-null counts, and data types


attention_check_rows = df[df['texts'].str.startswith("This is an attention check", na=False)]

# Display the filtered rows
print(attention_check_rows)

print(attention_check_rows.info())

attention_check_rows.to_csv("attention_checks3.csv", index=False)