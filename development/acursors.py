from curses import wrapper
from curses.textpad import Textbox, rectangle
import curses
import sys
#class acursors:

#-------------------------------------------------------------------------------
import curses

def main(stdscr):
    # Clear the main window
    stdscr.clear()
    stdscr.box()
    # Print a message in the main window
    stdscr.addstr(0, 2, "Main Window")
    stdscr.addstr(1, 1, "This is the main window.")
    stdscr.addstr(2, 1, "You can type here.")

    # Create a new sub-window with height 10, width 20, at position (5, 5)
    win = curses.newwin(10, 30, 5, 5)

    # Clear the sub-window
    win.clear()

 # Draw a box around the sub-window
    win.box()
    # Print a message in the sub-window
    win.addstr(0, 2, "Sub-Window")
    win.addstr(1, 1, "This is a sub-window.")
    win.addstr(2, 1, "You can also type here.")

   

    # Refresh the main window to make the changes visible
    stdscr.refresh()

    # Refresh the sub-window to make the changes visible
    win.refresh()

    X=5
    Y=5    
    rows, cols = win.getmaxyx()    
    while True:        
        k = stdscr.getkey()
        if k == "q":
            sys.exit(0)
            
        elif k == "KEY_UP":
            Y-=1
        elif k == "KEY_DOWN":
           Y+=1
        elif k == "KEY_LEFT":
            X-=1
        elif k == "KEY_RIGHT":
            X+=1            
            
        sString='X'
                
        if X< 1:
            X=1
        if Y< 1:
            Y=1
        if Y> rows-1-1:
            Y=rows-1-1
            
        if X> cols-1-1 - len(sString):
            X=cols-1-1 - len(sString)
            
        win.addstr(Y, X, " X ")
        win.addstr(Y, X, "")     
        
            
        stdscr.addstr(4, 15, 'R=' + str(rows))
        stdscr.addstr(4, 20,  'C=' + str(cols))
        stdscr.addstr(4, 25, 'Ry=' + str(Y)+'  ')
        stdscr.addstr(4, 30,  'Cx=' + str(X)+ '  ')
        
       
        
        win.addstr(1, 2, "EDIT WIN")
        
        
            # Refresh the main window to make the changes visible
        stdscr.refresh()

    # Refresh the sub-window to make the changes visible
        win.refresh()
        

    


curses.wrapper(main)

