from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
import os

console = Console()


class myrich:
    
    def __init__(self, sTextLeft, sTextRight,sTitleLeft,sTitleRight,nScreenWidth):
    
        self.sTextLeft =sTextLeft
        self.sTextRight =sTextRight
        self.sTitleLeft =sTitleLeft
        self.sTitleRight =sTitleRight
        self.nScreenWidth =120
    
    
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    
    def print_right(self,stext):
        
        self.sTextRight=self.sTextRight + stext
        
    def print_left(self,stext):
            
            self.sTextLeft=self.sTextLeft + stext
            
    def refresh_console(self):
                     
            left_text_panel = Panel(self.sTextLeft, title=self.sTitleLeft)
            right_text_panel = Panel(self.sTextRight, title=self.sTitleRight)
            console.print(Columns([left_text_panel, right_text_panel]))
        
 #===============================================================================       
def add_linebreaks(text, max_length=60):
    return '\n'.join([text[i:i+max_length] for i in range(0, len(text), max_length)])

def main():
    
    myconsole=myrich('[bold magenta]Left Window[/bold magenta]\n','[bold cyan]Right Window[/bold cyan]\n','COMMANDS','RESULTS',120)
    
    myconsole.refresh_console()

    #myconsole.clear_console()
    
       

    while True:
        
        # left_text_panel = Panel(left_text, title="Left")
        # right_text_panel = Panel(right_text, title="Right")
        # console.print(Columns([left_text_panel, right_text_panel]))
        
        myconsole.refresh_console()
        
        choice = input("Enter your choice (1/2/3): ")


        if choice == "1":
            myconsole.print_left("\n.......You selected Option 1")
           
        elif choice == "2":
            myconsole.print_left("\n...........You selected Option 2")
        elif choice == "3":
            print("Exiting the application")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()