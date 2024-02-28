import pandas as pd


data = {
    'Text': ['apple', 'banana', 'cherry', 'date', 'fig'],
}

df = pd.DataFrame(data)

substring = 'ban'

index_list = df[df['Text'].str.find(substring) != -1].index

print("Indices of rows where the substring '{}' is found:".format(substring))
for index in index_list:
    print(index)
