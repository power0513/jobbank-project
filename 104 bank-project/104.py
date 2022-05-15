#爬取104人力銀行有關python的工作職缺
#結果轉存成json格式
import json
import requests
import bs4

#可以增加下一頁網址增加下一頁python職缺資訊
url='https://www.104.com.tw/jobs/search/?keyword=python&order=1&jobsource=2018indexpoc&ro=0'

htmlFile=requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text,'lxml')
jobs= objSoup.find_all('article',class_='js-job-item')
job_list=[]
for job in jobs:
    cust_name = job.get('data-cust-name')
    print('公司名稱:',cust_name)
    job_name = job.get('data-job-name')
    print('職務名稱:',job_name)
    d=[('公司名稱', cust_name),('職務名稱',job_name)]
    j_dict=dict(d)
    job_list.append(j_dict)

myjob={'Job':job_list}
fn="104 python job.json"
with open (fn,'w') as fn0bj:
    json.dump(myjob, fn0bj,indent=2, ensure_ascii=False)
    