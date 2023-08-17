import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fire Blaster")

LIGHT_GREEN = (213, 255, 208)
BLACK = (0, 0, 0)
RED = (194, 51, 115)
YELLOW = (247, 233, 135)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

FPS = 60
SHIP_SIZE = (70, 50)
MOVEMENT_SPEED = 5
BULLET_SPEED = 7
MAX_BULLETS = 5

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMG = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG, SHIP_SIZE), 90)

RED_SPACESHIP_IMG = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG, SHIP_SIZE), 270)


def draw_window(red, yellow, red_bull, yellow_bull):
    WIN.fill(LIGHT_GREEN)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

    for bullet in red_bull:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bull:
        pygame.draw.rect(WIN, YELLOW, bullet)


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
    if keys[pygame.K_LEFT] and red_ship.x - speed > BORDER.x + 10:
        red_ship.x -= speed
    if keys[pygame.K_RIGHT] and red_ship.x + speed < WIDTH - SHIP_SIZE[1]:
        red_ship.x += speed
    if keys[pygame.K_UP] and red_ship.y - speed > 0:
        red_ship.y -= speed
    if keys[pygame.K_DOWN] and red_ship.y + speed + SHIP_SIZE[0] < HEIGHT:
        red_ship.y += speed


def handle_bullets(yellow_player, red_player, yellow_bull, red_bull):
    for bullet in yellow_bull:
        bullet.x += BULLET_SPEED
        if red_player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bull.remove(bullet)

    for bullet in red_bull:
        bullet.x -= BULLET_SPEED
        if yellow_player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bull.remove(bullet)


def main():
    red = pygame.Rect(750, 200, WIDTH, HEIGHT)
    yellow = pygame.Rect(100, 200, WIDTH, HEIGHT)

    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_b and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        movement_controls_yellow(keys_pressed, yellow, MOVEMENT_SPEED)
        movement_controls_red(keys_pressed, red, MOVEMENT_SPEED)

        handle_bullets(yellow, red, yellow_bullets, red_bullets, )

        draw_window(red, yellow, red_bullets, yellow_bullets)
    pygame.quit()


if __name__ == "__main__":
    main()
