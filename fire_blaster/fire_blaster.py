import pygame
import os

pygame.font.init()
pygame.mixer.init()

BULLET_HIT_SOUND_FX = pygame.mixer.Sound(os.path.join("Assets", "Laser_shot.wav"))
BULLET_FIRE_SOUND_FX = pygame.mixer.Sound(os.path.join("Assets", "III - Zap 3 (C).wav"))
WINNER_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Fanfare.wav"))

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fire Blaster 🚀")
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VEL = 5
BULLET_VEL = 10

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

LIGHT_GREEN = (213, 255, 208)
BLACK = (0, 0, 0)
RED = (187, 37, 37)
DARK_BLUE = (20, 30, 70)
DARK_BROWN = (65, 53, 67)

BORDER = pygame.Rect(WIDTH // 2 - 3, 0, 6, HEIGHT)

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

MAX_BULLETS = 3

FPS = 60

PAUSE_BEFORE_NEXT_GAME = 3000

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background.jpeg")), (WIDTH, HEIGHT))


def draw_window(red, yellow, red_bullets, yellow_bullets, yellow_health, red_health):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, DARK_BROWN)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, DARK_BROWN)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, DARK_BLUE, bullet)

    pygame.display.update()


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, DARK_BROWN)
    WIN.blit(draw_text, ((WIDTH - draw_text.get_width()) // 2, HEIGHT // 2 - draw_text.get_height()))
    pygame.display.update()
    WINNER_SOUND.play()
    pygame.time.delay(PAUSE_BEFORE_NEXT_GAME)


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL < BORDER.x - SPACESHIP_WIDTH:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > SPACESHIP_WIDTH // 4:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height + SPACESHIP_WIDTH // 2 < HEIGHT:
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width + SPACESHIP_WIDTH // 4:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - SPACESHIP_WIDTH + SPACESHIP_WIDTH // 4:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > SPACESHIP_WIDTH // 4:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height + SPACESHIP_WIDTH // 2 < HEIGHT:
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    yellow_health = 10
    red_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND_FX.play()

                if event.key == pygame.K_b and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND_FX.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND_FX.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND_FX.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, yellow_health, red_health)

    main()


if __name__ == "__main__":
    main()
