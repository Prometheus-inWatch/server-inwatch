#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

       
def to_json(tipId, text):
        '''Converts tip to json.
        
        Args:
            tipId:
            text:
            
        Returns:
            Json formated string.
        '''
        return '{"tipId":'+str(tipId)+', "text":"'+str(text)+'"}'
    
def get_tip():
        '''Get tip from database.
        
        Returns:
            Tuple (tipId, text).
        '''
        return (148,"Quita cigarrillos y ceniceros del automovil")

if __name__ == "__main__":
    tip = tips()
    print(tip.GET())