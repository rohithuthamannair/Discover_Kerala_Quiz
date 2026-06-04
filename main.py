"""
Discover Kerala: Harmony Day Cultural Quiz Game

This program will introduce primary school students to selected
aspects of Kerala culture through educational screens and a quiz.

Students will explore cultural topics, answer quiz questions,
earn a badge, and save their result to a file.

Author: Rohith
Date: June 2026
"""

import pygame


# --------------------
# CONSTANTS
# --------------------

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650
FPS = 60


def main():
    """
    Start the Pygame application and create the main game window.

    The function opens a window and keeps it running until
    the user closes it.
    """
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Discover Kerala")

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 230, 190))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()