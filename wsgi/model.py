#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from datetime import datetime

from bdinterface import BDInterface


#bd = BDInterface()


class UserManager(object):

    def __init__(self):
        self.user_list = []
    
    def  get_user(self,email):
        for user in self.user_list:
            if user.email == email:
                return user
        return None


class User(object):
    
    def __init__(self, email, cigarsPerDay,  cigarsPerPacket, pricePerPacket, stopSmokingDate):
        self.userId = 0
        self.email = email
        self.cigarsPerDay = cigarsPerDay
        self.cigarsPerPacket = cigarsPerPacket
        self.pricePerPacket = pricePerPacket
        self.stopSmokingDate = stopSmokingDate
        self.totalUnsmokedCigars=20
        self.totalMoneySaved=44.90
        self.totalTimeSaved=20
        self.totalDaysClean =20

    def __userget_to_json (self,userId,cigarsPerday,cigarsPerPacket,pricerPerPacket,stopSmokingDate,totalUnsmokedCigars,totalMoneySaved,totalTimeSaved,totalDaysClean):
        return '\
{\
"userId": '+str(userId)+',\
"cigarsPerday": '+str(cigarsPerday)+',\
"cigarsPerPacket": '+str(cigarsPerPacket)+',\
"pricerPerPacket": '+str(pricerPerPacket)+',\
"stopSmokingDate": "'+str(stopSmokingDate)+'",\
"totalUnsmokedCigars": '+str(totalUnsmokedCigars)+',\
"totalMoneySaved": '+str(totalMoneySaved)+',\
"totalTimeSaved": '+str(totalTimeSaved)+',\
"totalDaysClean": '+str(totalDaysClean)+'\
} '

    def to_json(self):
        return self.__userget_to_json(self.userId, self.cigarsPerDay, self.cigarsPerPacket, self.pricePerPacket, self.stopSmokingDate, self.totalUnsmokedCigars, self.totalMoneySaved, self.totalTimeSaved, self.totalDaysClean)

    def __eq__(self,other):
        try:
            if self.email == other.email:
                return True
            else:
                return False
        except:
            return False
    
    def log(self):
        pass
       
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


users = UserManager()