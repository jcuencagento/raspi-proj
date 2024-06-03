import pygame # type: ignore
import sys

# Testing Raspi
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Raspberry Pi Test')

# Set up the font
font = pygame.font.Font(None, 74)
text = font.render('Hello, Raspberry Pi!', True, (255, 255, 255))

# Set up the background color
background_color = (0, 0, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(background_color)

    # Blit the text onto the screen
    screen.blit(text, (150, 250))

    pygame.display.flip()

pygame.quit()
sys.exit()
