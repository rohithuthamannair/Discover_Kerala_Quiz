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
    Create and run the Discover Kerala game.

    This function initializes Pygame, handles user input,
    controls screen navigation and updates the display.
    """
    pygame.init()

    title_font = pygame.font.SysFont("arial", 50, bold=True)
    normal_font = pygame.font.SysFont("arial", 30)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Discover Kerala")

    clock = pygame.time.Clock()
    running = True
    current_screen = "START"
    student_name = ""
    selected_topic = ""

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if current_screen == "START":

                    if event.key == pygame.K_k:
                        current_screen = "NAME"

                    elif event.key == pygame.K_ESCAPE:
                        running = False

                elif current_screen == "NAME":

                    if event.key == pygame.K_RETURN:

                        if student_name.strip() != "":
                            current_screen = "MENU"

                    elif event.key == pygame.K_BACKSPACE:
                        student_name = student_name[:-1]

                    else:
                        if len(student_name) < 18 and event.unicode.isprintable():
                            student_name += event.unicode

                elif current_screen == "MENU":

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    elif event.key == pygame.K_f:
                        selected_topic = "FOOD"
                        current_screen = "TOPIC"

                    elif event.key == pygame.K_e:
                        selected_topic = "FESTIVALS"
                        current_screen = "TOPIC"

                    elif event.key == pygame.K_a:
                        selected_topic = "ARTS & PERFORMANCE"
                        current_screen = "TOPIC"

                    elif event.key == pygame.K_c:
                        selected_topic = "CLOTHING"
                        current_screen = "TOPIC"

                    elif event.key == pygame.K_m:
                        selected_topic = "MARTIAL ARTS"
                        current_screen = "TOPIC"

                    elif event.key == pygame.K_w:
                        selected_topic = "WELLNESS"
                        current_screen = "TOPIC"

                    elif event.key == pygame.K_k:
                        selected_topic = "KERALA FUN FACTS"
                        current_screen = "TOPIC"

                elif current_screen == "TOPIC":

                    if event.key == pygame.K_BACKSPACE:
                        current_screen = "MENU"
                
                elif current_screen == "TOPIC":

                    screen.fill((255, 255, 255))

                    title_text = title_font.render(
                        selected_topic,
                        True,
                        GREEN
                    )

                    screen.blit(title_text, (250, 80))

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

        elif current_screen == "NAME":

            screen.fill((255, 255, 255))

            title_text = title_font.render(
                "ENTER STUDENT NAME",
                True,
                GREEN
            )

            label_text = normal_font.render(
                "Name:",
                True,
                BLACK
            )

            name_text = normal_font.render(
                student_name,
                True,
                BLACK
            )

            enter_text = normal_font.render(
                "Press ENTER to continue",
                True,
                RED
            )

            screen.blit(title_text, (180, 150))
            screen.blit(label_text, (220, 280))
            screen.blit(name_text, (330, 280))
            screen.blit(enter_text, (220, 400))

            pygame.display.flip()

        elif current_screen == "MENU":

            screen.fill(LIGHT_ORANGE)

            welcome_text = normal_font.render(f"Welcome, {student_name}",True,GREEN)

            title_text = normal_font.render("PRESS THE FOLLOWING KEYS TO EXPLORE KERALA",True,BLACK)

            screen.blit(welcome_text, (280, 50))
            screen.blit(title_text, (90, 120))

            menu_lines = [
                "F - Food",
                "E - Festivals",
                "A - Arts & Performance",
                "C - Clothing",
                "M - Martial Arts",
                "W - Wellness",
                "K - Kerala Fun Facts",
                "",
                "Q - Start Quiz",
                "ESC - Exit"
            ]

            y = 200

            for line in menu_lines:

                text = normal_font.render(
                    line,
                    True,
                    BLACK
                )

                screen.blit(text, (280, y))

                y += 40
            pygame.display.flip()

        elif current_screen == "TOPIC":

            screen.fill((255, 255, 255))

            title_text = title_font.render(
                selected_topic,
                True,
                GREEN
            )

            back_text = normal_font.render(
                "Press BACKSPACE to return to Main Menu",
                True,
                RED
            )

            screen.blit(title_text, (220, 150))
            screen.blit(back_text, (180, 500))

            pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()