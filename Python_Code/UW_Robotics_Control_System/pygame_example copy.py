import pygame


pygame.init()


# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()


# -------- Main Program Loop -----------
while True:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        pass

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()


    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()

        for i in range(axes):
            axis = joystick.get_axis(i)
            print(axis)

        buttons = joystick.get_numbuttons()

        for i in range(buttons):
            button = joystick.get_button(i)
    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()