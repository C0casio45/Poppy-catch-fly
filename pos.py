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


def ms(m,t=2,wait=False):
    poppy.goto_position(
        {("m"+str(id)):value for id, value in m.items()},
        t,
        wait=wait
    )
    
def m(m,x,t=2,wait=False):
    ms({m:x},t,wait=wait)
    
def sky_watching():
    ms({
        1:180,
        2:0,
        3:0,
        4:90,
        5:-90
    }, wait=True)


def reverse():
    ms({
        1:180,
        2:0,
        3:90,
        4:180,
        5:-90
    }, wait=True)
    

def plongeur():
    ms({
        1:-20,
        2:-45,
        3:45,
        4:0,
        5:-60
    }, wait=True)
    
    
def balai_brosse():
    ms({
        1:90,
        2:-70,
        3:10,
        4:180,
        5:-90
    }, wait=True)
    sleep(1)
    m(1,270,wait=True)
    sleep(1)
    m(1,90,wait=True)
    

def shaker():
    ms({
        1:0,
        2:0,
        3:0,
        4:0,
        5:90
    }, wait=True)
    sleep(1)
    m(1,360,5)
    m(5,0,wait=True)
    m(5,90,wait=True)
    m(5,0,wait=True)
    m(5,90,wait=True)
    m(5,0,wait=True)
    m(5,90,wait=True)
    

def looping():
    ms({
        1:0,
        2:-90,
        3:0,
        4:0,
        5:90
    }, wait=True)
    sleep(1)
    ms({
        1:0,
        2:-90,
        3:-90,
        4:0,
        5:-90
    }, wait=True)
