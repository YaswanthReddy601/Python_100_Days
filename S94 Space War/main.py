import pygame
import os
pygame.font.init()# Initialise the pygame font library
pygame.mixer.init()#Initialising the Sound effect library

WIDTH, HEIGHT= 900,500
WINDOW= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("first_game")

WHITE= (255, 255, 255)
BLACK= (0, 0, 0)
RED= (255, 0, 0)
YELLOW= (255, 255, 0)
BORDER= pygame.Rect(WIDTH//2-2.5, 0, 5, HEIGHT)
HEALTH_FONT= pygame.font.SysFont("comicsans", 40)
WINNER_FONT= pygame.font.SysFont("comicsans", 100)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT= 50, 50
RED_SHIP_IMAGE= pygame.image.load(os.path.join("Assets","spaceship_red.png"))
#Resizing
RED_SHIP= pygame.transform.rotate(pygame.transform.scale(RED_SHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
YELLOW_SHIP_IMAGE= pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SHIP= pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))

BULLET_HIT_SOUND= pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))
BULLET_FIRE_SOUND= pygame.mixer.Sound(os.path.join("Assets", "Gun+Silencer.mp3"))


YELLOW_HIT= pygame.USEREVENT + 1
RED_HIT= pygame.USEREVENT + 2

FPS=60
VEL=5
BULLET_VEL= 8

MAX_RED_BULLETS= 4
MAX_YELLOW_BULLETS= 4

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):

    WINDOW.blit(SPACE, (0,0))
    pygame.draw.rect(WINDOW, BLACK, BORDER)
    #To write something on surface of window
    WINDOW.blit(YELLOW_SHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SHIP, (red.x, red.y))

    red_health_text= HEALTH_FONT.render("Health: "+ str(red_health) , 1, WHITE)
    yellow_health_text= HEALTH_FONT.render("Health: "+ str(yellow_health) , 1, WHITE)
    WINDOW.blit(yellow_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WINDOW.blit(red_health_text, (10, 10))

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    pygame.display.update()

def display_winner(text):
    winner= WINNER_FONT.render(text, 1, WHITE)
    WINDOW.blit(winner, (WIDTH//2 - winner.get_width()/2, HEIGHT//2 - winner.get_height()/2))

    pygame.display.update()
    pygame.time.delay(2000)


def red_movement(pressed_key, red):
    if pressed_key[pygame.K_a] and red.x - VEL > 0 :  # "LEFT":
        red.x -= VEL
    if pressed_key[pygame.K_d] and red.x + VEL + red.width < BORDER.x:  # "RIGHT":
        red.x += VEL
    if pressed_key[pygame.K_w] and red.y - VEL > 0:  # "UP":
        red.y -= VEL
    if pressed_key[pygame.K_s] and red.y + VEL + red.height < HEIGHT:  # "DOWN":
        red.y += VEL

def yellow_movement(pressed_key, yellow):
    if pressed_key[pygame.K_LEFT] and yellow.x - VEL > BORDER.x + BORDER.width :  # "LEFT":
        yellow.x -= VEL
    if pressed_key[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < WIDTH:  # "RIGHT":
        yellow.x += VEL
    if pressed_key[pygame.K_UP] and yellow.y - VEL > 0:  # "UP":
        yellow.y -= VEL
    if pressed_key[pygame.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT:  # "DOWN":
        yellow.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in red_bullets:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
            BULLET_HIT_SOUND.play()
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)
    for bullet in yellow_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            BULLET_HIT_SOUND.play()
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)


def main():
    red= pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow= pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []
    red_health = 5
    yellow_health= 5
    clock= pygame.time.Clock()
    run= True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_RED_BULLETS:
                    bullet= pygame.Rect(red.x + red.width, red.y + red.height//2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_YELLOW_BULLETS:
                    bullet= pygame.Rect(yellow.x , yellow.y + yellow.height//2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1

            if event.type == YELLOW_HIT:
                yellow_health -= 1

            winner_text= ""
            if red_health <= 0:
                winner_text= "Yellow Wins"

            if yellow_health <=0:
                winner_text= "Red Wins"

            if winner_text != "":
                display_winner(winner_text)
                run = False

        pressed_key= pygame.key.get_pressed()
        red_movement(pressed_key, red)
        yellow_movement(pressed_key, yellow)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    pygame.quit()
    # main()
if __name__=="__main__":
    main()
