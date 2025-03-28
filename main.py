import pygame

from engine.colors import WHITE, RED, GREEN, BLUE
from engine.timer.timer import Timer
from engine.ui.shapes.Circle import Circle
from engine.ui.shapes.CircleSurface import CircleSurface
from engine.ui.shapes.RectangleSurface import RectangleSurface
from engine.ui.shapes.Triangle import Triangle
from engine.ui.shapes.TriangleSurface import TriangleSurface
from engine.ui.text.text_builder import TextBuilder
from engine.window import Window


def main():
    screen = pygame.display.set_mode((1200, 800))

    window = Window(screen=screen, caption="test", background_color=WHITE)
    window.init()
    pygame.font.init()

    text = TextBuilder(pygame.Rect(25, 25, 250, 100)).set_text("messi").create_text()

    text.set_on_click_listener(lambda:
                               Timer(lambda: print("yo sir"), 1)
                               .start())

    rect_surface = RectangleSurface(pygame.Rect(225, 25, 250, 100), RED)
    triangle_surface = TriangleSurface(Triangle(255, 30, 450, 300, 222, 300), GREEN)
    circle_surface = CircleSurface(Circle(255, 445, 35), BLUE)

    running = True
    while running:
        window.screen.fill(window.background_color)

        text.draw(screen)
        rect_surface.draw(screen)
        triangle_surface.draw(screen)
        circle_surface.draw(screen)
        # for loop through the event queue
        events = pygame.event.get()
        text.on_event_tick(events)
        for event in events:

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()


if __name__ == "__main__":
    main()