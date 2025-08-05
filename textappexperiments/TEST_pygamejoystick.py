import pygame

def external_function():
    print("External function called")

def main():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("No joystick found")
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"Joystick name: {joystick.get_name()}")

    button_mapping = {
        0: external_function  # Button 0 calls external_function
    }

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} moved to {event.value}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
                if event.button in button_mapping:
                    button_mapping[event.button]()
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")
            elif event.type == pygame.JOYHATMOTION:
                print(f"Hat {event.hat} moved to {event.value}")

if __name__ == "__main__":
    