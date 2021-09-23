#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:03:12 2021
@author: Tom LUCAS
"""

from pypot import vrep
from pypot.creatures import PoppyErgoJr
from time import sleep, time



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
    
def sky_watching(t=2):
    ms({
        1:180,
        2:0,
        3:0,
        4:90,
        5:-90
    },t, wait=True)
    sleep(2)


def reverse(t=2):
    ms({
        1:180,
        2:0,
        3:90,
        4:180,
        5:-90
    },t, wait=True)
    sleep(2)
    

def plongeur(t=2):
    ms({
        1:-20,
        2:-45,
        3:45,
        4:0,
        5:-60
    },t, wait=True)
    sleep(2)
    
    
def balai_brosse(t=2,t2=2):
    ms({
        1:90,
        2:-70,
        3:-10,
        4:180,
        5:-90
    },t, wait=True)
    m(1,270,t=t2,wait=True)
    m(1,90,t=t2,wait=True)
    

def shaker(t=2,t2=20,t3=3):
    ms({
        1:0,
        2:0,
        3:0,
        4:0,
        5:90
    },t, wait=True)
    m(1,360,t2)
    for i in range(3):
        m(5,0,t3,wait=True)
        m(5,90,t3,wait=True)


def looping(t=2,t2=5):
    ms({
        1:0,
        2:-90,
        3:0,
        4:0,
        5:90
    },t, wait=True)
    ms({
        1:0,
        2:0,
        3:-90,
        4:0,
        5:-90
    },t2, wait=True)
    
def back_brosse(t=2,t2=15):
    ms({
        1:180,
        2:0,
        3:90,
        4:0,
        5:-90
    },t, wait=True)
    ms({
        1:360,
        2:0,
        3:90,
        4:-180,
        5:-90
    },t2, wait=True)
    ms({
        1:0,
        2:0,
        3:90,
        4:0,
        5:-90
    },t2, wait=True)
    
    
def burppp(t=2,t2=5):
    ms({
        1:0,
        2:0,
        3:90,
        4:180,
        5:-90
    },t, wait=True)
    ms({
        1:0,
        2:0,
        3:-90,
        4:0,
        5:-90
    },t2, wait=True)
    
def end_style(t=2,t2=6,t3=8):
    ms({
        1:180,
        2:0,
        3:90,
        4:180,
        5:-90
    },t, wait=True)
    for i in range(2):
        ms({
            1:180,
            2:0,
            3:90,
            4:-90,
            5:-90
        },t2, wait=True)
        ms({
            1:180,
            2:0,
            3:90,
            4:90,
            5:-90
        },t2, wait=True)
    ms({
        1:0,
        2:0,
        3:90,
        4:180,
        5:-90
    },t3, wait=True)
    
    
def start():
    ms({
        1:0,
        2:0,
        3:0,
        4:0,
        5:0
    },10, wait=True)
    sky_watching(10)
    back_brosse(7)
    looping(7)
    burppp(7,10)
    shaker(10,26,4)
    plongeur(12)
    balai_brosse(7,8)
    reverse(10)
    end_style(5)
    ms({
        1:0,
        2:0,
        3:0,
        4:0,
        5:0
    },10, wait=True)
    
def timed():
    start_time = time()
    start()
    print("Temps : " + str(time() - start_time))
    
timed()
