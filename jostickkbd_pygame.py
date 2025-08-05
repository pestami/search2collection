import pygame

pygame.init()

# Check for connected joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} moved to {event.value}")

            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")

            if event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")

        pygame.display.flip() 

else:
    print("No joysticks connected.")