from pynput import keyboard
import threading

from pyjoystick.sdl2 import Key, Joystick, run_event_loop

def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def key_received(key):
    print('Key:', key)
    if key=='Hat 0 [Up]':
        print("Let us exit")


stop_loop = False

def on_press(key):
    global stop_loop
    try:
        if key.char.lower() == 'q':  # Press 'q' to exit the loop
            stop_loop = True
            return False  # Stop listener
    except AttributeError:
        pass

def main():
    global stop_loop
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while not stop_loop:
        # Your loop code here
        print("Loop is running...")
        # Simulating some work
        import time
        time.sleep(1)

    listener.stop()
    print("Loop exited.")

if __name__ == "__main__":
    main()
