import pandas as pd
import glob


# Define the path where your CSV files are stored
file_path = "/Users/hongyuchen/Desktop/GE/streamlit/survey_responses_*.csv"  # Adjust accordingly

# Use glob to find all matching CSV files
csv_files = glob.glob(file_path)

# Read and merge all CSV files
df_list = [pd.read_csv(file) for file in csv_files]
merged_df = pd.concat(df_list, ignore_index=True)  # Merging all into one DataFrame

# Display the first few rows
print(merged_df.head())

# Optional: Save merged data to a new CSV file
merged_df.to_csv("merged_survey_responses.csv", index=False)
