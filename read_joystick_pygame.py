import pygame
import sys

#
#===============================================================================
class pygame_joystick:
    
    #global my_debug
    
    #def __init__(self,**arg):
        
    def __init__(self,**arg):
        
        self.my_debug=True
        self.my_debug=False
        
        # Initialize pygame
        pygame.init()
    
        # Initialize joystick module
        pygame.joystick.init()
        
        
        if self.my_debug: print("===INITIALIZE=====")
      
        

    def poll_joystick(self,**arg):
        
        if self.my_debug: 
           print("===POLLING JOYSTICK=====")

        # Get the number of joysticks
        num_joysticks = pygame.joystick.get_count()
        if num_joysticks == 0:
            if self.my_debug: 
               print("No joystick found")
            return "NOP"
        
        # Get the first joystick
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    
        # Get the name of the joystick
        if self.my_debug: 
           print(f"Joystick name: {joystick.get_name()}")
        CMD=''
        # Main loop
        
        while True:
            # Get events
            for event in pygame.event.get():                


                                                 
                if event.type == pygame.JOYBUTTONUP:
                    if self.my_debug: 
                           print(f"Button {event.button} released")
                           
                    if event.button ==2:
                        if self.my_debug: 
                           print("moved LEFT")
                        CMD="LEFT"
                        CMD="s"
                        
                    if event.button ==1:
                        if self.my_debug: 
                           print("moved RIGHT")
                        CMD="RIGHT"
                        CMD="d"
                            
                    if event.button ==3:
                        if self.my_debug: 
                               print("moved UP")
                        CMD="UP"
                        CMD="e"
                    if event.button ==0:
                        if self.my_debug: 
                                print("moved DOWN")
                        CMD="DOWN"
                        CMD="x"
                    if event.button ==5:
                         if self.my_debug: 
                                print("Released Button")
                         CMD="BUTTON"
                         CMD="5"
                    
                    if self.my_debug: 
                                print("CMD=" + CMD)                              
                        
                # Delay to prevent high CPU usage
                    pygame.time.delay(50)
                    
                    if CMD !='':    # Exit on button 0 press
                            if self.my_debug: 
                               print("Exiting program")
                            # pygame.quit()
                            # sys.exit()
                            return CMD
                    
        return CMD   
    
#===============================================================================
if __name__ == "__main__":
    
    
    joy_kbd=pygame_joystick(my_debug=True)
    
    CMD=joy_kbd.poll_joystick()
    
    print('===================================')
    print(CMD)
    if CMD==" ":
        print("SAPACE")
    print('===================================')
