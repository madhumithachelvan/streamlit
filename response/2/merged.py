import glob
import pandas as pd

# Find all CSV files starting with "survey_responses"
file_list = glob.glob("survey_responses*.csv")
file_list.sort()  # Optional: sort the list

# Read each CSV file into a DataFrame and concatenate them
dataframes = [pd.read_csv(f) for f in file_list]
merged_df = pd.concat(dataframes, ignore_index=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv("merged_pilot2_responses.csv", index=False)




