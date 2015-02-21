#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

       
def tips_to_json(tipId, text):
    '''Converts tip to json.
    
    Args:
        tipId:
        text:
        
    Returns:
        Json formated string.
    '''
    return '{"tipId":'+str(tipId)+', "text":"'+str(text)+'"}'
    
def get_tips():
    '''Get tip from database.
    
    Returns:
        Tuple (tipId, text).
    '''
    return (148,"Quita cigarrillos y ceniceros del automovil")


def userget_to_json (userId,cigarsPerday,cigarsPerPacket,pricerPerPacket,stopSmokingDate,totalUnsmokedCigars,totalMoneySaved,totalTimeSaved,totalDaysClean):
    return '\
{\
"userId": '+str(userId)+',\
"cigarsPerday": '+str(cigarsPerday)+',\
"cigarsPerPacket": '+str(cigarsPerPacket)+',\
"pricerPerPacket": '+str(pricerPerPacket)+',\
"stopSmokingDate": "'+stopSmokingDate+'",\
"totalUnsmokedCigars": '+str(totalUnsmokedCigars)+',\
"totalMoneySaved": '+str(totalMoneySaved)+',\
"totalTimeSaved": '+str(totalTimeSaved)+',\
"totalDaysClean": '+str(totalDaysClean)+'\
} '

def get_user():
    '''Get user from database.
    
    Returns:
        Tuple (userId, cigarsPerDay, cigarsPerPacket, pricePerPacket, stopSmokingDate, totalUnsmokedCigars, totalMoneySaved, totalTimeSaved, totalDaysClean)
    '''
    userId=33002
    cigarsPerDay=10
    cigarsPerPacket=20
    pricePerPacket=3
    stopSmokingDate="2015-02-20T18:25:43+01:00"
    totalUnsmokedCigars=32
    totalMoneySaved=2.4
    totalTimeSaved=120.0
    totalDaysClean=2
    return (userId, cigarsPerDay, cigarsPerPacket, pricePerPacket, stopSmokingDate, totalUnsmokedCigars, totalMoneySaved, totalTimeSaved, totalDaysClean)
    
    
def userpost_to_json(email,cigarsPerday,cigarsPerPacket,pricerPerPacket,stopSmokingDate):
    return '\
{\
"email": "'+str(email)+'",\
"cigarsPerday": '+str(cigarsPerday)+',\
"cigarsPerPacket": '+str(cigarsPerPacket)+',\
"pricerPerPacket": '+str(pricerPerPacket)+',\
"stopSmokingDate": "'+str(stopSmokingDate)+'"\
} '
    
def post_user():
    '''Post user to database.
    
    Returns:
        Tuple (email, cigarsPerDay, cigarsPerPacket, pricerPerPacket, stopSmokingDate)
    '''
    email='example@example.com'
    cigarsPerDay=10
    cigarsPerPacket=20
    pricePerPacket=20
    stopSmokingDate="2015-02-20T18:25:43+01:00"
    
    return (email, cigarsPerDay, cigarsPerPacket, pricePerPacket, stopSmokingDate)

def log_to_json(_id, userId, day, cigarsSmoked, ok):
    return '{\
"id": '+str(_id)+'\
"userId": '+str(userId)+',\
"is_ok": '+str(ok).lower()+',\
"day": "'+day+'",\
"smokedCigars": '+str(cigarsSmoked)+'\
}' 

def get_log():
    '''Get log from database.
    
    Returns:
        Tuple (id, userId, day, cigarsSmoked, ok)
    '''
    _id=123465
    userId=33002
    day="2015-02-20T18:25:43+01:00"
    cigarsSmoked=12
    ok=True
 
    return (_id, userId, day, cigarsSmoked, ok)
