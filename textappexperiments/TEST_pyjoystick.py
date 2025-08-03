from pyjoystick.sdl2 import Key, Joystick, run_event_loop

def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def key_received(key):
    print('Key:', key)
    if key=='Hat 0 [Up]':
        print("Let us exit")
        stop_loop = True
        



def main():
    global stop_loop
    run_event_loop(print_add, print_remove, key_received)  
       

    while not stop_loop:
        # Your loop code here
        print("Loop is running...")
        # Simulating some work
        import time
        time.sleep(1)

    run_event_loop.stop()
    print("Loop exited.")

if __name__ == "__main__":
    main()

