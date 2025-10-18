"""
Coding Challenge
Create a DataFrame from this dict:

python
data = {'Name': ['Ram', 'Sita', 'Lakshman'],
        'Marks': [88, 92, 85],
        'Subject': ['Math', 'Science', 'Math']}
Print the first 2 rows.

Print only the 'Name' and 'Marks' columns.

Filter rows where 'Marks' is greater than 85 and print those rows.
"""

import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Name': ['Ram', 'Sita', 'Lakshman'],
    'Marks': [88, 92, 85],
    'Subject': ['Math', 'Science', 'Math']
}
df = pd.DataFrame(data)

# Step 2: Print the first 2 rows
print("First 2 rows:")
print(df.head(2))

# Step 3: Print only 'Name' and 'Marks' columns
print("\nName and Marks columns:")
print(df[['Name', 'Marks']])

# Step 4: Filter rows where 'Marks' > 85
print("\nRows where Marks > 85:")
print(df[df['Marks'] > 85])
