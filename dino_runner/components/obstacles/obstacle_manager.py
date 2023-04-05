from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from random import randint


class ObstacleManager:
    obstacles: list[Bird | Cactus]

    def __init__(self) -> None:
        self.obstacles = list()
        self.obstacles.append(Cactus())

    def update(self, game_speed, player):
        if len(self.obstacles) == 0:
            value = randint(0, 1)
            if value == 0:
                self.obstacles.append(Cactus())
            else:
                self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
