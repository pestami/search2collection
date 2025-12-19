#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 14:39:02 2025

@author: pi
"""

import evdev  #apt install python3-evdev

def getjoy_cmd():
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    for device in devices:
        print(f"Found DEVICE: {device.name}")
        if 'stick' in device.name.lower():  # Look for joystick devices
            print(f"Found joystick: {device.name}")
            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_ABS:
                    print(f"Axis {event.code}: {event.value}")
                    sCMD=event.value
                elif event.type == evdev.ecodes.EV_KEY:
                    print(f"Button {event.code}: {'pressed' if event.value == 1 else 'released'}")
                    sCMD=event.code
                    print(f"CMD={event.code}")
                if sCMD==288:
                    print('EXIT')
                    break
    return sCMD             




def main():
    
    sCMD=''
    #sCMD=getjoy_cmd()
    
    print("Command=", sCMD)
    
    sKEYBOARD1=['ABCDEFGHI']
    sKEYBOARD2=['JKLMNOPQR']
    sKEYBOARD3=['STUVWXYZ']
    n=5
    print( sKEYBOARD1[0][n:n+1] + '\033[92m')
    
    print("\033[91m This text is red \033[0m")  # Red
    print("\033[92m This text is green \033[0m")  # Green
    print("\033[93m This text is yellow \033[0m")  # Yellow
    print("\033[94m This text is blue \033[0m")  # Blue
    print("\033[95m This text is magenta \033[0m")  # Magenta
    print("\033[96m This text is cyan \033[0m")  # Cyan


if __name__ == "__main__":
    main()
