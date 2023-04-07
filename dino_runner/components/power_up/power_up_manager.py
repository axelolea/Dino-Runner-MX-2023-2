from dino_runner.components.power_up.shield import Shield
from dino_runner.components.power_up.hammer import Hammer
from random import randint


class PowerUpManager:
    POINTS = 250
    power_ups: list[Shield | Hammer]

    def __init__(self):
        self.power_ups = list()

    def update(self, game_speed, points, player):
        if len(self.power_ups) == 0 and points % self.POINTS == 0:
            value = randint(0, 1)
            value = 0
            if value == 0:
                self.power_ups.append(Hammer())
            else:
                self.power_ups.append(Shield())

        for power_up in self.power_ups:
            if power_up.rect.x < -power_up.rect.width or power_up.used:
                self.power_ups.pop()
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
