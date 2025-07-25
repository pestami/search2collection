# input#-------------------------------------------------------------------------------
# Name:      search2collection.py
# Purpose:
#
# Author:      MPA
#
# Created:     2024 05 03
#
#-------------------------------------------------------------------------------
import sqlite3
from colors import colors
import os
import re
from xml.dom.minidom import parse
import xml.dom.minidom

class s2c_r:

#-------------------------------------------------------------------------------
    
#============================================================================
#============================================================================
# ID='0123456789'0-clscr; 1-heading; 2-systems; 3-collections; 4-search keywrd; 5-save search; 6-admin
# Help(ID)     
# black; red; green; yellow; blue; magenta; cyan; white; bright_black; bright_red; bright_green; 
# bright_yellow; bright_blue; bright_magenta; bright_cyan; bright_white
    def Help(ID): 
        
            sHelp=""
            
            if ID=='':
                ID='0123456789'
            #sHelp+=chr(27) + "[2J")
            
            if '0' in ID:
                os.system('cls||clear')
                os.system('cls||clear')
                
            if '1' in ID:
                sHelp+= '[green]'
                sHelp+='=========================================================='
                sHelp+='\n==Program to generate a playlist=======V20250613=========='
                sHelp+='\n=========================================================='
                sHelp+= '[/green]'
           
            if '2' in ID:
                #sHelp+= colors.fg.lightred
                sHelp+='[magenta]'
                sHelp+='\n\n..UPDATE SEARCH DATABASE..............................'
                sHelp+='\ntype ls to list installed game Systems (MAME ,ATARI etc.)'
                sHelp+='\ntype ws to scrape Systems information to Search-DataBase'
                sHelp+='\ntype ds <item> to delete a Systems from the search DataBase'
                sHelp+= '[/magenta]'
           
            if '3' in ID:
                #sHelp+= colors.fg.purple, "...")
                sHelp+= '[cyan]'
                sHelp+='\n\n..MANAGE COLLECTIONS...................................'
                sHelp+='\ntype lc to list collections'
                sHelp+='\ntype dc <item> to delete a collection'
                sHelp+= '[/cyan]'
           
            if '4' in ID:
                #sHelp+= colors.fg.lightblue, "...")
                sHelp+= '[yellow]'
                sHelp+='\n\n..SEARCH for ROMS.....................................'
                sHelp+='\ntype s keyword1+keyword2 to search for game in Name of ROM'
                sHelp+='\ntype sd keyword1+keyword2 to search for games in description'
                sHelp+= '[/yellow]'
            
            if '5' in ID:
                #sHelp+= colors.fg.lightblue, "...")
                sHelp+= '[bright_white]'
                sHelp+='\n\n..SEARCH RESULTS.......................................'
                sHelp+='\ntype l  list last plalists resulting from Search criteria'
                sHelp+='\ntype wr to write playlist to a collection list then rename'
                sHelp+='\ntype w  to write playlist to default named collection list'
                sHelp+= '[/bright_white]'
           
            if '6' in ID:
                #sHelp+= colors.fg.green, "...")
                sHelp+= '[green]'
                sHelp+='\n\n.......................................................'
                sHelp+='\ntype h  to help'
                sHelp+='\ntype x  to quit'
                sHelp+='\n\n=========================================================='
                sHelp+= '[/green]'
                
            return sHelp
#-------------------------------------------------------------------------------
#============================================================================
#===========================================================================
    def DisplayGameLists():
               
                pathcollections='/home/pi/.emulationstation/gamelists/'
                sGameLists=''

                dir_list = os.listdir(pathcollections)
                i=0
               
                # prints all files
                # os.system('cls||clear')
                # sGameLists+='..................................\n'
                # sGameLists+='-----GAME Lists FOUND---------------\n'
                # sGameLists+="Directory= \n"
                # sGameLists+= pathcollections +'\n'
                
                for sfiles in dir_list:                   
                    sGameLists+=str(i) + ":" + sfiles +'\n'
                    i=i+1
                    
                return sGameLists
#-------------------------------------------------------------------------------

#===========================================================================
#============================================================================
    def Displaylist(result_List):
        
        #print(chr(27) + "[2J")
        os.system('cls||clear')
        
        sCMD=''
        sDisplaylist=''
        
        while sCMD != 'x' and sCMD != 'X':
            
           
            sDisplaylist+='------------------------------'
            sDisplaylist+='-----KEWORDS FOUND LIST-------'
            sFound=str(len(result_List))
            
           
            i=0
            nTotal=0
            for items in result_List:
                i=i+1
                nTotal=nTotal+1
                sDisplaylist+=str(nTotal)+' : ' + items[0]
               
                if i==25:
                    i=0
                    print( colors.fg.lightblue, "...")
                    sPRINT='\nDisplayed: ' +str(nTotal) +'/'+ sFound +'  Press key to continue, x to exit.........'
                    sDisplaylist+=sPRINT
                    
                    
                    sCMD = str(input())   
                    if sCMD =='x' or sCMD =='X':
                        break
            
        print('-----KEWORDS FOUND END-------------------')      
        print('---------------------------------------------------------')
    
        return sDisplaylist 
    
#-------------------------------------------------------------------------------
#============================================================================
#============================================================================
   


#============================================================================
#============================================================================
        
###############################################################################
if __name__ == '__main__':
    
    print ("======================================================")
    print ("TEST CODE s2c_search.py===============================")
    print ("======================================================")
    
    temp=s2c_r.Help('123456789')
    print (temp)
    
    
    print ("======================================================")