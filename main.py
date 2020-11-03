import pygame
import sys

W, H = 800, 600
w, h = 50, 50
x = (W - W) // 2
y = H // 2 - h * 2
red = (250, 0, 0)
navy = (5, 0, 50)

pygame.init()
pygame.display.set_caption('Текст')
screen = pygame.display.set_mode((W, H))

background = pygame.Surface(screen.get_size())
background.fill(navy)


font = pygame.font.Font(None, 96)
text = font.render("Всем привет", 1, (250, 250, 250), None)
text_pos = text.get_rect(center=(W // 2, H // 2))

font2 = pygame.font.Font(None, 48)
text2 = font2.render("задание на урок", 1, (250, 250, 250), None)
text_pos2 = text2.get_rect(center=(W // 2, H // 2 + font.get_height()))

font = pygame.font.SysFont('Arial', 96, True, False)
font2 = pygame.font.SysFont('Arial', 48, False, True)
font_box = pygame.Surface((W - 50, font.get_height()))
font_box_rect = font_box.get_rect(center=(W // 2, H - 50))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

pygame.display.set_caption(text, pos, font, font2):
    screen.blit(text_pos)
    screen.blit(font2.render(text, True, red), (pos[0] + 5, pos[1] + 5))
    screen.blit(text_pos)
    screen.blit(font.render(text, True, navy), (pos[0] + 5, pos[1] + 5)) 