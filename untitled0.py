#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:50:25 2024

@author: henrynelson
"""

import math as mp 
import numpy as np
import matplotlib.pyplot as mp


def main ():
    
    def rising1D(v0,g=9.8):
        h = v0**2/(2*g)
        t = v0/g
        return h,t



    def falling1D(h,v0=0):
    # returns the time and velocity of an object falling from h and at an initial velocity v0
        g=9.8
    #solution to quadratic equation
        time = -v0/g + mp.sqrt(v0**2/g**2+2*h/g)
        velo = mp.sqrt(v0**2+2*g*h)
        return time,velo

    def projectile(v0, angle, h):
        deg2rad = lambda ang: ang*mp.pi/180
        angle = deg2rad(angle)
        vx= v0*mp.cos(angle)
        vy0 = v0*mp.sin(angle)
        [h1, t1] = rising1D(vy0)
        maxh = h + h1
        [t2, vf] = falling1D(maxh)
        time = t1 + t2
        print(time)
        rang = vx*time
        print(rang)
     

        return time, round(rang)

        plotP = mp.plot(time,rang,'r--.')
        mp.xlabel("time")
        mp.ylabel("range")
        plotP.show()

#t should take the launch velocity and launch angle, return the range and maximum height, and produce the trajectory graph

if __name__ == '__main__':
    main()

