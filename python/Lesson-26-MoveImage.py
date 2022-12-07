import pygame

#---- Set screen

MAX_X = 800
MAX_Y = 600
game_over = False
# bg_color = (red, green, blue)
bg_color = (0, 1, 0)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("Hello my First PyGame! :)")

myimage = pygame.image.load("i7processor.png").convert()
myimage = pygame.transform.scale(myimage, (100, 100))

x = 400
y = 200

# ------ Main game loop -------------
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()

