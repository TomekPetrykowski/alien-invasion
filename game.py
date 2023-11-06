import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry"""

    def __init__(self):
        pygame.init()

        self.set = Settings()

        self.screen = pygame.display.set_mode(
            (self.set.screen_width, self.set.screen_height))
        pygame.display.set_caption("Inwazja obcych")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.set.bg_color)
            self.ship.blitme()

            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
