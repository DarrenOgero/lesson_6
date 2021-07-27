import csv
import pandas as pd

with open('nginx_logs.csv', 'r')as f:
    data = csv.reader(f)

    # for line in data:
    #     print(line)

df = pd.read_csv('nginx_logs.csv')
print(df.head())