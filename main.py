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
# Colours
LIGHT_ORANGE = (255, 230, 190)
GREEN = (0, 120, 0)
BLACK = (0, 0, 0)
RED = (180, 0, 0)

def main():
    """
    Start the Pygame application and create the main game window.

    The function opens a window and keeps it running until
    the user closes it.
    """
    pygame.init()

    title_font = pygame.font.SysFont("arial", 50, bold=True)
    normal_font = pygame.font.SysFont("arial", 30)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Discover Kerala")

    clock = pygame.time.Clock()
    running = True
    current_screen = "START"

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if current_screen == "START":

                    if event.key == pygame.K_k:
                        print("K pressed")

                    elif event.key == pygame.K_ESCAPE:
                        running = False            
            if event.type == pygame.QUIT:
                running = False

        screen.fill(LIGHT_ORANGE)

        if current_screen == "START":

            title_text = title_font.render(
                "DISCOVER KERALA",
                True,
                GREEN
            )

            subtitle_text = normal_font.render(
                "Harmony Day Cultural Quiz Game",
                True,
                BLACK
            )

            start_text = normal_font.render(
                "Press K to Discover Kerala",
                True,
                BLACK
            )

            exit_text = normal_font.render(
                "Press ESC to Exit",
                True,
                RED
            )

            screen.blit(title_text, (220, 150))
            screen.blit(subtitle_text, (220, 250))
            screen.blit(start_text, (260, 350))
            screen.blit(exit_text, (320, 420))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()