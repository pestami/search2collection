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
import os
import re,sys,io

sPathFileDB='/home/pi/RetroPie/roms/ports/search2collection/SearchRetroRoms.db'

con = sqlite3.connect(sPathFileDB)
con.text_factory = str
cur = con.cursor()

from colors import colors
from s2c_search import s2c
from s2c_search_rich import s2c_r
# from my_rich_text import myrich

from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
#from rich.scrollable import Scrollable # not in rich
import os

console = Console()
#==================================================================
    
#==================================================================
def checkInteger(s):
    # our created pattern to check for the integer value
    if re.match('^[+-]?[0-9]+$', s):
        return True
    else:
        return False
#------------------------------------------------------------------
def sListToText(sList,nStart,nEnd):
    
    sList=sList[nStart:nEnd]
    sText=''
    
    for line in sList:
        sText+=line +'\n'
    return sText

def sTextToList(sText):
    
    sList=sText.split('\n')
    
    return sList    
    
#==================================================================
    
#==================================================================

# print(chr(27) + "[2J")  # no clear screen in rich



sCMD=''
ResultLists=[]
sResults_Text=''
collections_List=[]
game_lists_List=[]
tResults=''
scrollable_step=10
scrollable_page=0

sResultsTitle="RESULTS"

#-------------------------------------------------------------------------------
for i in range(50):
    ResultLists.append("LINE= " +str(i))
    sResults_Text+=str(i)+ " Result..." + str(i) +"\n"
    
#-------------------------------------------------------------------------------

# left_text_panel = Panel(Scrollable(("...", title="RESULTS"))
# right_text_panel = Panel("...", title="COMMANDS")
# console.print(Columns([left_text_panel, right_text_panel]))

#print(chr(27) + "[2J")  # no clear screen in rich
os.system('cls||clear')

sHelp=s2c_r.Help('123456789')
sHelpLeft='\n=========================================================='
sPannelResults=sListToText(ResultLists, 0,15)

# right_text_panel = Panel(sHelp, title="COMMANDS")
# left_text_panel = Panel(sPannelResults, title="RESULTS")
# console.print(Columns([left_text_panel, right_text_panel]))
# console.print(Columns([left_text_panel, right_text_panel]))

#-------------------------------------------------------------------------------
while(sCMD!='x'):
    
    ResultLists=sTextToList(sResults_Text)
    ResultListsSize=len(ResultLists)
    sPannelResults=sListToText(ResultLists,scrollable_step *scrollable_page,scrollable_step *(scrollable_page+1))
    sPannelResults='Press to scroll: u-up d-down \n'+ sPannelResults + '\n'+sHelpLeft
    # print (scrollable_step *scrollable_page)
    # print (scrollable_step *(scrollable_page+1))
    #sPannelResults=sListToText(ResultLists,10,20)
        
    right_text_panel = Panel(sHelp, title="COMMANDS")
    left_text_panel = Panel(sPannelResults, title=sResultsTitle)
    console.print(Columns([left_text_panel, right_text_panel]))
       

    # sCMD = str(input('Command:'))    ##   s space+invaders
    sCMD = console.input("Command: ")
    
    os.system('cls||clear')
    
    
    # print( colors.cursor.blinkoff, "")
    if sCMD =='':
        sCMD='?'
        
    sCMD_LINE=sCMD.split(' ') 
    
    sCOMMAND=sCMD_LINE[0]
    sPARAMETERS=''
    sPARAMETERS=sCMD.replace(sCOMMAND+' ','')
    

###################################################################
         
###----search commands---------------------------------------------------       
    if sCOMMAND=='s':
           print( colors.fg.lightblue, "...")
           result_List=s2c.Makeplaylist(sPARAMETERS,'s')   
           
###----scroll commands--------------------------------------------------- 
    elif sCOMMAND=='d':
              scrollable_page+=1
              if ResultListsSize < scrollable_step *scrollable_page:
                  scrollable_page=0
                  
              
    elif sCOMMAND=='u':
                  scrollable_page-=1
                  if scrollable_page ==-1:
                      scrollable_page=0
           
    elif sCOMMAND=='sd':
           print( colors.fg.lightblue, "...")
           result_List=s2c.Makeplaylist(sPARAMETERS,'sd')   
           
###-----Write Commands--------------------------------------------------  
    elif sCOMMAND=='ws':
            
            #--- parameters
            print( colors.fg.lightblue, "...")
            if checkInteger(sPARAMETERS):            
                sSystemName= game_lists_List[int(sPARAMETERS)]
           
            
                #--- Get ROMS in FOLDER
                #--require gameslisting to ensure games listed in gameslists realy exist
                sPathROMS="/home/pi/RetroPie/roms/"+sSystemName       
                sPathNameGamelist='/home/pi/.emulationstation/gamelists/' + sSystemName + '/gamelist.xml'
                
                print ("Your selection= " + sSystemName)
                
                lLIST_XML_GAMESLISTS_Metadata,lgames =s2c.ExtractMetadatefromGameXML(sPathNameGamelist,sPathROMS)   
               # print(lLIST_XML_GAMESLISTS_Metadata[0])
               
                print ("..................................................................\n")
                print ("Number of ROMS Detected in folder=" + str(len(lgames)))
                print ("Number of ROMS Listed in gamelist=" + str(len(lLIST_XML_GAMESLISTS_Metadata)))
                print ("..................................................................\n")
                
                console=sSystemName
                sPathFileDB="/home/pi/RetroPie/roms/ports/search2collection/SearchRetroRoms.db"             
                s2c.ROM_DB_LoadGameListsContents(sPathFileDB,lLIST_XML_GAMESLISTS_Metadata,console)
            else:
                print ("Argument is missing, example: ws 1")   
                
                
###-----Write Commands--------------------------------------------------  
        
    elif  sCOMMAND=='w':   
          print( colors.fg.lightblue, "...")
          s2c.WriteToCollection(result_List)          
          
    elif  sCOMMAND=='wr':  
          print( colors.fg.lightblue, "...")
          s2c. WriteToCollectionRename(result_List)      
    
###-----list Commands--------------------------------------------------          
          
    elif  sCOMMAND=='l':   
          print( colors.fg.lightblue, "...")
          s2c.Displaylist(result_List)
          s2c.Help('5')
          
    elif  sCOMMAND=='lc': 
          print( colors.fg.purple, "...")
          collections_List= s2c.DisplayCollections()
          s2c.Help('3')

    elif  sCOMMAND=='ls':    # ----------------------------------MIGRATED
          # print( colors.fg.lightred, "...")
          # game_lists_List= s2c.DisplayGameLists()
          sResults_Text=s2c_r.DisplayGameLists()
          
          sResultsTitle='/home/pi/.emulationstation/gamelists/'
          scrollable_page=0
          sHelpLeft=s2c_r.Help('2')
          # print()
          # s2c.Help('2')

###-----delete Commands-------------------------------------------------- 
          
    elif  sCOMMAND=='dc':  
          print( colors.fg.purple, "...")
          s2c.DeleteCollection(collections_List)
          s2c.Help('3')
          
    elif  sCOMMAND=='ds':   
          print( colors.fg.lightred, "...")
          s2c.DeleteSystem(sPathFileDB,sPARAMETERS)
          s2c.Help('5')

###-----System Commands--------------------------------------------------           
    elif  sCOMMAND=='h': 
          print( colors.fg.green, "...")
          s2c.Help('')
          
    elif  sCOMMAND=='x':   
          print( colors.fg.yellow, "...")
          print('Good Bye, enjoy your games.')
          print('Remember:')
          print('1. : restart emulationstation !')
          print('2. : Ensure collection is set visible !')
          sDUMMY = str(input('press any key to continue:'))    

    elif  sCOMMAND=='?':
          s2c.Help('')
          
    else:
        print('...........................................')
        print('Unkown command = ' + sCMD )
        print('With Parameters = ' + sPARAMETERS )
        
        
######################################################################        
sDUMMY = input('press any key to continue:')   ##  final wait
#-------------------------------------------------------------------------------
#con.commit()
#con.close()
#print('=======================================')
#print('==CLOSED===============================')
#print('=======================================')
