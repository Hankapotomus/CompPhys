#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:08:35 2024

@author: henrynelson
"""

import numpy as np
def main ():
    codex = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,"k": 11,"l": 12,"m": 13,"n": 14,
         "o": 15,"p": 16,"q": 17,"r": 18,"s": 19,"t": 20,"u": 21,"v": 22,"w": 23,"x": 24,"y": 25, "z": 26, " ":27, ",":28, ".":29, "?":30, "A": 31, "B": 32, "C": 33, "D": 34, "E": 35, "F": 36, "G": 37, "H": 38, "I": 39, "J": 40,"K": 41,"L": 42,"M": 43,"N": 44,
              "O": 45,"P": 46,"Q": 47,"R": 48,"S": 49,"T": 50,"U": 51, "V": 52,"W": 53,"X": 54,"Y": 55, "Z": 56, "!":57}
   
    firstmessage = (input("message or file: "))
    if firstmessage == ("file"):
       Text = open((str(input("file: "))), "r") #file input, reads it

    if firstmessage == ("message"):  
        Text= input(str("Sentence to be encrypted:")) #sentence imput
                                                                                            #letters =['"{}"' .format(letter) for letter in letters]
                                                                                                #V = ("'{}'".format(H)) #puts each letter in quotes 
                                                                                                        #print(codex.get(V)) DOES NOT WORK, codex get doesnt take lists
    encryptionlist = [] #starts a new open list
    letters = list([letter for letter in Text])   #turns sentence into list of letters, 'letter'
    for key in letters:
           encryptionlist.append(codex[key])# appends enclist to include values                            #THIS DOESNT WORK num = (codex.get(key)) #numerical valuefor each original letter    
    encryptionarray = np.array(encryptionlist) #turns enclist into an array                                        #num.join() does not work!
    print (encryptionarray)  


    reversecodex = {y: x for x, y in codex.items()} #inverts the codex's keys and value
   
  
    
    GibberishNumbers= list(encryptionarray+17)   #This is the line that decides the encription
    print(GibberishNumbers)
    GibberishNumberslist=[]   #a new open list
    for value in  GibberishNumbers:
        if value > 57:  
            value= value-57   #if the value is over 57, it returns back to the range of accepted values
        ( GibberishNumberslist.append(reversecodex[value])) #Adds these new values to  GibberishNumberslist
    
    def convert( GibberishNumberslist): 
        new = "" 
        for x in  GibberishNumberslist: 
            new += x 
        return new #turns the  GibberishNumberslist list of letters into a string
    print(convert( GibberishNumberslist)) 
    
   
   


if __name__ == '__main__':
    main()
    
    
    
    
    