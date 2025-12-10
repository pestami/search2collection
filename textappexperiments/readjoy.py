#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 14:39:02 2025

@author: pi
"""

import evdev  #apt install python3-evdev

def main():
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    for device in devices:
        print(f"Found DEVICE: {device.name}")
        if 'stick' in device.name.lower():  # Look for joystick devices
            print(f"Found joystick: {device.name}")
            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_ABS:
                    print(f"Axis {event.code}: {event.value}")
                elif event.type == evdev.ecodes.EV_KEY:
                    print(f"Button {event.code}: {'pressed' if event.value == 1 else 'released'}")

if __name__ == "__main__":
    main()
