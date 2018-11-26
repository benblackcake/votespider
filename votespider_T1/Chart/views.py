from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import requests
# import xlwt
from bs4 import BeautifulSoup
from .function import ttmier

# from .function import fetch_all


row_name = list()
row_percentage = list()
row_per=list()
row_per_range=list()
row_open=list()
def ViewChart(request):
    row_name.clear()
    row_percentage.clear()
    row_per.clear()
    row_open.clear()
    row_per_range.clear()
    get_post()
    for i in range(0,len(row_percentage),2):
        row_per.append(row_percentage[i].replace(",",""))
        row_per_range.append(float(row_percentage[i+1].replace(",", "")))
    print(row_per)
    print(row_per_range)
    # print(row_open)
    row_open[0]=int(row_open[1])-int(row_open[0])
    ran=int(row_per[0])-int(row_per[1])
    return render(request,'index.html',{
        'dataName':row_name,
        'dataPer':row_per,
        'dataPerRange':row_per_range,
        'p':ran,
        'd':row_open
    })




# conn = pymysql.connect(host="localhost", user="root", passwd="", db="pydb")
# c = conn.cursor()

def get_post():
    targetURL = "https://www.cec.gov.tw/pc/zh_TW/TC/s63000000000000000.html"
    rs = requests.session()
    res = rs.get(targetURL, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    tab=soup.find("table",{"class":"tableT"})
    # print(soup.find("table",{"class":"tableT"}))

    for i in tab.findAll("tr",{"class":"trT"}):
        # print(i)

        if i.find(text="柯文哲"):
            row_name.append(i.find(text="柯文哲"))
        elif i.find(text="丁守中"):
            row_name.append(i.find(text="丁守中"))
        elif i.find(text="姚文智"):
            row_name.append(i.find(text="姚文智"))
        elif i.find(text="李錫錕"):
            row_name.append(i.find(text="李錫錕"))
        elif i.find(text="吳蕚洋"):
            row_name.append(i.find(text="吳蕚洋"))
        # if i.findAll({"class":"trT"}):
    for i in tab.findAll("td",{"class":"tdAlignRight"}):
        row_percentage.append(i.text.replace("%",""))
        print(i.text)

    for i in tab.findAll("tr",{"class":"trFooterT"}):
        # i.text.strip("0")
        row_open.extend(i.text.replace(u'\xa0\n', u'').split(": ")[1].split("/"))
        print(i.text.replace(u'\xa0\n', u'').split(": ")[1].split("/"))
    # print(tab.findAll("td",{"class":"tdAlignRight"}))
    print(row_name)
    print(row_percentage)