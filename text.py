# -*- coding: utf-8 -*-
import requests
import re
import xlrd
import xlwt

def strs(row):
    values = ""
    for i in range(len(row)):
        if i == len(row) - 1:
            values = values + str(row[i])
        else:
            values = values + str(row[i])
    return values


data = xlrd.open_workbook("L:\\博士论文\\8.1结果部分\国家分析\\图谱制作\\after10.xls")
sqlfile = open("learn.txt", "a")  # 文件读写方式是追加
table = data.sheets()[0]  # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.row_values(1)  # 某一行数据
s = 0

#创建excel
MY_EXCEL = xlwt.Workbook(encoding='utf-8') # 创建MY_EXCEL对象
excelsheet = MY_EXCEL.add_sheet('sheet1') # 创建工作表（创建excel里面的工作表）
excelsheet.write(0,0,"DOI")
excelsheet.write(0,1,"title")
excelsheet.write(0,2,"abstract")
m = 0
n = 1
for ronum in range(1, nrows):  # 控制显示第几行，即去除行标题之类的
    s = s + 1
    row = table.cell_value(rowx=ronum, colx=3)  # 只需要修改你要读取的列数-1
    row = str(row)
    #excelsheet.write()
    values = strs(row)
#DOI写入excel
    try:
        excelsheet.write(n,0,values)
    except Exception as e:
        excelsheet.write(n, 0, "kong")
        excelsheet.write(n, 1, "kong")
        excelsheet.write(n, 2, "kong")
        continue
    else:

        # 获取DIO号对应的pubmed的url
        url = 'https://pubmed.ncbi.nlm.nih.gov/?term=+' + values
        headers = {

            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            'cookie': "pm-csrf=WOMsnAg8u2ia9ytoBd3zS6hSHVViliyRaIXoJBH5yIiZbPMZggSVs4OvhHgDPLWt; ncbi_sid=7F8235C7274A9C53_11604SID; pm-sb=relevance; _ce.s=v~b7b03023b86e701b27f3384c2c9dd618fd943682~vpv~1; _ga_HF818T9R4Y=GS1.1.1655482980.28.1.1655482980.0; pm-sid=ij7xz4imld-3G-wyqpKgYA:3156f7990e1f95d20cdeb68f81e2ad5c; pm-adjnav-sid=ZBGz5_XE2N7qwvCkrg2KHg:3156f7990e1f95d20cdeb68f81e2ad5c; _gid=GA1.2.2082975641.1662469088; _ga_DP2X732JSX=GS1.1.1662469088.61.1.1662469102.0.0.0; _ga=GA1.1.1166724415.1651816378; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgJwEECMAYgAylHYCiArAMw0DCVppATABy6H1stX3EB2FgDp8wgLZx8IADQgArgDsANgHsAhqkVQAHgBdMoFpnDyARuKjo5NE2HOXrIACwnEqy7JBUTXlsRM8ImZyajpGZmJ2Tm5efiFRCSk/aSx7CysMdMcMd0sMADkAeQKKP2M0hythRQBjM2Qa5XEa5ERhAHNVGD9sE3xsfy8aAKx8YjYAm1SQAaGbCtniZymQOhMAM3VlAGcoYdcsPQh5fZs2Xxs+rGcWFmd8W+M5FZMnh+xJr2dbLGJhGgCYSrZyHBQqDRaXQGF4+P5eWgmABsvARYLYbGkcioSJMqyoAjxXiRM3YtjkSNxaXUHSgcBgyCgAHcQABfVlAA=="
        }

        try:
            data = requests.get(url, headers=headers, timeout=10)
            data1 = data.text
            data2 = str(data1)
            url1 = re.findall(r'content\=\"(.{25,50})\"><meta', data2)
            url2 = url1[0]
        except IndexError:
            print('pubmend没有检索到这篇论文DOI是%s' % values)
            pass
        else:

            # print(url2)

            # 获取对应pubmed的网页数据
            try:
                p_url = url2
                # p_headers = {
                #
                #     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
                #     'cookie': "pm-csrf=WOMsnAg8u2ia9ytoBd3zS6hSHVViliyRaIXoJBH5yIiZbPMZggSVs4OvhHgDPLWt; ncbi_sid=7F8235C7274A9C53_11604SID; pm-sb=relevance; _ce.s=v~b7b03023b86e701b27f3384c2c9dd618fd943682~vpv~1; _ga_HF818T9R4Y=GS1.1.1655482980.28.1.1655482980.0; pm-sid=ij7xz4imld-3G-wyqpKgYA:3156f7990e1f95d20cdeb68f81e2ad5c; pm-adjnav-sid=ZBGz5_XE2N7qwvCkrg2KHg:3156f7990e1f95d20cdeb68f81e2ad5c; pm-sessionid=t0xm93i4ywgzm67haoj5a3grf32qoawi; _gid=GA1.2.1351034133.1661839944; _ga_DP2X732JSX=GS1.1.1661839944.58.1.1661839963.0.0.0; _ga=GA1.1.1166724415.1651816378; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgAwDEDMAQtiQIyECcuA7KQKwAcdJJATIaawMLWsBsFAIL4KAOlKiAtnFIgANCACuAOwA2AewCGqZVAAeAF0yhWmcIoBGkqOgX4zYS9dsgALGcTrr8kHTM/WbDM8IhZyKlpGZhZ2Th5+IRFxKRkA2SxHKxsMTOcMT2sMADkAeSKAUQDTDKcbUWUAYwtketVJeuREUQBzdRgAijNSCkCffCCsUmwGILt0kGHRu2qF7FdZkHx7LAAzTVUAZygx9ywDCEVjuwZ/O0GsBgF1jfWzR4oGVlkFV22cUXw1FEL1OSjUWh0+iMPz8WA2dD+fFYfgUdFBFEBPjofGCWOouIUfHm/HxhJxGU03SgcBgyCgAHcQABfJlAA=="
                # }
                p_data = requests.get(url = p_url, headers = headers, timeout = 10)
                p_data = str(p_data.text)
                # print(p_data)
    #DOI 对应的题目
                title = re.findall(r'\<title\>(.*?)\ \-\ PubMed\<\/title\>', p_data)
    #excel写入题目
                excelsheet.write(n,1,title)#excel写入题目

                #print(title)
                ab = re.findall(r'\<div\ class\=\"abstract\"\ id\=\"abstract\"\>(.*?)Keywords\:', p_data, re.S)
                ab = str(ab)
                #print(len(ab))
                if len(ab)==2:
                    ab = re.findall(r'\<div\ class\=\"abstract\"\ id\=\"abstract\"\>(.*?)\<div\ class\=\"similar\-articles\"\ id\=\"similar\"\>', p_data, re.S)
                    ab = str(ab)
                    ab = ab.replace("\n", "")
                    ab = ab.replace(" ", "")
                    ab = re.sub(r'<.*?>', '', ab)
                    ab = ab.replace('\\n', ' ')
                    ab = re.sub(r'\s{4,}', '\n', ab)
                    ab = ab.replace(" ", "")

                else:
                    ab = ab.replace("\n", "")
                    ab = ab.replace(" ", "")
                    ab = re.sub(r'<.*?>', '', ab)
                    ab = ab.replace('\\n', ' ')
                    ab = re.sub(r'\s{4,}', '\n', ab)
                    ab = ab.replace(" ", "")

                # print(r'ab')

            except OSError:
                values = str(values)
                print('pubmend检索到这篇论文但是爬取出错DOI是%s' % values)
                pass
            else:

                excelsheet.write(n,2,ab)
                print(ab)
                print('第%d篇爬取完成' % s)
    n = n + 1
    MY_EXCEL.save('country-after-10.xls')