#!/usr/bin/env python
# -*- coding: utf-8 -*-
def jsonuserget (userId,cigarsPerday,cigarsPerPacket,pricerPerPacket,stopSmokingDate,totalUnsmokedCigars,totalMoneySaved,totalTimeSaved,totalDaysClean):
	return '\
	{\n\
	\t"userId": '+str(userId)+',\n\
	\t"cigarsPerday": '+str(cigarsPerday)+',\n\
	\t"cigarsPerPacket": '+str(cigarsPerPacket)+',\n\
	\t"pricerPerPacket": '+str(pricerPerPacket)+',\n\
	\t"stopSmokingDate": "'+stopSmokingDate+'",\n\
	\t"totalUnsmokedCigars": '+str(totalUnsmokedCigars)+',\n\
	\t"totalMoneySaved": '+str(totalMoneySaved)+',\n\
	\t"totalTimeSaved": '+str(totalTimeSaved)+',\n\
	\t"totalDaysClean": '+str(totalDaysClean)+'\n\
	} ' 

def jsontip(tipId,text):
    return'\
    {\
    "tipId":'+str(tipId)+',\
	"text":"'+text+'"\
     }'

def jsonuserpost(email,cigarsPerday,cigarsPerPackect,pricerPerPacket,stopSmokingDate):
    return '\
{\
"email": "'+email+'",\
"cigarsPerday": '+str(cigarsPerday)+',\
"cigarsPerPacket": '+str(cigarsPerPacket)+',\
"pricerPerPacket": '+str(pricerPerPacket)+',\
"stopSmokingDate": "'+str(stopSmokingDate)+'"\
} '


def jsonlog(userId,is_ok,day,smokedCigars):
    return '{\
"userId": '+str(userId)+',\
"is_ok": '+is_ok+',\
"day": "'+day+'",\
"smokedCigars": '+str(smokedCigars)+'\
}' 

text='Hola'
tipId=1
day='12:12'
smokedCigars=12
is_ok='true'
userId=33002
cigarsPerday=10
cigarsPerPacket=20
pricerPerPacket=3
stopSmokingDate="2015-02-20T18:25:43+01:00"
totalUnsmokedCigars=32
totalMoneySaved=2.4
totalTimeSaved=120.0
totalDaysClean=2
email='a@a.com'


