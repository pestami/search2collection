#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 14:39:02 2025

@author: pi
"""

import evdev  #apt install python3-evdev
import os
import time

class joystic4kbd:
#===============================================================================
<<<<<<< HEAD
    def sentence_to_set(self, sentence):
        # Remove punctuation and convert to lower case
        sentence = ''.join(e for e in sentence if e.isalnum() or e.isspace()).lower()
        # Split the sentence into words and convert to a set
        word_set = set(sentence.split())
        return word_set

#===============================================================================
    def PollJoystick(self):
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for device in devices:
            print(f"Found DEVICE: {device.name}")
            
            setDeviceName=self.sentence_to_set(device.name.lower())
            setControlers={'joystick','gamecontroller','gamepad','contoler'}
            
            
            if setDeviceName&setControlers:  # Look for joystick devices
                print(f"Gamepad: {device.name}")
                
                for event in device.read_loop():
                    
                    os.system('cls||clear')
                    print('==READ JOYSTICK using evdf======')
    
    
                    time.sleep(1)
                    
                    if event.type == evdev.ecodes.EV_ABS:
                        print(f"Axis {event.code}: {event.value}")
                        #break
                    elif event.type == evdev.ecodes.EV_KEY:
                        print(f"Button {event.code}: {'pressed' if event.value == 1 else 'released'}")
                        #break

=======
def sentence_to_set(sentence):
    # Remove punctuation and convert to lower case
    sentence = ''.join(e for e in sentence if e.isalnum() or e.isspace()).lower()
    # Split the sentence into words and convert to a set
    word_set = set(sentence.split())
    return word_set

#===============================================================================
def main():
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    for device in devices:
        print(f"Found DEVICE: {device.name}")
        
        setDeviceName=sentence_to_set(device.name.lower())
        setControlers={'joystick','gamecontroller','gamepad','contoler'}
        
        
        if setDeviceName&setControlers:  # Look for joystick devices
            print(f"Gamepad: {device.name}")
            
            for event in device.read_loop():
                
                os.system('cls||clear')
                print('==READ JOYSTICK using evdf======')


                time.sleep(1)
                
                if event.type == evdev.ecodes.EV_ABS:
                    print(f"Axis {event.code}: {event.value}")
                    #break
                elif event.type == evdev.ecodes.EV_KEY:
                    print(f"Button {event.code}: {'pressed' if event.value == 1 else 'released'}")
                    #break

>>>>>>> origin/search2collections
#===============================================================================
if __name__ == "__main__":
    
    
    MP_joystic4kbd=joystic4kbd()
    
    MP_joystic4kbd.PollJoystick()
