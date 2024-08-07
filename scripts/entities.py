import pygame

# creating an entity
class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
    # has the entity type, calls in the game, calls in the position and a size
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    # how muchh entity should movvvev in a given frame.
    def update(self, tilemap,  movement=(0, 0)):

        self.collisions = {'up': False, 'down': False,
                           'right': False, 'left': False}
        
        
        # defines how it should moev
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        # shows how much it moves in that frame. so the movement is defined as velocity w/ increased acceleration
        # this adds to the position the frame movement
        self.pos[0] += frame_movement[0]

        # creating an entity as a rectangle
        # all the 
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        

        # two dimensional movement same thing
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y

        # gravity
        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

    # rendering take the surface and use the player where you take the image and the position
    def render(self, surf, offset=(0, 0)):
        surf.blit(self.game.assets['player'], (self.pos[0] - offset[0], self.pos[1] - offset[1]))