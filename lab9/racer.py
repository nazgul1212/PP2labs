import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Frame rate setup
FPS = 60
clock = pygame.time.Clock()

# Color definitions
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Window size and variables
W, H = 400, 600
SPEED = 5               
SCORE = 0              
COINS = 0              
SPEED_INCREASE_THRESHOLD = 5  

# Fonts and Game Over text
font = pygame.font.Font("font_user.ttf", 60)
font_small = pygame.font.Font("font_user.ttf", 20)
game_over = font.render("Game Over", True, BLACK)

# Load and scale coin icon (UI)
coin_icon = pygame.image.load("im/Coin.png")
coin_icon = pygame.transform.scale(coin_icon, (coin_icon.get_width() // 15, coin_icon.get_height() // 10))

# Background
bg = pygame.image.load("im/AnimatedStreet.png")

# Game window setup
SC = pygame.display.set_mode((W, H))
pygame.display.set_caption("My game")


# Enemy: falling cars to avoid
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("im/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > H:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

# Player: controllable car
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("im/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 1 and pressed_key[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < W and pressed_key[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin: collectible with random weight
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("im/Coin.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 12, self.image.get_height() // 12))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)
        self.value = random.choice([1, 2, 3])  # Each coin has random value (weight)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > H:
            self.reset_position()

    def reset_position(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, W - 40), 0)
        self.value = random.choice([1, 2, 3])  # New random value each time
        


P1 = Player()
E1 = Enemy()

# Groups
enemies = pygame.sprite.Group(E1)
coins_group = pygame.sprite.Group()
for _ in range(3):  # Spawn multiple coins
    coins_group.add(Coin())

all_sprites = pygame.sprite.Group(P1, E1, *coins_group)

# Timer to increase speed manually (optional)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 4000)


# MAIN GAME LOOP


while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Draw background and coin counter
    SC.blit(bg, (0, 0))
    SC.blit(coin_icon, (10, 35))
    coins_v = font_small.render(f"X{str(COINS)}", True, BLACK)
    SC.blit(coins_v, (50, 50))

    # Move and draw sprites
    for entity in all_sprites:
        SC.blit(entity.image, entity.rect)
        entity.move()

    # Check collision with enemy => game over
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('im/crash.wav').play()
        time.sleep(0.5)

        SC.fill(RED)
        SC.blit(game_over, (30, 250))
        result = font_small.render(f"Your result: {COINS}", True, BLACK)
        SC.blit(result, (120, 350))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check collision with coins,collect and reset only collected coin
    collected = pygame.sprite.spritecollide(P1, coins_group, dokill=False)
    for coin in collected:
        COINS += coin.value  # Add coin value (1, 2 or 3)
        coin.reset_position()

        # Increase enemy speed every N coins
        if COINS % SPEED_INCREASE_THRESHOLD == 0:
            SPEED += 2


    pygame.display.update()
    clock.tick(FPS)
