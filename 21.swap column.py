import pandas as pd

data = {
    'Text': ['apple', 'Banana', 'Cherry', 'Date', 'Fig'],
}

df = pd.DataFrame(data)

column_name = 'Text'
df[column_name] = df[column_name].str.swapcase()

print(df)
