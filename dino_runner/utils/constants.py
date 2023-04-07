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
    image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    image.load(os.path.join(IMG_DIR, 'Dino/DinoRun1Hammer.png')),
    image.load(os.path.join(IMG_DIR, 'Dino/DinoRun2Hammer.png')),
]

JUMPING = image.load(os.path.join(IMG_DIR, 'Dino/DinoJump.png'))
JUMPING_SHIELD = image.load(os.path.join(IMG_DIR, 'Dino/DinoJumpShield.png'))
JUMPING_HAMMER = image.load(os.path.join(IMG_DIR, 'Dino/DinoJumpHammer.png'))

DUCKING = [
    image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck1.png')),
    image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck2.png')),
]

DUCKING_SHIELD = [
    image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck1Shield.png')),
    image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck2Shield.png')),
]

DUCKING_HAMMER = [
    image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck1Hammer.png')),
    image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck2Hammer.png')),
]

SMALL_CACTUS = [
    image.load(os.path.join(IMG_DIR, 'Cactus/SmallCactus1.png')),
    image.load(os.path.join(IMG_DIR, 'Cactus/SmallCactus2.png')),
    image.load(os.path.join(IMG_DIR, 'Cactus/SmallCactus3.png')),
]
LARGE_CACTUS = [
    image.load(os.path.join(IMG_DIR, 'Cactus/LargeCactus1.png')),
    image.load(os.path.join(IMG_DIR, 'Cactus/LargeCactus2.png')),
    image.load(os.path.join(IMG_DIR, 'Cactus/LargeCactus3.png')),
]

BIRD = [
    image.load(os.path.join(IMG_DIR, 'Bird/Bird1.png')),
    image.load(os.path.join(IMG_DIR, 'Bird/Bird2.png')),
]

SHIELD = image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

# Background Scene

CLOUD = image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))

BG = image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_1 = image.load(os.path.join(IMG_DIR, 'Other/DinoBackground1.png'))
BG_2 = image.load(os.path.join(IMG_DIR, 'Other/DinoBackground2.png'))

HEART = image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = 'default'
SHIELD_TYPE = 'shield'
HAMMER_TYPE = 'hammer'

DATA_SAVE = './data.json'

DEFAULT_STATS = {
    'best_score': 0,
    'total_points': 0,
    'jumps': 0,
    'obstacles_jump': 0,
    'obstacles_destroy': 0,
    'dead': 0,
    'shields': 0,
    'hammers': 0
}
