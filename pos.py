#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:03:12 2021

@author: Tom LUCAS
"""

from pypot import vrep
from pypot.creatures import PoppyErgoJr
from time import sleep


vrep.close_all_connections()
poppy = PoppyErgoJr(simulator='vrep', scene='poppy_ergo_jr_holder.ttt', camera='dummy')

def m(m,x,t=1,wait=False):
    poppy.goto_position({("m"+str(m)):x},t,wait=wait)
    
    
def sky_watching():
    m(1,180)
    m(2,0)
    m(3,0)
    m(4,90)
    m(5,-90)


def reverse():
    m(1,180)
    m(2,0)
    m(3,90)
    m(4,180)
    m(5,-90)
    

def plongeur():
    m(1,-20)
    m(2,-45)
    m(3,45)
    m(4,0)
    m(5,-60)
    
    
def balai_brosse():
    m(1,90,wait=True)
    m(2,-70,wait=True)
    m(3,10,wait=True)
    m(4,180,wait=True)
    m(5,-90,wait=True)
    sleep(1)
    m(1,270,wait=True)
    sleep(1)
    m(1,90,wait=True)
    

def shaker():
    m(1,0)
    m(2,0)
    m(3,0)
    m(4,0)
    m(5,90,wait=True)
    sleep(1)
    m(1,360,5)
    m(5,0,wait=True)
    m(5,90,wait=True)
    m(5,0,wait=True)
    m(5,90,wait=True)
    m(5,0,wait=True)
    m(5,90,wait=True)
    

def looping():
    m(1,0)
    m(2,-90)
    m(3,0)
    m(4,0)
    m(5,90,wait=True)
    sleep(1)
    m(2,0)
    m(3,-90)
    m(5,-90)
