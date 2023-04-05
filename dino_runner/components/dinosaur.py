from dino_runner.utils.constants import (
    RUNNING,
    DUCKING,
    JUMPING,
    RUNNING_SHIELD,
    DUCKING_SHIELD,
    JUMPING_SHIELD,
    RUNNING_HAMMER,
    DUCKING_HAMMER,
    JUMPING_HAMMER,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    HAMMER_TYPE,
    DEAD
)
from pygame import K_DOWN, K_UP
from pygame.time import get_ticks


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCKING = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = {
            DEFAULT_TYPE: RUNNING,
            SHIELD_TYPE: RUNNING_SHIELD,
            HAMMER_TYPE: RUNNING_HAMMER,
        }
        self.duck_img = {
            DEFAULT_TYPE: DUCKING,
            SHIELD_TYPE: DUCKING_SHIELD,
            HAMMER_TYPE: DUCKING_HAMMER
        }
        self.jump_img = {
            DEFAULT_TYPE: JUMPING,
            SHIELD_TYPE: JUMPING_SHIELD,
            HAMMER_TYPE: JUMPING_HAMMER
        }
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_live = True
        self.shield = False
        self.time_up_power_up = 0

    def update(self, user_input) -> None:
        if not self.dino_live:
            self.image = DEAD
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        elif self.dino_run:
            self.run()

        if user_input[K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_input[K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif user_input[K_DOWN] and self.dino_jump:
            self.jump_vel -= 1.5
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

        if self.shield:
            time_show = round(
                (self.time_up_power_up - get_ticks()) / 1000,
                2
            )
            if time_show < 0:
                self.reset()

    def draw(self, screen) -> None:
        screen.blit(self.image, self.dino_rect)

    def run(self):
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCKING
        self.step_index += 1

    def set_power_up(self, power_up):
        if power_up.type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
            self.shield = True
            self.time_up_power_up = power_up.time_up

    def reset(self):
        self.type = DEFAULT_TYPE
        self.shield = False
        self.time_up_power_up = 0
