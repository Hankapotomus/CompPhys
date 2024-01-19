#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:06:27 2024

@author: henrynelson
"""

import math #to use math.pi
import numpy as np
#altitudes of satelites based on period
def main ():
    R= 6.3781*(10**6)  #Earths radius #in meters
    G= 6.6743*(10**-11) #Newton gravitational constant
    M= 5.97219*(10**24) #Mass of earth #in kg
    h= 60 # this is here so I can imout either minutes or hours * h
    Min= [94,4*h,6*h,24*h] #imput 94 min, then 4 * h, etc.
   
    T= np.array(Min) #turns the list into an array
    
    height= (((G*M*((T*60)**2)/(4*(math.pi)**2))**(1/3))-R)/1000
    
    height=  np.round([height], decimals = 0)
    #this rounds the answer to nearest kilometer
    

    print (height) 
    return(height) #this value is the height in km required for an object of T period to orbit

if __name__ == '__main__':
    main (),
