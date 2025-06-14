import glob
import pandas as pd
import os

responses_dir = 'responses_2'
count = 0

for i,folder in enumerate(os.listdir(responses_dir)):
    if folder not in ['.DS_Store', 'merged.py', 'merged']:

        folder_path = os.path.join(responses_dir,folder)
        if len(os.listdir(folder_path)) == 0:
            continue

        # Find all CSV files starting with "survey_responses"
        if folder == 'demographic':
            file_list = glob.glob("prolific_export*.csv",root_dir=folder_path)
        else:
            file_list = glob.glob("survey_responses*.csv",root_dir=folder_path)
        file_list = [os.path.join(folder_path,file) for file in file_list]
        file_list.sort()  # Optional: sort the list

        # Read each CSV file into a DataFrame and concatenate them
        dataframes = [pd.read_csv(f) for f in file_list]
        merged_df = pd.concat(dataframes, ignore_index=True)

        # Write the merged DataFrame to a new CSV file
        if folder == 'demographic':
            merge_name = os.path.join(responses_dir,f"merged/merged_demographics.csv")
        else:
            merge_name = os.path.join(responses_dir,f"merged/merged_pilot{folder}_responses.csv")

        merged_df.to_csv(merge_name, index=False)
        count += 1  # Keeps count of response folders





