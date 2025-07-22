import pandas as pd
import random

filename = "/Users/madhumitha/uni-stuttgart/IRIS_HiWi_materials/my_streamlit/aggregated.csv"

agg = pd.read_csv(filename,header=0)
print(agg.info())

batch = {9: [], 10: [], 11: [], 12: [], 13: []}
for id,row in agg.iterrows():
    p_id, round, mss = row
    if 9 <= round <= 13:
        batch[round].append(p_id)
        # batch.append([p_id,round,mss])

selected = []
for round in batch:
    selected.extend(random.sample(batch[round],k=6))

print(','.join(selected))
print(f'length of selected{len(selected)}')

