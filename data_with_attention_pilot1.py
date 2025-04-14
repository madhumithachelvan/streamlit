

import pandas as pd
import random
def load_data():
    return pd.read_csv("dataset/data_pilot3.csv")

df = load_data()

random_rows = {
    "id": [f"{i+1}" for i in range(3)],
    "short_text": [
        f"This is an attention check. {instruction}"
        for instruction in [
            "Please select 'Somewhat Feminine (2)' and '4: Very Confident. You were very certain about your judgment with no hesitation'",
            "Please select 'Neutral (3)' and '2: Somewhat Confident. You made a judgment but still felt uncertain or had significant doubts'",
            "Please select 'Very Masculine (5)' and '1: Not Confident. You were unsure or found the text ambiguous'"
        ]
    ],
    "is_attention_check": [True for _ in range(3)],
    "expected_answer": [24, 32, 51]
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
output_file = "data_pilot3_attention.csv"
combined_df.to_csv(output_file, index=False)  # Set index=False to avoid saving row indices to the CSV

print(f"Updated dataset saved to {output_file}")
print(combined_df)

