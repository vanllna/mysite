# coding:utf-8
# author:vanll
# -- demo code --
import requests
import json
import random
import time
from baofeng.threaddemo import thpay


orderurl = 'http://220.166.63.47:21003/goods/goods/publish'
ordernum = 5
tokenlist = ['Bearer 23ae0ffd-0eb2-487f-9a43-1da4b3659a16',
            'Bearer 49c8385d-60f8-44f5-a2c2-c365ec2e4139',
            'Bearer a11c822a-0f0e-456e-827b-08937879ca2c',
            'Bearer b8a54b47-789f-4818-b607-c2f6a00377d0',
            'Bearer c6d359ac-fd5b-4438-b15e-0ad99de07a14',
            'Bearer d2ca59d7-0706-4f58-b105-f8650b034997'
            ]

categary = [['5cdcc2c1dc8d260bf1cdbd98','5cdcc2cfdc8d260bf1cdbd99','5cdcc9a8dc8d264779a6be96','测量学徒'],
            ['5cdcc2c1dc8d260bf1cdbd98','5ce63164dc8d269794fe4d2e','5ce6317edc8d269794fe4d2f','施工队长'],
            ['5cbec5ca3fe01b434fabdc05','5cbec5d83fe01b434fabdc06','5cbec61f3fe01b434fabdc07','钻工'],
            ['5cbec5ca3fe01b434fabdc05','5ce63143dc8d269794fe4d2d','5ce631b6dc8d269794fe4d37','电焊工'],
            ['5cc264203fe01b635f2bb2ae','5cc2643d3fe01b635f2bb2af','5cd11fe75f93a71b41ddfcdf','财务']
            ]


yalujilist = ['SR23MR','SR26MR','SM28MR','SRP95']
username = ['赵郭','李想','张绎','刘洋','孙工','钱胡']
phone = ['18108189672','15208189672','19208189632','13708349632','16808147632']
yearlist = ["2019-01-01 00:00:00","2018-01-01 00:00:00","2017-01-01 00:00:00","2016-01-01 00:00:00"]

def order():
    for i in range(0, ordernum):
        startPrice = random.randrange(1, 3000)
        endPrice = random.randrange(3001, 6000)
        jobnumber = random.randrange(1,10)
        name = random.choice(username)
        tel = random.choice(phone)
        data = [catedata for catedata in categary]
        catechoice = random.choice(data)
        year = random.choice(yearlist)
        brand = ''
        marque = ''
        imgurl = ''
        if catechoice[2] == '5cdcc9a8dc8d264779a6be96':
            brand = '测量学徒'
            imgurl = 'LzE1NTkxMTE3OTkxNTAuanBlZw==_aa60cde7-367c-445a-9881-c28b84a72c74_I'
        elif catechoice[2] == '5ce6317edc8d269794fe4d2f' :
            brand = '施工队长'
            imgurl = 'LzE1NTkwMzUzNTUwODMuanBlZw==_7668a1ba-91a8-4648-8b1d-3d952a1f76b3_I'
        else :
            brand = '钻工'
            imgurl = 'LzE1NTkxMTE0NTM1MDkuanBlZw==_a96fce60-bfec-41cf-980a-8c151c0e1cb7_I'

        token = random.choice(tokenlist)
        print(token)
        header = {'authorization': token,
                  'Content-Type': 'application/json; charset=utf-8'
                  }

        # 招聘json
        datas = {"goodsInfo":{"recruit":{"welfare":[],"recruitType":0,"sexCondition":0,"ageCondition":0,"jobCondition":1,"educationCondition":1,
                                         "isNegotiable":False,"startTime":"2019-04-01 00:00:00","endTime":"2019-08-01 00:00:00",
                                         "projectCompany":"贝易网"}},"pics":[],"type":2,"startPrice":startPrice,"endPrice":endPrice,
                 "contactsSex":0,"address":"桂溪街道交子大道98AFC中航国际广场","countyCode":"510107","lat":"30.5841353","lon":"104.060316",
                 "category1stId":catechoice[0],"category2ndId":catechoice[1],"category3rdId":catechoice[2],
                 "category3rdName":catechoice[3],"quantity":jobnumber,"contactsName":name,"contactsMobile":tel}


        '''
        # 求租json   
        datas = {"goodsInfo":{"recruit":{"welfare":[],"recruitType":1,"sexCondition":None,"isWaiting":True,"jobCondition":0,"educationCondition":0,
        "isNegotiable":False}},"pics":[],"type":2,"startPrice":startPrice,"endPrice":endPrice,"contactsSex":0,"address":"武侯祠大街264号",
        "countyCode":"510107","lat":"30.641904","lon":"104.043243","category1stId":catechoice[0],
        "category2ndId":catechoice[1],"category3rdId":catechoice[2],"category3rdName":catechoice[3],"countyName":"武侯区",
        "contactsName":name,"contactsMobile":tel}
        '''

        data = json.dumps(datas)
        response = requests.post(orderurl, data=data,headers=header)
        resjson = response.json()
        print(response,resjson)
        # time.sleep(1)
        return resjson


if __name__ == '__main__':
    thpay(order)

