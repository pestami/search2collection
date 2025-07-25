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
    def Help(ID): 
        
            sHelp=""
            
            if ID=='':
                ID='0123456789'
            #sHelp+=chr(27) + "[2J")
            
            if '0' in ID:
                os.system('cls||clear')
                os.system('cls||clear')
                
            if '1' in ID:
                sHelp+= colors.fg.green
                sHelp+='\n=========================================================='
                sHelp+='\n==Program to generate a playlist=======V20250613=========='
                sHelp+='\n=========================================================='
           
            if '2' in ID:
                sHelp+= colors.fg.lightred
                sHelp+='\n\n..Update Search DataBase................................'
                sHelp+='\ntype ls to list installed game Systems (MAME ,ATARI etc.)'
                sHelp+='\ntype ws to scrape Systems information to Search-DataBase'
                sHelp+='\ntype ds <item> to delete a Systems from the search DataBase'
           
            if '3' in ID:
                #sHelp+= colors.fg.purple, "...")
                sHelp+='\n.............................................'
                sHelp+='\ntype lc to list collections'
                sHelp+='\ntype dc <item> to delete a collection'
           
            if '4' in ID:
                #sHelp+= colors.fg.lightblue, "...")
                sHelp+='\n\n..SEARCH for ROMS......................................'
                sHelp+='\ntype s keyword1+keyword2 to search for game in Name of ROM'
                sHelp+='\ntype sd keyword1+keyword2 to search for games in description'
            
            if '5' in ID:
                #sHelp+= colors.fg.lightblue, "...")
                sHelp+='\n\n..SEARCH RESULTS.......................................'
                sHelp+='\ntype l  list last plalists resulting from Search criteria'
                sHelp+='\ntype wr to write playlist to a collection list then rename'
                sHelp+='\ntype w  to write playlist to default named collection list'
           
            if '6' in ID:
                #sHelp+= colors.fg.green, "...")
                sHelp+='\n\n........................................................'
                sHelp+='\ntype h  to help'
                sHelp+='\ntype x  to quit'
                sHelp+='\n\n=========================================================='
                
            return sHelp
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
    
    temp=s2c_r.Help('0123456789')
    print (temp)
    
    
    print ("======================================================")