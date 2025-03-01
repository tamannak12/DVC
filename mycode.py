import pandas as pd 
import os

data={'Name':['Sam','Bob','Charlie'],
      'Age':[25,30,35],
      'City':['NYC','LA','Chicago']
      }

df=pd.DataFrame(data)
#Adding new row to df for v2
#new_row_loc={'Name':'V2','Age':30, 'City':'City1'}
#df.loc[len(df.index)]=new_row_loc

##adding new row to df for v3
#new_row_loc2={'Name';'V3','Age':30,'City':'City1'}
#df.loc[len(df.index)]=new_row_loc2

#Ensure the "data directory exists at the root level
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#define file path
file_path=os.path.join(data_dir,'sample_data.csv')

#save the dataframe to csv file
df.to_csv(file_path,index=False)

print(f"csv fle saved to {file_path}")