#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:07:41 2024

@author: henrynelson
"""

import numpy as np
def main ():
    codex = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,"k": 11,"l": 12,"m": 13,"n": 14,
         "o": 15,"p": 16,"q": 17,"r": 18,"s": 19,"t": 20,"u": 21,"v": 22,"w": 23,"x": 24,"y": 25, "z": 26, " ":27, ",":28, ".":29, "?":30, "A": 31, "B": 32, "C": 33, "D": 34, "E": 35, "F": 36, "G": 37, "H": 38, "I": 39, "J": 40,"K": 41,"L": 42,"M": 43,"N": 44,
              "O": 45,"P": 46,"Q": 47,"R": 48,"S": 49,"T": 50,"U": 51, "V": 52,"W": 53,"X": 54,"Y": 55, "Z": 56, "!":57}
   
    first = (input("message or file: "))
    if first == ("file"):
       T = open((str(input("file: "))), "r") #file input, reads it

    if first == ("message"):  
        T= input(str("Sentence to be encrypted:")) #sentence imput
                                                                                            #letters =['"{}"' .format(letter) for letter in letters]
                                                                                                #V = ("'{}'".format(H)) #puts each letter in quotes 
                                                                                                        #print(codex.get(V)) DOES NOT WORK, codex get doesnt take lists
    enclist = [] #starts a new open list
    letters = list([x for x in T])   #turns sentence into list of letters, 'x'
    for key in letters:
           enclist.append(codex[key])# appends enclist to include values                            #THIS DOESNT WORK num = (codex.get(key)) #numerical valuefor each original letter    
    encarray = np.array(enclist) #turns enclist into an array                                        #num.join() does not work!
  
    D= (encarray+17)   #This is the line that decides the encription
    print(D)
if __name__ == '__main__':
    main()