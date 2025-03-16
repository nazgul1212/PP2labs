import pygame

def main():
    width = 1280
    height = 720
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Circle')
    x = 50
    y = 50
    rad = 25
    vel = 20
    clock = pygame.time.Clock()
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - vel > 25: y -= vel
        if pressed[pygame.K_DOWN] and y + vel < 695: y += vel
        if pressed[pygame.K_LEFT] and x - vel > 25 : x -= vel
        if pressed[pygame.K_RIGHT] and x + vel < 1255: x += vel
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), rad, 0)
        
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
        
if __name__ == '__main__':
    pygame.init()
    main()