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
from my_rich_text import myrich

def checkInteger(s):
    # our created pattern to check for the integer value
    if re.match('^[+-]?[0-9]+$', s):
        return True
    else:
        return False
#==================================================================
def capture_print():
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    return new_stdout

def restore_print(old_stdout):
    sys.stdout = old_stdout
    
    # Example usage:
    # captured_stdout = capture_print()
    # print("Hello, world!")
    # print("This is another line.")
    # restore_print(captured_stdout)
    
#==================================================================

print(chr(27) + "[2J")

print( colors.fg.lightred, "...")

sCMD=''
result_List=[]
collections_List=[]
game_lists_List=[]

#-------------------------------------------------------------------------------

    
myconsole=myrich('[bold magenta]Left Window[/bold magenta]\n','[bold cyan]Right Window[/bold cyan]\n','COMMANDS','RESULTS',120)
myconsole.clear_console
myconsole.refresh_console()

captured_stdout = capture_print()

s2c.Help('123456789')

sPrintText=captured_stdout.getvalue()  #string_io.getvalue()
myconsole.print_right(sPrintText)  
myconsole.refresh_console()

restore_print(captured_stdout)


#-------------------------------------------------------------------------------
while(sCMD!='x'):
      
    print( colors.fg.yellow, colors.cursor.blinkon, ":")   
    sCMD = str(input('Command:'))    ##   s space+invaders
    print( colors.cursor.blinkoff, "")
    if sCMD =='':
        sCMD='?'
        
    sCMD_LINE=sCMD.split(' ') 
    
    sCOMMAND=sCMD_LINE[0]
    sPARAMETERS=''
    sPARAMETERS=sCMD.replace(sCOMMAND+' ','')
    
#    print( 'Command='+ sCOMMAND)
#    print( 'Parameters='+ sPARAMETERS)
    print( colors.fg.pink, "")
###################################################################
###----search commands---------------------------------------------------       
    if sCOMMAND=='s':
           print( colors.fg.lightblue, "...")
           result_List=s2c.Makeplaylist(sPARAMETERS,'s')   
           
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

    elif  sCOMMAND=='ls':  
          print( colors.fg.lightred, "...")
          game_lists_List= s2c.DisplayGameLists()
          print()
          s2c.Help('2')

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
