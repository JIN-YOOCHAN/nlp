import pandas as pd
import googletrans

df = pd.read_csv("/Users/jinyoochan/Desktop/nlp/news_title_labeling.csv")
df = df.drop(['Unnamed: 0'], axis=1)

translator = googletrans.Translator()
df["news_title_english"] = 0

a = 0
while a < 90000:
  for i in range(a, a+100):
      try:
        result1 = translator.translate(df.iloc[i,0], dest='en')
        df.iloc[i,1] = result1.text
        a=i+1
        print(i)
      except:
        a=i

df.to_csv("/Users/jinyoochan/Desktop/nlp/news_title_labeling_translated.csv")
