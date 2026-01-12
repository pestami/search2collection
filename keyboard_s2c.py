
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

from read_joystick_pygame import pygame_joystick



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
            ['-', '&', '+', '.', '/', ';', '\'', '{', '}','%','SPACE']

        ]

        self.strKEYBOARD =''
        self.focused_key = None
        self.strCOMMANDLINE =''

#-------------------------------------------------------------------------------
    def draw_keyboard_textvar(self, focused_key):
        # Print the keyboard layout
        
                
        strKEYBOARD=''
        for i, row in enumerate(self.keyboard_layout):
            row_str = '[red]'
            for j, key in enumerate(row):

                if (i+1, j+1) == focused_key:
                    # Highlight the focused key with red foreground and yellow background
                    highlighted_key = f'\033[91;103m{key.center(3)}\033[0m'
                    highlighted_key = f'[bold][white]{key.center(3)}[/white][/bold]'

                    row_str += highlighted_key
                elif key == '                                        ':
                    row_str += ' ' * 40
                else:
                    row_str += key.center(3)

            strKEYBOARD+=row_str + '[/red]\n'

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
         

        keyboard = Keyboard()
        sCMD=''
        sCMD_PRE=''
        nROW=1
        nCOL=1
        sPannelText2=''
        sKey_virtual=''
        
     
        #-----Initialize Print keyboard----------------------------------------
        sPannelText = ' [blue]  X-left A-Right Y-up B-down [/blue]\n' + keyboard.draw_keyboard_textvar((nROW,nCOL)) +    '      [blue]fire=SELECT[/blue]'
        sResultsTitle='KEYBOARD'
        sResultsTitle2='TYPED'
        keyboard_panel = Panel(sPannelText, title=sResultsTitle,height=9,width=40)
        keyboard_panel2 = Panel(sPannelText2, title=sResultsTitle2,height=5,width=40)

        console.print(Columns([keyboard_panel]))
        #console.print(Columns([keyboard_panel2]))
    
        #---------------------------------------------------------------------
        

       # while(sCMD!='5'):
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        while(sKey_virtual !='ENTER'):
            
            
            sPannelText1 = keyboard.draw_keyboard_textvar((nROW,nCOL)) # returns text table of keyboard
            sResultsTitle1='KEYBOARD'
            sResultsTitle2='TYPED'
            keyboard_panel1 = Panel(sPannelText1, title=sResultsTitle1,height=7,width=40)
            keyboard_panel2 = Panel(sPannelText2, title=sResultsTitle2,height=5,width=40)

            if sCMD in ['2','8','4','6','5','e','s','d','x',' ','w','r']:
                os.system('clear')
                # console.print(Columns([keyboard_panel1]))
                # console.print(Columns([keyboard_panel2]))     
                console.print(Columns([keyboard_panel1, keyboard_panel2]))
                #sCMD=''
                
            #-----COMMANDLINE------------------------------------------------------
            #key =self.read_keypress()
            #sCMD =key
            key=''
            
            joy_kbd=pygame_joystick(my_debug=False)  
            sCMD_PRE=sCMD
            sCMD=joy_kbd.poll_joystick()      
            #print(sCMD)
            #-------------------------------------------------------------------                
            if sCMD in ['2','x']:
                nROW+=1
            if nROW > 5:
                    nROW=1
            if sCMD in ['8','e']:
                nROW-=1
                if nROW == 0:
                        nROW=5
            if sCMD in ['4','s']:
                nCOL-=1
                if nCOL ==0:
                        nCOL=11
            if sCMD in ['6','d']:
                nCOL+=1
                if nCOL > 11:
                        nCOL=1
                        
            if sCMD in ['5','w']:  #select
            
                sKey_virtual=self.get_focused_key_rowcol(nROW,nCOL)                           
                
                if len(sKey_virtual)==1:
                    self.strCOMMANDLINE+=self.get_focused_key_rowcol(nROW,nCOL)
                    
                if sKey_virtual=='ENTER':
                    sCMD='5'
                if sKey_virtual=='SPACE':
                    sCMD=' '
                    self.strCOMMANDLINE+=' '
                if sKey_virtual=='CLR':
                    self.strCOMMANDLINE=''
                if sKey_virtual=='DEL':
                    self.strCOMMANDLINE=self.strCOMMANDLINE[0:-1]
                    
            if sCMD in ['9','r']:
                sKey_virtual='ENTER'
                
                    
       
            sPannelText2=' ROW=' + str(nROW) + ' COLUMN=' + str(nCOL) +'\n sKey='+ sCMD +  '\n Command:'+ self.strCOMMANDLINE   #DEBUG
            
            sPannelText2=' sCMD_PRE='+ sCMD_PRE + ' sCMD='+ sCMD +  '\n Command:'+ self.strCOMMANDLINE
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
             
            
            # print(f'sCMD={sCMD} ')
            # print(f'ROW={nROW} COLUMN={nCOL}')
            # print(f'TypedText={self.strCOMMANDLINE}')
            


        return self.strCOMMANDLINE
#===============================================================================
if __name__ == "__main__":


    os.system('clear')
    keyboard = Keyboard()
    sCOMMANDLINE= keyboard.draw_keyboard_loop()
    print(f'COMMANDLINE={sCOMMANDLINE} ')

