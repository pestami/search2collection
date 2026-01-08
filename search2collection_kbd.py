# input#-------------------------------------------------------------------------------
# Name:      search2collection.py
# Purpose:
#
# Author:      MPA
#
# Created:     2024 05 03
# Created:     2025 08 16
#
#Modules required rich pip3 install rich
#-------------------------------------------------------------------------------
import sqlite3
import os
import re,sys,io

##sPathFileDB='/home/pi/RetroPie/roms/ports/search2collection/SearchRetroRoms.db'
##
##con = sqlite3.connect(sPathFileDB)
##con.text_factory = str
##cur = con.cursor()

from colors import colors
from s2c_search_rich import s2c_r
from s2c_db import s2c_db
from keyboard_s2c import Keyboard
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
result_List='Search results are empty please use: commnad=s\n to create a search results set. ' # sql results from search
sResults_Text='Search results are empty '
collections_List=[]
game_lists_List=[]
tResults=''
scrollable_step=15
scrollable_page=0

sResultsTitle="RESULTS"

#-------------------------------------------------------------------------------
for i in range(50):
    ResultLists.append("LINE= " +str(i))
    sResults_Text+=str(i)+ " Result..." + str(i) +"\n"

#-------------------------------------------------------------------------------

# left_text_panel = Panel(Scrollable(("...", title="RESULTS").height=20)
# right_text_panel = Panel("...", title="COMMANDS",.height=20)
# console.print(Columns([left_text_panel, right_text_panel]))

#print(chr(27) + "[2J")  # no clear screen in rich
os.system('cls||clear')

sHelp=s2c_r.Help('123456789')
sHelpLeft='\n=========================================================='
sPannelText=sListToText(ResultLists, 0,20)

# right_text_panel = Panel(sHelp, title="COMMANDS")
# left_text_panel = Panel(sPannelText, title="RESULTS")
# console.print(Columns([left_text_panel, right_text_panel]))
# console.print(Columns([left_text_panel, right_text_panel]))

#-------------------------------------------------------------------------------
#---------MAIN LOOP-------------------------------------------------------------
#-------------------------------------------------------------------------------
sFOOTER=''
sHEADER=''
sBODY=''

console.print('Press k to use Keyboard for text input:\n Press ENTER to cuse JOYSTICK for text input:')
sCMD = console.input("Your Response: ")
print(": " + sCMD)
gui_interface='joystick'
if sCMD.lower()=='k':
    gui_interface='keyboard'

if gui_interface=='joystick':
    keyboard = Keyboard()

while(sCMD!='x'):

    if sResults_Text :
        sHEADER='[green]Page: '+str(scrollable_page)+' Press to scroll: u-up d-down [/green]\n\n'
        ResultLists=sTextToList(sResults_Text)
        ResultListsSize=len(ResultLists)
        sBODY=sListToText(ResultLists,scrollable_step *scrollable_page,scrollable_step *(scrollable_page+1))
    
    if "\n[green]" not in sFOOTER:
        sFOOTER='\n'+'[green]'+ sFOOTER +'[/green]' #

    sPannelText=sHEADER + sBODY +sFOOTER
    #----------------------------------------------------------------------

    #-----SHOW PANNEL------------------------------------------------------
    right_text_panel = Panel(sHelp, title="COMMANDS",height=30,width=65)
    left_text_panel = Panel(sPannelText, title=sResultsTitle,height=30,width=65)
    console.print(Columns([left_text_panel, right_text_panel]))
    #----------------------------------------------------------------------

    
##    sPannelText = keyboard.draw_keyboard_textvar((1,1))
##
##    keyboard_panel = Panel(sPannelText, title=sResultsTitle,height=6,width=65)
##    console.print(Columns([keyboard_panel]))

    #-----COMMANDLINE------------------------------------------------------
    
    if gui_interface=='keyboard':
        #sCMD = str(input('Command:'))    ##   s space+invaders
        sCMD = console.input("Command: ")
        print(": " + sCMD)
    
    if gui_interface=='joystick':
        sCMD= keyboard.draw_keyboard_loop()
        sCMD=sCMD.lower()

   
    # print( colors.cursor.blinkoff, "")
    if sCMD =='':
        sCMD='?'

    sCMD_LINE=sCMD.split(' ')

    sCOMMAND=sCMD_LINE[0]

    if len(sCMD_LINE) > 1:
        sCMD_PARAMETERS=sCMD_LINE[1]
    else:
        sCMD_PARAMETERS=''

    # sCMD_PARAMETERS=sCMD.replace(sCOMMAND+' ','') # works for with or without parameter
    #----------------------------------------------------------------------

    os.system('clear')


###################################################################

###----search commands---------------------------------------------------
    if sCOMMAND=='s' and sCMD_PARAMETERS:   # ----------------------------------MIGRATED

           result_List,sMessage,lGamesRomCollectionsList =s2c_r.Makeplaylist(sCMD_PARAMETERS,'s')
           sResultsTitle='SEARCH SQL RESULTS'
           sResults_Text=sMessage
           sFOOTER=  s2c_r.Help('5')



###----scroll commands---------------------------------------------------
    elif sCOMMAND=='d':
              scrollable_page+=1
              if ResultListsSize < scrollable_step *scrollable_page:
                  scrollable_page=0


    elif sCOMMAND=='u':
                  scrollable_page-=1
                  if scrollable_page ==-1:
                      scrollable_page=0

    elif sCOMMAND=='sd': # ----------------------------------MIGRATED

           result_List,sMessage,lGamesRomCollectionsList =s2c_r.Makeplaylist(sCMD_PARAMETERS,'sd')
           # lGamesRomCollectionsList the list required for gamelist
           sResultsTitle='SEARCH SQL RESULTS'
           sResults_Text=sMessage
           sFOOTER=  s2c_r.Help('5')


###-----Write Commands--------------------------------------------------
    elif sCOMMAND=='ws':# ----------------------------------MIGRATED

            #--- parameters
            #print( colors.fg.lightblue, "...")
            if checkInteger(sCMD_PARAMETERS):
                sSystemName= game_lists_List[int(sCMD_PARAMETERS)]


                #--- Get ROMS in FOLDER
                #--require gameslisting to ensure games listed in gameslists realy exist
                sPathROMS="/home/pi/RetroPie/roms/"+sSystemName
                sPathNameGamelist='/home/pi/.emulationstation/gamelists/' + sSystemName + '/gamelist.xml'

                sFOOTER= "Your selection= " + sSystemName +'\n'

                lLIST_XML_GAMESLISTS_Metadata,lgames,nSizeGamelist = s2c_db.ExtractMetadatefromGameXML(sPathNameGamelist,sPathROMS,flagDebug=False)

                # print(lLIST_XML_GAMESLISTS_Metadata[0])

                sROMCOUNT=str(len(lLIST_XML_GAMESLISTS_Metadata))

                sFOOTER+= ".......................................\n"
                sFOOTER+= "Number of ROMS Detected in folder=" + str(len(lgames))+'\n'
                sFOOTER+= "Number of ROMS Listed in gamelist=" + str(nSizeGamelist)+'\n'
                sFOOTER+= "The Name of Game and Description of " + sROMCOUNT + " ROMS \n"
                sFOOTER+= 'were loaded into search DB \n'
                sFOOTER+= ".......................................\n"

                sConsole=sSystemName
                sPathFileDB="/home/pi/RetroPie/roms/ports/search2collection/SearchRetroRoms.db"
                s2c_db.ROM_DB_LoadGameListsContents(sPathFileDB,lLIST_XML_GAMESLISTS_Metadata,sConsole)

            else:
                # print ("Argument is missing, example: ws 1")
                sFOOTER="WS: Argument is missing, example: ws 1"


###-----Write Commands--------------------------------------------------

    elif  sCOMMAND=='w':   # ----------------------------------MIGRATED IN WORK
          # print( colors.fg.lightblue, "...")
          sMessage= s2c_r.WriteToCollection(lGamesRomCollectionsList)

          sResultsTitle='COLLECTION CREATION'
          sResults_Text=sMessage
          sFOOTER=  s2c_r.Help('5')

    elif  sCOMMAND=='wr' and sCMD_PARAMETERS:  # ----------------------------------MIGRATED IN WORK
          # print( colors.fg.lightblue, "...")
          sMessage= s2c_r.WriteToCollectionRename(lGamesRomCollectionsList,sCMD_PARAMETERS)

          sResultsTitle='COLLECTION CREATION'
          sResults_Text=sMessage
          sFOOTER=  s2c_r.Help('5')

###-----list Commands--------------------------------------------------

    elif  sCOMMAND=='l':   # ----------------------------------MIGRATED

             sResults_Text=result_List
             nLen=sResults_Text.count('\n')
             sResultsTitle=str(nLen) + ' SEARCH RESULTS LISTED'
             scrollable_page=0
             sFOOTER=s2c_r.Help('5')

    elif  sCOMMAND=='lc':  # ----------------------------------MIGRATED

              sResults_Text,collections_List=s2c_r.DisplayCollections()
              sResultsTitle='/home/pi/.emulationstation/collections/'
              scrollable_page=0
              sFOOTER=s2c_r.Help('3')

    elif  sCOMMAND=='ls':    # ----------------------------------MIGRATED
              sResults_Text,game_lists_List=s2c_r.DisplayGameLists()
              sResultsTitle='/home/pi/.emulationstation/gamelists/'
              scrollable_page=0
              sFOOTER=s2c_r.Help('2')


###-----delete Commands--------------------------------------------------

    elif  sCOMMAND=='dc':   # ----------------------------------MIGRATED

              sMessage= s2c_r.DeleteCollection(collections_List,sCMD_PARAMETERS)
              sFOOTER=s2c_r.Help('3') +sMessage

    elif  sCOMMAND=='ds':
          # print( colors.fg.lightred, "...")
          s2c_r.DeleteSystem(sPathFileDB,sCMD_PARAMETERS)
          s2c_r.Help('5')

###-----System Commands--------------------------------------------------
    elif  sCOMMAND=='h':
          print( colors.fg.green, "...")
          s2c_r.Help('')

    elif  sCOMMAND=='x':
          print( colors.fg.yellow, "...")
          print('Good Bye, enjoy your games.')
          print('Remember:')
          print('1. : restart emulationstation !')
          print('2. : Ensure collection is set visible !')
          sDUMMY = str(input('press any key to continue:'))

    elif  sCOMMAND=='?':
          s2c_r.Help('')

    else:
        sResults_Text='[red]'
        sResults_Text+='...........................................\n'
        sResults_Text+='Unkown command =' + sCMD +'\n'
        sResults_Text+='With Parameters =' + sCMD_PARAMETERS +'\n'
        sResults_Text+='...........................................\n'
        sResults_Text+='[/red]'

######################################################################
sDUMMY = input('press any key to continue:')   ##  final wait
#-------------------------------------------------------------------------------
#con.commit()
#con.close()
#print('=======================================')
#print('==CLOSED===============================')
#print('=======================================')