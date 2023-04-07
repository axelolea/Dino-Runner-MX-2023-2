import pygame

from dino_runner.utils.constants import (
    CLOUD,
    BG,
    BG_1,
    BG_2,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS
)
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_up.power_up_manager import PowerUpManager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text import get_message
from math import ceil
from dino_runner.utils.save_data import save_data, loading_data


class Game:

    stats: dict

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.player = Dinosaur()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.points = 0
        self.death = 0
        self.new_score = False
        self.game_speed = 20
        self.backgrounds = {
            'cloud_1': {
                'img': CLOUD,
                'pos_x': 120,
                'pos_y': 50,
                'percentage': 0.3,
                'duplicated': False
            },
            'cloud_2': {
                'img': CLOUD,
                'pos_x': 800,
                'pos_y': 110,
                'percentage': 0.3,
                'duplicated': False
            },
            'background_1': {
                'img': BG_1,
                'pos_x': 0,
                'pos_y': 210,
                'percentage': 0.5,
                'duplicated': True
            },
            'background_2': {
                'img': BG_2,
                'pos_x': 0,
                'pos_y': 239,
                'percentage': 0.7,
                'duplicated': True
            },
            'line_track': {
                'img': BG,
                'pos_x': 0,
                'pos_y': 380,
                'percentage': 1,
                'duplicated': True
            }
        }
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        self.stats = loading_data()
        while self.running:
            self.events()
            self.update()
            self.draw()
        save_data(self.stats)
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

    def update(self):
        if not self.playing:
            return
        self.points += 1
        if self.points % 200 == 0:
            self.game_speed += 1
        user_input = pygame.key.get_pressed()
        self.obstacle_manager.update(self.game_speed, self.player, user_input)
        self.power_up_manager.update(self.game_speed, self.points, self.player)
        self.player.update(user_input)
        if not self.player.dino_live:
            self.playing = False
            self.death += 1
            self.set_stats_value()

    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_scene()
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()

        if not self.player.dino_live:
            self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_scene(self):
        for bg in self.backgrounds.values():
            relative_speed = self.game_speed * bg['percentage']
            image_width = bg['img'].get_width()
            if bg['duplicated']:
                repeats = ceil(SCREEN_WIDTH/image_width) + 1
                for number in range(0, repeats):
                    pos_x = (image_width * number) + bg['pos_x']
                    self.screen.blit(bg['img'], (pos_x, bg['pos_y']))
            else:
                self.screen.blit(bg['img'], (bg['pos_x'], bg['pos_y']))

            if bg['pos_x'] <= -image_width:
                bg['pos_x'] = 0 if bg['duplicated'] else SCREEN_WIDTH

            bg['pos_x'] -= relative_speed

    def draw_score(self):
        score, score_rect = get_message(f'Points: {self.points}', 20, 1000, 40)
        best_score, best_score_rect = get_message(f'Best: {self.stats["best_score"]}', 20, 1000, 60)
        self.screen.blit(score, score_rect)
        self.screen.blit(best_score, best_score_rect)

    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        if self.death == 0:
            text, text_rect = get_message('Press any Key to Start', 40)
            self.screen.blit(text, text_rect)
        else:
            score_msg = 'Points'
            if self.new_score:
                score_msg = 'New Best'
            text, text_rect = get_message('Press any Key to Restart', 40)
            score, score_rect = get_message(
                f'{score_msg}: {self.points}',
                20,
                height=SCREEN_HEIGHT // 2 + 50
            )
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)
            self.draw_stats()

    def draw_stats(self):
        for enum, stat in enumerate(self.stats.keys()):
            pos_y = (SCREEN_HEIGHT//2) + (enum * 20)
            stat_text = ' '.join(stat.split('_')).capitalize()
            text, text_rect = get_message(
                f'{stat_text}: {self.stats[stat]}',
                20,
                SCREEN_WIDTH - SCREEN_WIDTH//6,
                pos_y
            )
            self.screen.blit(text, text_rect)

    def reset(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.power_up_manager = PowerUpManager()
        self.obstacle_manager = ObstacleManager()
        self.points = 0

    def set_stats_value(self):
        for stat in self.player.counts.keys():
            self.stats[stat] += self.player.counts[stat]
        self.stats['dead'] += 1
        self.stats['total_points'] += self.points
        if self.stats['best_score'] < self.points:
            self.stats['best_score'] = self.points
            self.new_score = True
        else:
            self.new_score = False
