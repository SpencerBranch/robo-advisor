# import pandas as pd
# # Create a dataframe from csv
# df = pd.read_csv('tickers.csv', delimiter='\n')
# print(df.head())

import csv
results = []
with open('nyse-listed_csv', 'r') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row)
# print(results)
split = results[0][0].split("\n")
print(type(split))
print(len(split))

