from pygame import image
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

DEAD = image.load(os.path.join(IMG_DIR, 'Dino/DinoDead.png'))

RUNNING = [
    image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
