import pandas as pd

vix = pd.read_csv("/Users/jinyoochan/Desktop/nlp/vix.csv")

print(vix.iloc[0,0].split("\t")[0])

print(vix.iloc[0,0].split("\t")[1])

