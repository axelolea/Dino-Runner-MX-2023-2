from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from random import choice


class Cactus(Obstacle):
    Y_POS_CACTUS = 397

    def __init__(self):
        self.image = choice(SMALL_CACTUS + LARGE_CACTUS)
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUS - self.image.get_height()
