import discord
import random
from discord.ext import commands

def roller(num, dice, mult): #rolls "num" amount of "dice" sided dice and adds the results and multiplies it by "mult"
    total = 0
     
    for total in range(num):
        total += random.randint(1, dice)
    
    total *= mult
    
    return total

def table(type, id): #rolls a specific "id" loot table of given "type" 
    out = '' #output string that we will concatinate
    row = 0 #variable to control which "row" of the table is being used
    
    #initilize tables
    
    #individual monster tables
    itable1 = [[5, 6, 1, ' CP'], [4, 6, 1, ' SP'], [2, 6, 1, ' GP'], [3, 6, 1, ' GP'], [1, 6, 1, ' PP']]
    itable2 = [[4, 6, 100, ' CP'], [6, 6, 10, ' SP'], [2, 6, 10, ' GP'], [4, 6, 10, ' GP'], [3, 6, 1, ' PP']]
    itable3 = [[4, 6, 100, ' SP'],[1, 6, 100, ' GP'],[2, 6, 100, ' GP'],[2, 6, 10, ' PP']]
    itable4 = [[8, 6, 100, ' GP'],[1, 6, 1000, ' GP'],[2, 6, 100, ' PP']]
    
    d100 = roller(1, 100, 1)
    
    if(type == 'ind'):
        #choose table based on monster CR
        if(id <= 4):
            #determine which row of the table to use
            if(d100 > 30 and d100 <= 60): row = 1
            elif(d100 > 60 and d100 <= 70): row = 2
            elif(d100 > 70 and d100 <= 95): row = 3
            elif(d100 > 95): row = 4
            out += str(roller(itable1[row][0], itable1[row][1], itable1[row][2])) + itable1[row][3]
            
        elif(id > 4 and id <= 10):
            if(d100 > 30 and d100 <= 60): row = 1
            elif(d100 > 60 and d100 <= 70): row = 2
            elif(d100 > 70 and d100 <= 95): row = 3
            elif(d100 > 95): row = 4
            out += str(roller(itable2[row][0], itable2[row][1], itable2[row][2])) + itable2[row][3]
        
        elif(id > 10 and id < 17):
            if(d100 > 20 and d100 <= 35): row = 1
            elif(d100 > 35 and d100 <= 75): row = 2
            elif(d100 > 75): row = 3
            out += str(roller(itable3[row][0], itable3[row][1], itable3[row][2])) + itable3[row][3]
        elif(id >= 17):
            if(d100 > 20 and d100 <= 35): row = 1
            elif(d100 > 35 and d100 <= 75): row = 2
            elif(d100 > 75): row = 3
            out += str(roller(itable4[row][0], itable4[row][1], itable4[row][2])) + itable4[row][3]
    
    return out