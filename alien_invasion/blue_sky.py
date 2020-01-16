import sys

import pygame

class Character():

    def __init__(self, screen):
        """Initialize the character and set its starting position."""
        self.screen = screen

        # Load the character image and get its rect.
        self.image = pygame.image.load('images/kirby.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start character at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    # Set the background color.
    bg_color = (0, 200, 255)

    # Make a characer.
    kirby = Character(screen)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        kirby.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()