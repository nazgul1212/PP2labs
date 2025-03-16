import pygame
import datetime


pygame.init()
W, H = 600, 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey Clock")

time_font = pygame.font.Font('/Users/nazekkhurshitova/Desktop/pp2labs/lab7/font_user.ttf', 24)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

def system_time(now):
    global time_font
    
    min = now.strftime('%M')
    sec = now.strftime('%S')
    
    sc_text = time_font.render(f"{min}:{sec}", 1, RED, YELLOW)
    pos = sc_text.get_rect()

    pos.x, pos.y = 500, 350
    sc.blit(sc_text, pos)



clock_sc = pygame.image.load('/Users/nazekkhurshitova/Desktop/pp2labs/lab7/mickey img/clock.png').convert_alpha()
leftarm_sc = pygame.image.load('/Users/nazekkhurshitova/Desktop/pp2labs/lab7/mickey img/sec_hand.png').convert_alpha()
rightarm_sc = pygame.image.load('/Users/nazekkhurshitova/Desktop/pp2labs/lab7/mickey img/min_hand.png').convert_alpha()

clock_sc = pygame.transform.scale(clock_sc, (W, H))
leftarm_sc = pygame.transform.scale(leftarm_sc, (leftarm_sc.get_width()//2.0, leftarm_sc.get_height()//2.0))
rightarm_sc = pygame.transform.scale(rightarm_sc, (rightarm_sc.get_width()//2.0, rightarm_sc.get_height()//2.0))

angle = 0

clock = pygame.time.Clock()

leftarm_rect = leftarm_sc.get_rect(center=(W//2, H//2))
rightarm_rect = rightarm_sc.get_rect(center=(W//2, H//2))

sc.blit(leftarm_sc, leftarm_rect)
sc.blit(rightarm_sc, rightarm_rect)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    now = datetime.datetime.now()
    sc.fill((255, 255, 255))
    sc.blit(clock_sc, (0, 0))

    angle = -(now.second+1)*6
    angle2 = -(now.minute)*6

    leftarm_sc_rotated = pygame.transform.rotate(leftarm_sc, angle)
    leftarm_rect_rotated = leftarm_sc_rotated.get_rect(center=leftarm_rect.center)

    rightarm_sc_rotated = pygame.transform.rotate(rightarm_sc, angle2-54)
    rightarm_rect_rotated = rightarm_sc_rotated.get_rect(center = rightarm_rect.center)

    
    sc.blit(leftarm_sc_rotated, leftarm_rect_rotated)
    sc.blit(rightarm_sc_rotated, rightarm_rect_rotated)

    system_time(now)
    
    pygame.display.update()

    clock.tick(1)