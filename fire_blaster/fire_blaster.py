import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fire Blaster")

LIGHT_GREEN = (213, 255, 208)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

FPS = 60
SHIP_SIZE = (70, 50)
MOVEMENT_SPEED = 5

YELLOW_SPACESHIP_IMG = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG, SHIP_SIZE), 90)

RED_SPACESHIP_IMG = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG, SHIP_SIZE), 270)


def draw_window(red, yellow):
    WIN.fill(LIGHT_GREEN)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def movement_controls_yellow(keys, yellow_ship, speed):
    if keys[pygame.K_a] and yellow_ship.x - speed > 0:
        yellow_ship.x -= speed
    if keys[pygame.K_d] and yellow_ship.x + speed < (BORDER.x - SHIP_SIZE[1]):
        yellow_ship.x += speed
    if keys[pygame.K_w] and yellow_ship.y - speed > 0:
        yellow_ship.y -= speed
    if keys[pygame.K_s] and yellow_ship.y + speed + SHIP_SIZE[0] < HEIGHT:
        yellow_ship.y += speed


def movement_controls_red(keys, red_ship, speed):
    if keys[pygame.K_LEFT]:
        red_ship.x -= speed
    if keys[pygame.K_RIGHT]:
        red_ship.x += speed
    if keys[pygame.K_UP]:
        red_ship.y -= speed
    if keys[pygame.K_DOWN]:
        red_ship.y += speed


def main():
    red = pygame.Rect(750, 200, WIDTH, HEIGHT)
    yellow = pygame.Rect(100, 200, WIDTH, HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        movement_controls_yellow(keys_pressed, yellow, MOVEMENT_SPEED)
        movement_controls_red(keys_pressed, red, MOVEMENT_SPEED)

        draw_window(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
