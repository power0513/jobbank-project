#使用for 迴圈爬取多頁資料
#爬取104人力銀行有關python的工作職缺
#結果轉存成json格式

import json
from matplotlib.pyplot import uninstall_repl_displayhook
import requests
import bs4
import random
import time

def job_list(url):
    htmlFile=requests.get(url)
    objSoup = bs4.BeautifulSoup(htmlFile.text,'lxml')
    jobs= objSoup.find_all('article',class_='js-job-item')
    job_list=[]
    for job in jobs:
        print('公司名稱:',job.get('data-cust-name'))
        print('職務名稱:',job.get('data-job-name'))

url_H='https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&page='
url_T='&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'
page_total = 10
for page in range(page_total):
    url= url_H+str(page+1)+url_T
    job_list(url)
    print('-'*70)
    time.sleep(random.randint(3,5))

#可以增加下一頁網址增加下一頁python職缺資訊
#url='https://www.104.com.tw/jobs/search/?keyword=python&order=1&jobsource=2018indexpoc&ro=0'


 