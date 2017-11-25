import pygame, sys, math as mt
pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
ColorPicked = (255, 0 ,0)
DrawSize = 3
pygame.draw.rect(screen, (255, 255, 255), [0, 0, width, height])
pos1 = (0, 0)
while True:
    CursorPosition = pygame.mouse.get_pos()
    MouseClicked = pygame.mouse.get_pressed()
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1337)
    if key[pygame.K_1]:
        ColorPicked = (255, 0, 0)  # Red
    if key[pygame.K_2]:
        ColorPicked = (0, 255, 0)  # Green
    if key[pygame.K_3]:
        ColorPicked = (0, 0, 255)  # Blue
    if key[pygame.K_4]:
        ColorPicked = (255, 255, 255)  # White
    if key[pygame.K_LEFTBRACKET]:
        DrawSize +=0.001
    if key[pygame.K_RIGHTBRACKET] and DrawSize>0:
        DrawSize -=0.001
    if MouseClicked[0] == 1 and before == False:
        before = True
        pos1 = CursorPosition
    elif MouseClicked[0] == 1 and before == True:
        pygame.draw.line(screen, ColorPicked, pos1, CursorPosition, mt.floor(DrawSize))
        pos1 = CursorPosition
    else:
        before = False
    print(DrawSize)
    pygame.display.flip()
