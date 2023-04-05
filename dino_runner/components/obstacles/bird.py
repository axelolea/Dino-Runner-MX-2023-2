from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from random import choice
from pygame.time import delay


class Bird(Obstacle):

    Y_POS_BIRD = (325, 260, 200)

    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.min_pos_y = choice(self.Y_POS_BIRD)
        self.rect.y = 0
        self.step_index = 0

    def update(self, game_speed, player):
        # Update x, y value
        self.rect.x -= game_speed
        self.rect.y = self.min_pos_y + (self.rect.x * 0.1) - (self.rect.x**2 * 0.0003)
        # Collision
        if self.rect.colliderect(player.dino_rect):
            player.dino_live = False
            delay(1000)
        # Change image
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]

        if self.step_index >= 10:
            self.step_index = 0
        else:
            self.step_index += 1
