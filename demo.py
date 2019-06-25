# coding:utf-8
# author:vanll
# -- demo code --

import random
import requests
import json



a = random.randrange(1,4)
b = random.random()
c = random.choice(['aaaa','bbbb','cccc'])

startPrice = random.randrange(1,3000)
endPrice = random.randrange(3001,6000)

categary = [['5cbec42a3fe01b434fabdbf7','5cbec56c3fe01b434fabdbfb','5ce63822dc8d269794fe4d89','挖掘机'],
            ['5cbec42a3fe01b434fabdbf7','5cbec56c3fe01b434fabdbfb','5ce63822dc8d269794fe4d88','推土机'],
            ['5cbec42a3fe01b434fabdbf7','5cbec56c3fe01b434fabdbfb','5ce63822dc8d269794fe4d8a','压路机'],
            ]


data = [ catedata for catedata in categary]
catechoice = random.choice(data)
print(catechoice)
# print(data[0][3])
tokenlist = ['863fc7f2-ece0-41e6-a9ee-77f85e935961',
         '8453bf50-0750-4797-89da-1ddc94bc6a70',
         '3c95cfa5-90f2-4561-b4dc-ac3a47c40c78',
         '21ad2357-8723-4d2b-9ab7-ceb6362b8605',
         '17ff5ed4-4464-46ce-acf8-f638ae8ba243',
         '0422d9c6-cba3-48cb-bd2b-acda4991971c'
         ]

# print(random.choice(tokenlist))




'''    
url = 'http://220.166.63.47:21003/goods/goods/publish'
# 出售
datas = {"goodsInfo":{"second":{"goodsRelatedInfo":{},"maintainInfo":{},"secondType":0,"isExFactoryDatePublic":True,"isPurchaseDatePublic":True,"isServiceTimePublic":True,"isRelatedInfoPublic":True,"isMaintainInfoPublic":True,"brand":"小松","marque":"PC56","exFactoryDate":"2019-01-01 00:00:00","purchaseDate":"2019-01-01 00:00:00","serviceTime":"430"}},"pics":[{"major":True,"url":"LzE1NTkwMTI4Nzk4MjIuanBlZw==_bfbcf95b-9295-4757-aee3-9a349c7398ca_I","sequence":0}],"type":0,"startPrice":startPrice,"endPrice":endPrice,"contactsSex":0,"address":"九里堤星科路3号","countyCode":"510106","lat":"44.056051","lon":"116.032593","category1stId":"5cbec42a3fe01b434fabdbf7","category2ndId":"5cbec56c3fe01b434fabdbfb","category3rdId":"5ce63822dc8d269794fe4d89","category3rdName":"挖掘机","countyName":"金牛区","contactsName":"赵郭","contactsMobile":"18108189672"}
# 求购
#datas = {"goodsInfo":{"second":{"goodsRelatedInfo":{},"maintainInfo":{},"secondType":1,"isRelatedInfoPublic":True,"isMaintainInfoPublic":True,"brand":"小松","marque":"PC56","exFactoryDate":"2019-01-01 00:00:00","purchaseDate":"2019-01-01 00:00:00","serviceTime":"699"}},"pics":[{"major":True,"url":"LzE1NTkwMTI4Nzk4MjIuanBlZw==_bfbcf95b-9295-4757-aee3-9a349c7398ca_I","sequence":0}],"type":0,"startPrice":startPrice,"endPrice":endPrice,"contactsSex":0,"address":"桂溪街道交子大道98AFC中航国际广场","countyCode":"510107","lat":"30.5841353","lon":"104.060316","category1stId":"5cbec42a3fe01b434fabdbf7","category2ndId":"5cbec56c3fe01b434fabdbfb","category3rdId":"5ce63822dc8d269794fe4d89","category3rdName":"挖掘机","quantity":"1","contactsName":"吴世","contactsMobile":"18108189672"}
# 出租
#datas = {"goodsInfo":{"lease":{"forbiddenAreas":[],"forbiddenProjects":[],"availableAreas":[],"availableProjects":[],"leaseInsuranceInfo":{},"leasePeriodInfo":{},"paymentMethods":[{"pwId":"1122473629615726593","name":"押一付一"}],"leaseType":0,"exFactoryDate":"2019-01-01 00:00:00","purchaseDate":"2019-01-01 00:00:00","isUsing":False,"isExFactoryDatePublic":True,"isPurchaseDatePublic":True,"isServiceTimePublic":True,"brand":"山推","marque":"SD13","serviceTime":"143"}},"pics":[{"major":True,"url":"LzE1NTkwMDk1NDY3MjIuanBlZw==_bacba2ce-8995-47ae-bbb2-990616f96d23_I","sequence":0}],"type":1,"startPrice":startPrice,"endPrice":endPrice,"contactsSex":0,"category1stId":"5cbec58d3fe01b434fabdc02","category2ndId":"5cbee7693fe01b5ffcc57c91","category3rdId":"5ce63448dc8d269794fe4d4a","category3rdName":"推土机","contactsName":"李晨","contactsMobile":"18108189672","address":"东风东路25号","countyCode":"530103","countyName":"盘龙区","lat":"25.037468","lon":"102.723692"}
# 求租
#datas = {"goodsInfo":{"lease":{"availableProjects":[],"forbiddenAreas":[],"forbiddenProjects":[],"leaseInsuranceInfo":{},"leasePeriodInfo":{},"paymentMethods":[{"pwId":"1122473629615726593","name":"押一付一"}],"leaseType":1,"exFactoryDate":"2019-01-01 00:00:00","purchaseDate":"2019-01-01 00:00:00","brand":"小松","marque":"PC56","serviceTime":"456"}},"pics":[{"major":True,"url":"LzE1NTkwMTI4Nzk4MjIuanBlZw==_bfbcf95b-9295-4757-aee3-9a349c7398ca_I","sequence":0}],"type":1,"startPrice":startPrice,"endPrice":endPrice,"contactsSex":0,"address":"霄云路42号","countyCode":"110105","lat":"39.955764","lon":"116.462185","category1stId":"5cbec58d3fe01b434fabdc02","category2ndId":"5cbee7693fe01b5ffcc57c91","category3rdId":"5ce63448dc8d269794fe4d4b","category3rdName":"挖掘机","quantity":"1","countyName":"朝阳区","contactsName":"张图","contactsMobile":"18108189672"}
# 招聘
#datas = {"goodsInfo":{"recruit":{"welfare":[],"recruitType":0,"sexCondition":0,"ageCondition":0,"jobCondition":1,"educationCondition":1,"isNegotiable":False,"startTime":"2019-04-01 00:00:00","endTime":"2019-08-01 00:00:00","projectCompany":"贝易网"}},"pics":[],"type":2,"startPrice":startPrice,"endPrice":endPrice,"contactsSex":0,"address":"桂溪街道交子大道98AFC中航国际广场","countyCode":"510107","lat":"30.5841353","lon":"104.060316","category1stId":"5cdcc2c1dc8d260bf1cdbd98","category2ndId":"5ce63164dc8d269794fe4d2e","category3rdId":"5ce6317edc8d269794fe4d2f","category3rdName":"施工队长","quantity":"2","contactsName":"王鹏","contactsMobile":"18108189672"}
# 求职
# datas = {"goodsInfo":{"recruit":{"welfare":[],"recruitType":1,"sexCondition":None,"isWaiting":True,"jobCondition":0,"educationCondition":0,"isNegotiable":False}},"pics":[],"type":2,"startPrice":startPrice,"endPrice":endPrice,"contactsSex":0,"address":"武侯祠大街264号","countyCode":"510107","lat":"30.641904","lon":"104.043243","category1stId":"5cdcc2c1dc8d260bf1cdbd98","category2ndId":"5cdcc2cfdc8d260bf1cdbd99","category3rdId":"5cdcc9a8dc8d264779a6be96","category3rdName":"测量学徒","countyName":"武侯区","contactsName":"张帅","contactsMobile":"18108189672"}

data = json.dumps(datas)
print('data: ',type(data))
header = {'authorization':'Bearer 044c5460-d63a-41a9-a245-671d05b1460f',
            'Content-Type': 'application/json; charset=utf-8'
          }
print(type(header))
response = requests.post(url,data=data,headers=header)
print(response)
restext = response.text
print(restext)
resjson = json.loads(restext)
print(resjson)
'''

