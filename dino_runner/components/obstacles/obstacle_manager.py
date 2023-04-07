from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from random import randint
from pygame import K_SPACE


class ObstacleManager:
    obstacles: list[Bird | Cactus]
    COUNTS = 3

    def __init__(self) -> None:
        self.obstacles = list()
        self.counts = self.COUNTS
        self.hammer_state = False
        self.obstacles.append(Cactus())

    def update(self, game_speed, player, user_input):
        if len(self.obstacles) == 0:
            value = randint(0, 1)
            if value == 0:
                self.obstacles.append(Cactus())
            else:
                self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                player.counts['obstacles_jump'] += 1
                self.obstacles.pop()

            if user_input[K_SPACE] and player.hammer and not self.hammer_state:
                if self.counts > 0:
                    value_a1 = player.dino_rect.y
                    value_a2 = player.dino_rect.y + player.dino_rect.height
                    value_b1 = obstacle.rect.y
                    value_b2 = obstacle.rect.y + obstacle.rect.height
                    self.counts -= 1
                    self.hammer_state = True
                    if value_b1 in range(value_a1, value_a2) or value_b2 in range(value_a1, value_a2):
                        self.obstacles.pop()
                        player.counts['obstacles_destroy'] += 1

            if self.counts <= 0 and player.hammer:
                player.reset()

            if not user_input[K_SPACE] and self.hammer_state:
                self.hammer_state = False

            if not player.hammer:
                self.counts = self.COUNTS

            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
