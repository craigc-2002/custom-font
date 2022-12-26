"""
Program to test the customFont library

Creates a pygame display and uses the library to render text to it
"""

import customFont
import pygame
import random

# ---Setup---
pygame.init()  # Initialise pygame

# Set the dimensions of the window
window_width = 1280
window_height = 720

# Set up the window to the required dimensions, name it and create a clock object
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("CustomFont Test")
clock = pygame.time.Clock()

font = customFont.CustomFont("assets/my-font.png", "assets/font-file.txt")
pos = [random.randint(0, window_width), random.randint(0, window_height)]
#pos = 100, 300
v = [random.randint(1, 5), random.randint(1, 5)]

# ---Main Game Loop---
while True:
    # Check event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Update sprites here
    pos[0] += v[0]
    if pos[0] < 0 or pos[0] > window_width:
        v[0] *= -1
        v[0] += random.randint(-1, 1)
    pos[1] += v[1]
    if pos[1] < 0 or pos[1] > window_height:
        v[1] *= -1
        v[1] += random.randint(-1, 1)

    screen.fill("white")
    # Display screen updates here
    font.write("Hello World,\nit's Craig.", screen, 10, pos, "centre")
    font.write("1234567890", screen, 10, (100, 400))

    pygame.display.flip()  # Display the screen updates
    clock.tick(60)
