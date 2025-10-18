"""
Start with this DataFrame:

python
data = {'Name': ['Ram', 'Sita', 'Lakshman', None], 'Marks': [88, 92, None, 75], 'Subject': ['Math', 'Science', 'Math', None]}
df = pd.DataFrame(data)
Detect and print rows with missing data.

Fill missing 'Name' with "Unknown".

Drop rows missing 'Marks'.

Convert 'Marks' to float.

Group data by 'Subject' and compute average marks (ignore missing groups).
"""

import pandas as pd

data = {
    'Name': ['Ram','Sita','Lakshman',None],
    'Marks': [88,92,None,75],
    'Subject': ['Math','Science','Math',None]
}
df = pd.DataFrame(data)

print(df[df.isnull().any(axis=1)])

df['Name'].fillna('None',inplace=True)

df.dropna(subset=['Marks'],inplace=True)

df['Marks'] = df['Marks'].astype(float)

grouped = df.dropna(subset=['Subject']).groupby('Subject')['Marks'].mean()

print(grouped)