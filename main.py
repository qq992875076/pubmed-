import csv
import re
import json
from lxml import etree
import requests


import xlrd
def strs(row):
    values = ""
    for i in range(len(row)):
        if i == len(row) - 1:
            values = values + str(row[i])
        else:
            values = values + str(row[i])
    return values
# 打开文件
data = xlrd.open_workbook("L:\\博士论文\\8.1结果部分\作者部分\\4IR后作者发文数量前十的\\LARS ENGEBRETSEN.xls")
sqlfile = open("learn.txt", "a")  # 文件读写方式是追加
table = data.sheets()[0]  # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.row_values(1)  # 某一行数据
# 打印出行数列数
s = 0
for ronum in range(1, nrows):     #控制显示第几行，即去除行标题之类的
        s = s + 1
        row = table.cell_value(rowx=ronum, colx = 8) #只需要修改你要读取的列数-1
        row = str(row)
        values = strs(row)  # 调用函数，将行数据拼接成字符串
        # sqlfile.writelines(values + "\n")  # 将字符串写入新文件
        # sqlfile.writelines(values + "\t")  # 将字符串写入新文件
        #构建google学术的url
        baseurl = 'https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q='

        #title = "What's the rate of knee osteoarthritis 10 years after anterior cruciate ligament injury? An updated systematic review"
        title = values.replace("'","")
        print('第%d篇论文：'%s+title)
        url = baseurl + title
        #print('google学术网址'+url)
        headers = {

        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        'cookie':"AEC=AakniGOnr5EG1Atazrw93QTHzTpBVd7oUN89kZuHkRxQhHYNaFtlhdTJv0A; GSP=A=wLdAfQ:CPTS=1659675559:LM=1659675559:S=cRYwRtflMJOK_9N3; NID=511=ac8tomad2T4YzHSSx6zW5PY6HBSepDNq0Y-RrSs-EOBNYsjT-DE5x0zfHtZxIOvtHH2zTcbRFNRcKR-J5INf38WAgdbwf8m9cf1Rg-UZ-7SUHrLbAiMqoxr1laVKgx0BA8Jrp6S1zhI4Y1eqmpSadBbS_mQNqRKtYqtUuTfYw8ZPSno8Lx2TO9BthAFivu9DN2cUNMbAag"
        }#更新google学术需要的cookie

        res = requests.get(url, headers=headers, timeout=10)

        h = res.text
        h = str(h)
        #print(h)

        #href = re.findall(r'\" href="(.*?)\" data-clk=', h)

        try:
            href = re.findall(r'\" href=\"(.{25,50}?)\" data-clk=', h)
            href = ''.join(href)
        except OSError:
            print('第%d篇论文：报错' % s)
            pass
        else:
        #print(href)
        #print(len(href))
        # first_href = re.findall(r'pdf(.*)\.abstract',href)

        #print(first_href)
        # url1 = ''.join(first_href)#将列表赋值给一个字符串
        # url1 = url1 + '.abstract'
        # print(url1)#打印题目对应的google学术网址


        #杂志官网爬取摘要：两个期刊通用

            url1 = href

            headers1 = {

            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            'cookie':"wisepops_activity_session=%7B%22id%22%3A%22d5660e4c-206f-472b-9b12-ea57e2802586%22%2C%22start%22%3A1659550158976%7D; _rollupGA=GA1.2.1848034210.1652857148; FPID=FPID2.2.YZtQ5LkjnJdBd%2FpMogkNPG%2FD%2BfvA4MjTd9tCrIA90%2B0%3D.1652857148; _fbp=fb.1.1652857152194.508484868; __gads=ID=045f450c5ea52692:T=1656419458:S=ALNI_MZRNQ9LbuN4X8T9_fEwuWFW8KSxIg; accessMethod=undefined; OptanonAlertBoxClosed=2022-07-15T13:19:20.520Z; eupubconsent-v2=CPcLfz_PcLfz_AcABBENCYCsAP_AAH_AAChQI6tf_X__b3_j-_5_f_t0eY1P9_7__-0zjhfdt-8N3f_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2cr7NKJ7PEmnMbO2dYGH9_n13TuZKY7_____7z_v-v______f_7-3f3__p_3_--_e_V_99zfn9_____9vP___9v-_9__________3_4I7AEmGrcQBdiWOBNtGEUKIEYVhIdQKACigGFogsIHVwU7K4CfWELABAKgIwIgQYgowYBAAIBAEhEQEgB4IBEARAIAAQAKgEIACNgEFgBYGAQACgGhYgRQBCBIQZEBEcpgQESJBQT2ViCUHehphCHWWAFAo_4qEBEoAQrAyEhYOQ4AkBLhZIFmKF8gBGCFAKJUAA.f_gAD_gAAAAA; _ga_LHT0ZJKRSY=GS1.1.1657896209.2.0.1657896209.0; _ga_8P7810XE1M=GS1.1.1657896209.2.0.1657896209.0; has_js=1; loggedIn=false; _gid=GA1.2.1633322648.1659422024; _rollupGA_gid=GA1.2.1812491729.1659422024; zabUserId=1659422023610zabu0.8685686063849192; cebs=1; RefTrackGroup=bjsm.bmj.com; FPLC=Z5h8P5Z5PHmIDt2BQzRHSXnvwK%2FOqQD3TuLxHmt8QM1uyxRVL%2BOt1G9MKmoAoARM2poIhvNXMRiNpgv2ZywtcCGEtF2YSXWvJ0Z9nkj%2FdX6D%2BzLOsjWpa3zda73c1Q%3D%3D; fcsid=ehb8ov7dmfm3pufa1s3tnobjva; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%22347602%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1652857156751%7D%2C%22354242%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1656419469097%7D%2C%22362809%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1659511870367%7D%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A66%2C%22cid%22%3A%222914%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; RefTrack=bjsm.bmj.com/content/55/17/949.abstract; SSESS5ac278cb1207db5e61ce8ffc30a9da88=IHKvU0qhPHs1GTrjJZcRwINorboI0zeOUToi6-1ykQk; OptanonConsent=isIABGlobal=false&datestamp=Thu+Aug+04+2022+03%3A09%3A16+GMT%2B0900+(%E9%9F%A9%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.8.0&hosts=&consentId=586a3fc9-24d8-4519-ac6f-2386a07c6f7a&interactionCount=2&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1%2CSTACK42%3A1%2Cgad%3A1&AwaitingReconsent=false&geolocation=KR%3B27; __gpi=UID=0000070d599a71c5:T=1656419458:RT=1659550156:S=ALNI_MZ3Aq9B_z4kYqaJ_WKmX5tEot_leg; zsc6c8747c090bf4c80bb73aa48c0ee8781=1659550156760zsc0.48861597234174403; zft-sdc=isef%3Dtrue-isfr%3Dtrue-src%3Ddirect; zps-tgr-dts=sc%3D5-expAppOnNewSession%3D%5B%5D-pc%3D1-sesst%3D1659550156762; cebsp=26; _ce.s=v~e1b7747fabd930cbc0ff62ba72aa84bd90fbfbee~vpv~3~v11.rlc~1659550156822; _ga_EXTSVLH45V=GS1.1.1659550156.10.0.1659550156.60; _ga=GA1.2.1848034210.1652857148; wisepops_visits=%5B%222022-08-03T18%3A09%3A18.468Z%22%2C%222022-08-03T08%3A15%3A12.695Z%22%2C%222022-08-03T07%3A33%3A42.941Z%22%2C%222022-08-03T07%3A30%3A51.468Z%22%2C%222022-08-03T07%3A09%3A29.747Z%22%2C%222022-08-02T15%3A17%3A06.335Z%22%2C%222022-08-02T15%3A16%3A24.238Z%22%2C%222022-08-02T15%3A13%3A48.646Z%22%2C%222022-08-02T15%3A08%3A28.088Z%22%2C%222022-08-02T06%3A49%3A04.188Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-08-03T18%3A09%3A18.468Z%22%2C%22mtime%22%3A1659550158960%2C%22pageviews%22%3A1%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3Anull%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D"
            }

            try:
                res1 = requests.get(url1, headers=headers1, timeout=50)
                h1 = res1.text
                h1 = str(h1)
                ab = re.findall(r'description" content="(.*?)\" />', h1,re.S)
                abstract = ''.join(ab)

            except OSError:
                print('第%d篇论文：报错' % s )
                pass
            else:
                print('第%d篇论文：' % s + abstract)
                print('\n\n\n')



#sqlfile.close()  # 关闭写入的文件

# #构建google学术的url
# baseurl = 'https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q='
# title = "What's the rate of knee osteoarthritis 10 years after anterior cruciate ligament injury? An updated systematic review"
# url = baseurl + title
# headers = {
#
# 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
# 'cookie':"AEC=AakniGOnr5EG1Atazrw93QTHzTpBVd7oUN89kZuHkRxQhHYNaFtlhdTJv0A; NID=511=mYLXvkl1M6TGYLzmjAO2ZDmIFjR7ZTsyMIz_xpf6WiFmv998QricvfZXxwv9hxz5U3mPG3owovx4TTuPg6s9-rH8GqY_MHWsdzqKdvkSfS6gKXzJ_9RJPFoZwxZ_MK0MSC5x3_pSMXcGq9oAXjIi_M3RyR_7CufNgCgzQUHw7GDEGyNs6jdcvot2aWHIFy0De0SpKBrw7A; GSP=A=wLdAfQ:CPTS=1659590941:LM=1659590941:S=4T6WPczDKohnaeWl"
# }#更新google学术需要的cookie
#
# res = requests.get(url, headers=headers, timeout=10)
# h = res.text
# h = str(h)
# href = re.findall(r'\" href="(.*?)\" data-clk=', h)
# href = ''.join(href)
# #print(href)
# first_href = re.findall(r'pdf(.*)\.abstract',href)
#
# #print(first_href)
# url1 = ''.join(first_href)#将列表赋值给一个字符串
# url1 = url1 + '.abstract'
# print(url1)
#
# #杂志官网爬取摘要：两个期刊通用
#
# url1 = url1
#
# headers1 = {
#
# 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
# 'cookie':"wisepops_activity_session=%7B%22id%22%3A%22d5660e4c-206f-472b-9b12-ea57e2802586%22%2C%22start%22%3A1659550158976%7D; _rollupGA=GA1.2.1848034210.1652857148; FPID=FPID2.2.YZtQ5LkjnJdBd%2FpMogkNPG%2FD%2BfvA4MjTd9tCrIA90%2B0%3D.1652857148; _fbp=fb.1.1652857152194.508484868; __gads=ID=045f450c5ea52692:T=1656419458:S=ALNI_MZRNQ9LbuN4X8T9_fEwuWFW8KSxIg; accessMethod=undefined; OptanonAlertBoxClosed=2022-07-15T13:19:20.520Z; eupubconsent-v2=CPcLfz_PcLfz_AcABBENCYCsAP_AAH_AAChQI6tf_X__b3_j-_5_f_t0eY1P9_7__-0zjhfdt-8N3f_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2cr7NKJ7PEmnMbO2dYGH9_n13TuZKY7_____7z_v-v______f_7-3f3__p_3_--_e_V_99zfn9_____9vP___9v-_9__________3_4I7AEmGrcQBdiWOBNtGEUKIEYVhIdQKACigGFogsIHVwU7K4CfWELABAKgIwIgQYgowYBAAIBAEhEQEgB4IBEARAIAAQAKgEIACNgEFgBYGAQACgGhYgRQBCBIQZEBEcpgQESJBQT2ViCUHehphCHWWAFAo_4qEBEoAQrAyEhYOQ4AkBLhZIFmKF8gBGCFAKJUAA.f_gAD_gAAAAA; _ga_LHT0ZJKRSY=GS1.1.1657896209.2.0.1657896209.0; _ga_8P7810XE1M=GS1.1.1657896209.2.0.1657896209.0; has_js=1; loggedIn=false; _gid=GA1.2.1633322648.1659422024; _rollupGA_gid=GA1.2.1812491729.1659422024; zabUserId=1659422023610zabu0.8685686063849192; cebs=1; RefTrackGroup=bjsm.bmj.com; FPLC=Z5h8P5Z5PHmIDt2BQzRHSXnvwK%2FOqQD3TuLxHmt8QM1uyxRVL%2BOt1G9MKmoAoARM2poIhvNXMRiNpgv2ZywtcCGEtF2YSXWvJ0Z9nkj%2FdX6D%2BzLOsjWpa3zda73c1Q%3D%3D; fcsid=ehb8ov7dmfm3pufa1s3tnobjva; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%22347602%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1652857156751%7D%2C%22354242%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1656419469097%7D%2C%22362809%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1659511870367%7D%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A66%2C%22cid%22%3A%222914%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; RefTrack=bjsm.bmj.com/content/55/17/949.abstract; SSESS5ac278cb1207db5e61ce8ffc30a9da88=IHKvU0qhPHs1GTrjJZcRwINorboI0zeOUToi6-1ykQk; OptanonConsent=isIABGlobal=false&datestamp=Thu+Aug+04+2022+03%3A09%3A16+GMT%2B0900+(%E9%9F%A9%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.8.0&hosts=&consentId=586a3fc9-24d8-4519-ac6f-2386a07c6f7a&interactionCount=2&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1%2CSTACK42%3A1%2Cgad%3A1&AwaitingReconsent=false&geolocation=KR%3B27; __gpi=UID=0000070d599a71c5:T=1656419458:RT=1659550156:S=ALNI_MZ3Aq9B_z4kYqaJ_WKmX5tEot_leg; zsc6c8747c090bf4c80bb73aa48c0ee8781=1659550156760zsc0.48861597234174403; zft-sdc=isef%3Dtrue-isfr%3Dtrue-src%3Ddirect; zps-tgr-dts=sc%3D5-expAppOnNewSession%3D%5B%5D-pc%3D1-sesst%3D1659550156762; cebsp=26; _ce.s=v~e1b7747fabd930cbc0ff62ba72aa84bd90fbfbee~vpv~3~v11.rlc~1659550156822; _ga_EXTSVLH45V=GS1.1.1659550156.10.0.1659550156.60; _ga=GA1.2.1848034210.1652857148; wisepops_visits=%5B%222022-08-03T18%3A09%3A18.468Z%22%2C%222022-08-03T08%3A15%3A12.695Z%22%2C%222022-08-03T07%3A33%3A42.941Z%22%2C%222022-08-03T07%3A30%3A51.468Z%22%2C%222022-08-03T07%3A09%3A29.747Z%22%2C%222022-08-02T15%3A17%3A06.335Z%22%2C%222022-08-02T15%3A16%3A24.238Z%22%2C%222022-08-02T15%3A13%3A48.646Z%22%2C%222022-08-02T15%3A08%3A28.088Z%22%2C%222022-08-02T06%3A49%3A04.188Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-08-03T18%3A09%3A18.468Z%22%2C%22mtime%22%3A1659550158960%2C%22pageviews%22%3A1%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3Anull%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D"
# }
# res1 = requests.get(url1, headers=headers1, timeout=50)
# h1 = res1.text
# h1 = str(h1)
# ab = re.findall(r'description" content="(.*?)\" />', h1,re.S)
# abstract = ''.join(ab)
# print(abstract)