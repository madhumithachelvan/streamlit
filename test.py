import pandas as pd
import glob


# Define the path where your CSV files are stored
file_path = "/Users/hongyuchen/Desktop/GE/streamlit/data_pilot*.csv"  # Adjust accordingly

# Use glob to find all matching CSV files
csv_files = glob.glob(file_path)

# Read and merge all CSV files
df_list = [pd.read_csv(file) for file in csv_files]
merged_df = pd.concat(df_list, ignore_index=True)  # Merging all into one DataFrame

# Display the first few rows
print(merged_df.head())

def load_data():
    return pd.read_csv("sub_dataset_6.csv")


df = load_data()


combined = pd.concat([merged_df, df], axis=0, ignore_index=True)
# Optional: Save merged data to a new CSV file
combined.to_csv("combined.csv", index=False)
print(combined.info())


