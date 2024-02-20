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
    Rad= 6.3781*(10**6)  #Earths radius #in meters
    Grav= 6.6743*(10**-11) #Newton gravitational constant
    Mass= 5.97219*(10**24) #Mass of earth #in kg
   
   
   
    Tint = int(input("Orbital period in minutes: "))
   
    height= (((Grav*Mass*((Tint*60)**2)/(4*(math.pi)**2))**(1/3))-Rad)/1000
    #this is the equation, with T multiplied by 60 to get the seconds, and /1000 at the end to get an answer in km
    
    height=  np.round([height], decimals = 0)
    #this rounds the answer to nearest kilometer
    

    print (height) 
    return(height) #this value is the height in km required for an object of T period to orbit

if __name__ == '__main__':
    main ()
