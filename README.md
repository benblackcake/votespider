# 中選會網站爬蟲votespider

## 使用說明
>套件 
>>BeautifulSoup  
>>requests  
>>django2.0.7  
>python manage.py runserver 8000
>
>localhost:8000/index
## 目標
>爬取中選會網站資料後,圖像化呈現北市選情  
 1.開票狀況  
 2.得票數1,2名差距  
 3.各候選人得票率  

## 做法
>後端使用django前端使用JavaScript  
使用request把網頁load進來  
用BeautifulSoup進行爬蟲  
因為沒有使用database所以每一次直接把上一次list資料clear  
利用JavaScript每五秒重新整理網頁,達到資料更新(但中選會網站實際上是一分鐘更新一次)  
把整理好的資料用chart.js呈現出來  
  
![](https://i.imgur.com/2YW5nMd.jpg)

## TODO
>可以把每分鐘資料匯入資料庫做出折線圖  
負載量大應該要用cache機制

