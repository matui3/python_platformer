import sys
import pygame

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
class Game:
    def __init__(self):

        # intializes the game
        pygame.init()

        # creating labels for things
        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240)) # convention bcuz screen is window, display is what you render onto, black image, render onto smaller resolution then scale it up to get pixel art

        self.clock = pygame.time.Clock()
        
        # moevment stuff????
        self.movement = [False, False]


        # loads assets for map
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }

        # collisions???
        self.collision_area = pygame.Rect(50, 50, 300, 50)

        # the physics entity uses the game class with self, the player asset, the position is 50, 50 and the size is 8x15
        # the game is not called at all with physics entity
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.tilemap = Tilemap(self, tile_size=16)

    def run(self):

        while True:
            # rendering window
            self.display.fill((14, 219, 248))
            
            # rendering tilemap
            self.tilemap.render(self.display) # renders self.dplay

            # update the player and rendering the player, # no changes in y-axis is but takes movement 1 - movement 0
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            # basic pygame loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            # screen correction    
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0)) # render display onto screen.
            pygame.display.update()
            self.clock.tick(60)

# run the game
Game().run()