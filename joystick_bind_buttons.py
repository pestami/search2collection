from read_joystick_pygame import pygame_joystick
import configparser
import pygame

def map_buttons_to_ini_file(file_path,lButtonValues):
    config = configparser.ConfigParser()

    # Create a section if it doesn't exist
    if not config.has_section('Buttons'):
        config.add_section('Buttons')

    # Set values
    config.set('Buttons', 'ButtonUP', lButtonValues[0])
    config.set('Buttons', 'ButtonDOWN', lButtonValues[1])
    config.set('Buttons', 'ButtonLEFT', lButtonValues[2])
    config.set('Buttons', 'ButtonRIGHT', lButtonValues[3])
    config.set('Buttons', 'ButtonSTART', lButtonValues[4])

    # Write to file
    with open(file_path, 'w') as configfile:
        config.write(configfile)
        
def Read_Button():
     key=''
     
     while True:
         #---------Get events-----------------------------------------------
         for event in pygame.event.get():               

             if event.type == pygame.JOYBUTTONUP:
                
                         key=str(event.button)
                         print(f"Button pressed  {event.button} and released")
                         break
             
             break   
         
         if key: 
             break
         
             # Delay to prevent high CPU usage
         pygame.time.delay(50)
           
           #----END-----Get events---------------------------------------- 
     return key
        
#============================================================================        
if __name__ == "__main__":
    my_debug=True
    #-------------------------------
    # Initialize pygame
    pygame.init()

    # Initialize joystick module
    pygame.joystick.init()    
    
    # Get the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    

    
    #-------------------------------
    
    lButtonValues=['','','','','']
    joy_kbd=pygame_joystick(my_debug=False)    

    print("====================================")  
    print("Press UP Button: ")        
    sCMD=Read_Button() 
    lButtonValues[0]=str(sCMD)
    print(f"UP Button:{lButtonValues[0]}")
    
    print("====================================")  
    print("Press  Down Button: ")        
    sCMD=Read_Button()    
    lButtonValues[1]=str(sCMD)
    print(f"Down Button:{lButtonValues[1]}")
    
    print("====================================")  
    print("Press  Left Button: ")        
    sCMD=Read_Button()     
    lButtonValues[2]=str(sCMD)
    print(f"Left Button:{lButtonValues[2]}")
    
    print("====================================")  
    print("Press  Right Button: ")        
    sCMD=Read_Button()   
    lButtonValues[3]=str(sCMD)
    print(f"Right Button:{lButtonValues[3]}")
    
    print("====================================")  
    print("Press  Start Button: ")        
    sCMD=Read_Button()    
    lButtonValues[4]=str(sCMD)
    print(f"Start Button:{lButtonValues[4]}")
    
    
    
    
    
    # Example usage
    file_path = 'joystick_buttons.ini'
    map_buttons_to_ini_file(file_path,lButtonValues)
