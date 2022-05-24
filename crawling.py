from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


#2005~2022년까지 주요 뉴스 타이틀 데이터 수집

def crawling_total():

  chrome_options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


  headers = "news_title"
  year = [i for i in range(2006,2023)]
  month = [i for i in range(1, 13)]
  day = [i for i in range(1,32)]

  total_list = []

  for y in year:
    for m in month:
      for d in day:
        try:
          driver.get(f"https://finance.naver.com/news/mainnews.naver?date={y}-{m}-{d}")
          driver.maximize_window()
          time.sleep(1)
          html = driver.page_source
          soup = BeautifulSoup(html, "html.parser")

          for i in range(1,21):
            news_title = soup.select(f"#contentarea_left > div.mainNewsList > ul > li:nth-child({i}) > dl > dt > a")[0].text
            if news_title == "":
              news_title = soup.select(f"#contentarea_left > div.mainNewsList > ul > li:nth-child({i}) > dl > dd.articleSubject > a")[0].text
            else:
              pass
            total_list.append(news_title)  
            print(news_title)

        except:
          pass
        
  total_df = pd.DataFrame(total_list, columns=[headers])

  return total_df.to_csv("/Users/jinyoochan/Desktop/nlp/news_title_labeling.csv")


def crawling_day():

  chrome_options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


  headers = "news_title"
  year = [i for i in range(2006,2023)]
  month = [i for i in range(1, 13)]
  day = [i for i in range(1,32)]
  total_list = []

  for y in year:
    for m in month:
      for d in day:
        total_day = [f"{y}-{m}-{d}"]
        try:
          driver.get(f"https://finance.naver.com/news/mainnews.naver?date={y}-{m}-{d}")
          driver.maximize_window()
          time.sleep(1)
          html = driver.page_source
          soup = BeautifulSoup(html, "html.parser")

          for i in range(1,21):
            news_title = soup.select(f"#contentarea_left > div.mainNewsList > ul > li:nth-child({i}) > dl > dt > a")[0].text
            total_day.append(news_title)  
            print(news_title)
            if news_title == "":
              news_title = soup.select(f"#contentarea_left > div.mainNewsList > ul > li:nth-child({i}) > dl > dd.articleSubject > a")[0].text
              total_day.append(news_title)  
              print(news_title)
            else:
              pass
            
          total_list.append(total_day)
        
        except:
          total_list.append(total_day)


  total_df = pd.DataFrame(total_list)

  return total_df.to_csv("/Users/jinyoochan/Desktop/nlp/news_title_days.csv")





def crawling_test():

  pass


# 크롤링 실행
if __name__ == "__main__":
  
  crawling_test()
  