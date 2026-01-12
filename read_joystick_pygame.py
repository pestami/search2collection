import pygame
import sys
import configparser

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
        
        


    def load_ini_file(self,file_path):
        config = configparser.ConfigParser()
        config.read(file_path)
    
        if 'Buttons' in config:
            buttons_config = config['Buttons']
            ButtonUP = buttons_config.get('ButtonUP', '')
            ButtonDOWN =  buttons_config.get('ButtonDOWN', '')
            ButtonLEFT =  buttons_config.get('ButtonLEFT', '')
            ButtonRIGHT =  buttons_config.get('ButtonRIGHT', '')
            ButtonSTART =  buttons_config.get('ButtonSTART', '')
            ButtonSELECT =  buttons_config.get('ButtonSELECT', '')
    
            return ButtonUP, ButtonDOWN, ButtonLEFT, ButtonRIGHT, ButtonSTART , ButtonSELECT
        else:
            print("The file does not contain a 'Buttons' section.")
            return None


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
        
        
        ButtonUP, ButtonDOWN, ButtonLEFT, ButtonRIGHT, ButtonSTART,ButtonSELECT = self.load_ini_file('joystick_buttons.ini')
        
        if self.my_debug: 
            print(f"ButtonUP: {ButtonUP}")
            print(f"ButtonDOWN: {ButtonDOWN}")
            print(f"ButtonLEFT: {ButtonLEFT}")
            print(f"ButtonRIGHT: {ButtonRIGHT}")
            print(f"ButtonSTART: {ButtonSTART}")
        # ------------------Main loop--------------------------------------
        
        while True:
            #---------Get events-----------------------------------------------
            for event in pygame.event.get():               

                if event.type == pygame.JOYBUTTONUP:
                    if self.my_debug: 
                           print(f"Button {event.button} released")
                           
                    if event.button ==int(ButtonLEFT):
                        if self.my_debug: 
                           print("moved LEFT")
                        CMD="LEFT"
                        CMD="s"
                        
                    if event.button ==int(ButtonRIGHT):
                        if self.my_debug: 
                           print("moved RIGHT")
                        CMD="RIGHT"
                        CMD="d"
                            
                    if event.button ==int(ButtonUP):
                        if self.my_debug: 
                               print("moved UP")
                        CMD="UP"
                        CMD="e"
                    if event.button ==int(ButtonDOWN):
                        if self.my_debug: 
                                print("moved DOWN")
                        CMD="DOWN"
                        CMD="x"
                    if event.button ==int(ButtonSTART):
                         if self.my_debug: 
                                print("Released Button")
                         CMD="START" 
                         CMD="r"
                         
                    if event.button ==int(ButtonSELECT):
                        if self.my_debug: 
                               print("Released Button")
                        CMD="SELECT"  
                        CMD="w"     
              
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
              #----END-----Get events----------------------------------------      
        
        return CMD   
    
#===============================================================================
if __name__ == "__main__":
    
    
    joy_kbd=pygame_joystick(my_debug=True)
    
    # Example usage
    file_path = 'joystick_buttons.ini'
    values = joy_kbd.load_ini_file(file_path)
    
    if values:
        ButtonUP, ButtonDOWN, ButtonLEFT, ButtonRIGHT, ButtonSTART = values
        print(f"ButtonUP: {ButtonUP}")
        print(f"ButtonDOWN: {ButtonDOWN}")
        print(f"ButtonLEFT: {ButtonLEFT}")
        print(f"ButtonRIGHT: {ButtonRIGHT}")
        print(f"ButtonSTART: {ButtonSTART}")     
    
    

    
    CMD=joy_kbd.poll_joystick()
    
    print('===================================')
    print(CMD)
    if CMD==" ":
        print("SAPACE")
    print('===================================')
