import pygame
from physics.gravity import GravitySimulator

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation")

# Create a gravity simulator instance
gravity_simulator = GravitySimulator()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the physics
    gravity_simulator.update_positions()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the bodies (this will be implemented in the GravitySimulator)
    gravity_simulator.draw_bodies(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()