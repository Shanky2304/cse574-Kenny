import pandas as pd
import numpy as np
import simpledorff as sdf
import sys

first_arg = sys.argv[1]
# print(first_arg)

data = pd.read_csv(first_arg)

df = pd.DataFrame(data=data[['annotator_1', 'annotator_2', 'annotator_3']])
df = df.fillna(value=2)
agreed = 0
rows, cols= df.shape
for idx, row in df.iterrows():
    if row['annotator_1'] == 2:
        if row['annotator_2'] == row['annotator_3']:
            agreed += 1
        
    elif row['annotator_2'] == 2:
        if row['annotator_1'] == row['annotator_3']:
            agreed += 1
        
    elif row['annotator_3'] == 2:
        if row['annotator_1'] == row['annotator_2']: 
            agreed += 1
            

percent_agreement = agreed/rows 

data = data.melt(id_vars=['tweet_ID'], var_name='annotators', value_vars=['annotator_1', 'annotator_2', 'annotator_3'], value_name='annotation')

agreement = sdf.calculate_krippendorffs_alpha_for_df(data, experiment_col='tweet_ID', annotator_col='annotators', class_col='annotation')

print(agreement,'\t', percent_agreement)

