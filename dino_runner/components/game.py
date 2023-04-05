import pygame

from dino_runner.utils.constants import (
    BG,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    CLOUD,
    FPS
)
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_up.power_up_manager import PowerUpManager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.player = Dinosaur()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.points = 0
        self.game_speed = 20
        self.percentage_cloud_speed = 0.3
        self.y_pos_bg = 380
        self.x_pos_bg = 0
        self.clouds = [
            {'pos_x': 120, 'pos_y': 50},
            {'pos_x': 800, 'pos_y': 110}
        ]
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(2000)
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.points += 1
        user_input = pygame.key.get_pressed()
        self.obstacle_manager.update(self.game_speed, self.player)
        self.power_up_manager.update(self.game_speed, self.points, self.player)
        self.player.update(user_input)
        if not self.player.dino_live:
            self.playing = False

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_clouds()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_clouds(self) -> None:
        cloud_speed = self.game_speed * self.percentage_cloud_speed
        image_width = CLOUD.get_width()
        for cloud in self.clouds:
            self.screen.blit(CLOUD, (cloud['pos_x'], cloud['pos_y']))
            cloud['pos_x'] -= cloud_speed
            actual_pos = cloud['pos_x'] + image_width
            if actual_pos < 0:
                cloud['pos_x'] += SCREEN_WIDTH + image_width
