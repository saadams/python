import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    #class to manage game assets and behavior

    def __init__(self):
        #Initialize the game
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        #start game loop 
        while True:
            self.check_events()
            self.update_screen()

            def check_events(self):
                #watch for keyboard and mouse events.
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                        
            def _update_screen(self):
                #redraw the screen for every itaration through the loop
                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()
                #make the most recently drawn screen visible
                pygame.display.flip()

if __name__ == '__main__':
    # make a game instance then run
    ai = AlienInvasion()
    ai.run_game()