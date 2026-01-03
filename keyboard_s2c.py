
import sqlite3
import os
import re,sys,io

from curses import wrapper
from curses.textpad import Textbox, rectangle
import curses
import sys


#===============================================================================
import os
## import msvcrt  # keypress  python3 -m pip install msvcrt..only windows
import termios
import sys
import tty


from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

console = Console()
#-------------------------------------------------------------------------------
class Keyboard:

    def __init__(self):
        # Define the keyboard layout
        self.keyboard_layout = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ,'ENTER'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P','CAPS'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '!','DEL'],
            ['Z', 'X', 'C', 'V', 'B', 'N', '<', '>', '[', ']','CLR'],
            ['-', '=', ',', '.', '/', ';', '\'', '{', '}']

        ]
        
        self.keyboard_layout = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ,'ENTER'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','CAPS'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '!','DEL'],
            ['z', 'x', 'c', 'v', 'b', 'n', '<', '>', '[', ']','CLR'],
            ['-', '=', ',', '.', '/', ';', '\'', '{', '}']

        ]

        self.strKEYBOARD =''
        self.focused_key = None
        self.strCOMMANDLINE =''

#-------------------------------------------------------------------------------
    def draw_keyboard_textvar(self, focused_key):
        # Print the keyboard layout
        strKEYBOARD=''
        for i, row in enumerate(self.keyboard_layout):
            row_str = ''
            for j, key in enumerate(row):

                if (i+1, j+1) == focused_key:
                    # Highlight the focused key with red foreground and yellow background
                    highlighted_key = f'\033[91;103m{key.center(3)}\033[0m'
                    highlighted_key = f'[magenta]{key.center(3)}[/magenta]'

                    row_str += highlighted_key
                elif key == '                                        ':
                    row_str += ' ' * 40
                else:
                    row_str += key.center(3)

            strKEYBOARD+=row_str + '\n'

        return strKEYBOARD
#-------------------------------------------------------------------------------
##    def set_focused_key(self, key_value):
##        for i, row in enumerate(self.keyboard_layout):
##            for j, key in enumerate(row):
##                if key == key_value:
##                    self.focused_key = (i, j)
##                    return
##        self.focused_key = None
#-------------------------------------------------------------------------------
    def get_focused_key_rowcol(self,nrow,ncol):

        return self.keyboard_layout[nrow-1][ncol-1]

#-------------------------------------------------------------------------------
    def draw_keyboard_terminal(self, key_value):
        # Print the keyboard layout
        strKEYBOARD=self.draw_keyboard_textvar(key_value)

        print(strKEYBOARD)
#-------------------------------------------------------------------------------
##    def draw_keyboard_2_string(self, key_value):
##        # Print the keyboard layout
##        self.set_focused_key( key_value)
##        strKEYBOARD=self.draw_keyboard_textvar(self.focused_key)
##
##        return strKEYBOARD
#-------------------------------------------------------------------------------
##    def draw_keyboard_2_string_rowcol(self, nrow,ncol):
##        # Print the keyboard layout
##        sKey=self.get_focused_key_rowcol(nrow,ncol)
##        strKEYBOARD=self.draw_keyboard_textvar(sKey)
##
##        return strKEYBOARD
    def read_keypress(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
#-------------------------------------------------------------------------------
    def draw_keyboard_loop(self):
         

       # keyboard = Keyboard()
        sCMD=''
        nROW=1
        nCOL=1
        sPannelText2=''
        sPannelText = self.draw_keyboard_textvar((nROW,nCOL))
        
        #-----COMMANDLINE------------------------------------------------------
        # sResultsTitle='KEYBOARD'
        # sResultsTitle2='TYPED'
        # keyboard_panel = Panel(sPannelText, title=sResultsTitle,height=8,width=40)
        # keyboard_panel2 = Panel(sPannelText2, title=sResultsTitle2,height=8,width=40)
        # #console.print(Columns([keyboard_panel]))
        # console.print(Columns([keyboard_panel, keyboard_panel2]))

        #-----COMMANDLINE------------------------------------------------------
        self.strCOMMANDLINE=''
        while(sCMD not in ['q','ENTER']):
            sCMD=''
            
            key =self.read_keypress()
            sCMD =key
            key=''
         
                
            if sCMD in ['2','x']:
                nROW+=1
            if nROW > 4:
                    nROW=1
            if sCMD in ['8','e']:
                nROW-=1
                if nROW == 0:
                        nROW=4
            if sCMD in ['4','s']:
                nCOL-=1
                if nCOL ==0:
                        nCOL=11
            if sCMD in ['6','d']:
                nCOL+=1
                if nCOL > 11:
                        nCOL=1
            if sCMD in ['5',' ']:
                sKey_virtual=self.get_focused_key_rowcol(nROW,nCOL)
                if len(sKey_virtual)==1:
                    self.strCOMMANDLINE+=self.get_focused_key_rowcol(nROW,nCOL)
                if sKey_virtual=='ENTER':
                    sCMD='ENTER'
                    #self.strCOMMANDLINE
                if sKey_virtual=='CLR':
                    self.strCOMMANDLINE=''
                if sKey_virtual=='DEL':
                    self.strCOMMANDLINE=self.strCOMMANDLINE[0:-1]

            sPannelText2=' ROW=' + str(nROW) + ' COLUMN=' + str(nCOL) +'\n sKey='+ sCMD +  '\n Command:'+ self.strCOMMANDLINE
            sPannelText = self.draw_keyboard_textvar((nROW,nCOL))
            
            #-------------------------------------------------------------------
            if sCMD in ['2','8','4','6','5','e','s','d','x',' ']:
                os.system('cls||clear')
                #sPannelText+='\nCOMMAND:' + self.strCOMMANDLINE
                #-----COMMANDLINE------------------------------------------------------
                                
                sResultsTitle='KEYBOARD'
                sResultsTitle2='TYPED'
                keyboard_panel = Panel(sPannelText, title=sResultsTitle,height=8,width=40)
                keyboard_panel2 = Panel(sPannelText2, title=sResultsTitle2,height=8,width=40)
                #console.print(Columns([keyboard_panel]))
                console.print(Columns([keyboard_panel, keyboard_panel2]))
        
                #-----COMMANDLINE------------------------------------------------------
            # print(f'sCMD={sCMD} ')
            # print(f'ROW={nROW} COLUMN={nCOL}')
            # print(f'TypedText={self.strCOMMANDLINE}')
            


        return self.strCOMMANDLINE
#===============================================================================
if __name__ == "__main__":


##    print('1---------------------------------')
##    keyboard = Keyboard()
##    print('2---------------------------------')
##    keyboard.draw_keyboard_terminal((1,1))
##    print('3---------------------------------')
##    sRES= keyboard.draw_keyboard_textvar((1,1))
##    print(sRES)
##    print('4---------------------------------')
##
##    print('5---------------------------------')

    os.system('cls||clear')
    keyboard = Keyboard()
    sCOMMANDLINE= keyboard.draw_keyboard_loop()
    print(f'COMMANDLINE={sCOMMANDLINE} ')

##    sCMD=''
##    nROW=1
##    nCOL=1
##    sCMD_STRING=''
##    os.system('cls||clear')
##    keyboard = Keyboard()
####    keyboard.draw_keyboard_terminal('A')
####
####    sKEYS= keyboard.draw_keyboard_2_string('A')
####    print(sKEYS)
##
##    while(sCMD!='x'):
##
##        #----------------------------------------------------------------------
##        keyboard = Keyboard()
####        sPannelText = keyboard.draw_keyboard_2_string(sCMD)
##        sPannelText = keyboard.draw_keyboard_2_string_rowcol(nROW,nCOL)
##        #-----COMMANDLINE------------------------------------------------------
##        sResultsTitle='KEYBOARD'
##        keyboard_panel = Panel(sPannelText, title=sResultsTitle,height=7,width=40)
##        console.print(Columns([keyboard_panel]))
##
##        # sCMD = str(input('Command:'))    ##   s space+invaders
####        sCMD = console.input("Command: ")
##        key = msvcrt.getch()
##        sCMD =key.decode()
##
##        os.system('cls||clear')
##
##        if sCMD =='2':
##            nROW+=1
##            if nROW > 4:
##                    nROW=1
##        if sCMD =='8':
##            nROW-=1
##            if nROW == 0:
##                    nROW=1
##
##        if sCMD =='4':
##            nCOL-=1
##            if nCOL ==0:
##                    nCOL=1
##        if sCMD =='6':
##            nCOL+=1
##            if nCOL > 11:
##                    nCOL=1
##
##        if sCMD =='5':
##            sKey_virtual=keyboard.get_focused_key_rowcol(nROW,nCOL)
##            if len(sKey_virtual)==1:
##                sCMD_STRING+=keyboard.get_focused_key_rowcol(nROW,nCOL)
##            if sKey_virtual=='ENTER':
##                sCMD='x'
##                print(f'COMMAND = {sCMD_STRING}')
##
##
##        print(f'ROW={nROW} COLUMN={nCOL}')
##        print(f'TypedText={sCMD_STRING}')



