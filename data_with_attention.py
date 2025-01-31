

import pandas as pd
import random
def load_data():
    return pd.read_csv("data_pilot2.csv")

df = load_data()

random_rows = {
    "id": [f"{i+1}" for i in range(3)],
    "texts": [
        f"This is an attention check. {instruction}"
        for instruction in [
            "Please select 'Somewhat Feminine (2)' and '4: Very Confident. You were very certain about your judgment with no hesitation'",
            "Please select 'Neutral (3)' and '4: Very Confident. You were very certain about your judgment with no hesitation'",
            "Please select 'Very Masculine (5)' and '4: Very Confident. You were very certain about your judgment with no hesitation'"
        ]
    ],
    "is_attention_check": [True for _ in range(3)],
    "expected_answer": [2, 3, 5]
}

random_df = pd.DataFrame(random_rows)

indices = [9, 18, 26]

combined_df = pd.DataFrame(columns=df.columns)

# Insert rows at the correct positions
current_index = 0
random_row_index = 0
for i in range(len(df) + len(random_df)):
    if random_row_index < len(indices) and i == indices[random_row_index]:
        # Insert a random row
        combined_df = pd.concat([combined_df, random_df.iloc[[random_row_index]]], ignore_index=True)
        random_row_index += 1
    else:
        # Insert the next original row
        combined_df = pd.concat([combined_df, df.iloc[[current_index]]], ignore_index=True)
        current_index += 1

# Save the updated DataFrame to a CSV file
output_file = "data_pilot2_attention.csv"
combined_df.to_csv(output_file, index=False)  # Set index=False to avoid saving row indices to the CSV

print(f"Updated dataset saved to {output_file}")
print(combined_df)

