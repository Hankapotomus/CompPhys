#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:47:37 2024

@author: henrynelson
"""

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
   
    TintTime = (str(input("Orbital period in minutes:, hours, or days: ")))  #asks for input in 3 forms
   
    if (TintTime[-8:]) == (" minutes"):  #if last 8 letters are minutes, then...
        Tintminute= ((TintTime[:-8]))  #takes numerical value
        Tint= (float(Tintminute)*60)   #multiplies minutes into seconds
    if (TintTime[-6:]) == (" hours"):#if last 6 letters are hours, then...
       Tinthour= (TintTime[:-6])    #takes numerical value
       Tint= (float(Tinthour)*3600)    #multiplies hours into seconds
    if (TintTime[-5:]) == (" days"):  #if last 5 letters are days, then....
        Tintday= (TintTime[:-5])      #takes numerical value
        Tint= (float(Tintday)*86400)    #multiplies days into seconds
    Tint = np.array(Tint)  #turns float into array
  
 
    height= (((Grav*Mass*((Tint)**2)/(4*(math.pi)**2))**(1/3))-Rad)/1000 #this is the equation, with T multiplied by 60 to get the seconds, and /1000 at the end to get an answer in km
    height=  np.round([height], decimals = 0)#this rounds the answer to nearest kilometer
   
    if height < 0: #if period is impossible
        print("orbit is not possible")
    if height > 0: #if period is possible
        print (height, "kilometers") 
        #this value is the height in km required for an object of T period to orbit
   
    question = (str(input("Do you want to test another period? y or n: "))) #asks if want to repeat program
   
    
    if question == ("y"): #if input is n, nothing happens, if yes, next fuction
        return(main())    #restarts program
        
        
        
if __name__ == '__main__':
    main ()
