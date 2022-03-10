#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:48:32 2022

@author: mrpasta
"""

hours=input('Enter hours:\n')
hours=float(hours)
rate=input('Enter rate:\n')
rate=float(rate)
normal_rate=rate
over_rate=1.8*rate

#Rewrite your pay computation to give the employee 1.5 times 
#the hourly rate for hours worked above 40 hours.

if hours>40:
    normal_hours=40
    over_hours=hours-40
    pay=normal_hours*normal_rate+over_hours*over_rate
    print('pay: ',pay)
else:
    pay=hours*rate
    print('pay:',pay)
    