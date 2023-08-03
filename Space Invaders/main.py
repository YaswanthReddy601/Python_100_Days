import random
import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600,700
RED= (255, 0, 0)
WINDOW= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE INVADER")
LIVES_FONT= pygame.font.SysFont("comicsans", 30)
LEVEL_FONT= pygame.font.SysFont("comicsans", 30)

SPACE= pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background-black.png")), (WIDTH, HEIGHT))
SHIP= pygame.transform.scale(pygame.image.load(os.path.join("Assets", "spaceship_red.png")), (40, 40))

BULLET_SHOT_SOUND= pygame.mixer.Sound(os.path.join("Assets", "Gun+Silencer.mp3"))
COLLISION_SOUND= pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))

WHITE= (255, 255, 255)
MOVE= 5
BULLET_MOVE= 7
LIVES= 3
LEVEL= 0
ENEMY_SHIP_SPEED = 1
def draw_window(fighter_ship, all_bullets, enemies):
    WINDOW.blit(SPACE, (0, 0))
    WINDOW.blit(SHIP, (fighter_ship.x, fighter_ship.y))
    lives_text= LIVES_FONT.render("Lives: "+str(LIVES), 1, WHITE)
    WINDOW.blit(lives_text, (10, 10))
    level_text = LEVEL_FONT.render("Level: " + str(LEVEL), 1, WHITE)
    WINDOW.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))


    for enemy in enemies:
        pygame.draw.rect(WINDOW, random.choice(["red", "green", "blue"]),enemy)

    for bullet in all_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)
    pygame.display.update()


def ship_movement(key_pressed, fighter_ship):

    if key_pressed[pygame.K_LEFT] and fighter_ship.x > 0:
        fighter_ship.x -= MOVE
    if key_pressed[pygame.K_RIGHT] and fighter_ship.x < WIDTH - fighter_ship.width:
        fighter_ship.x += MOVE
    if key_pressed[pygame.K_UP] and fighter_ship.y > 10:
        fighter_ship.y -= MOVE
    if key_pressed[pygame.K_DOWN] and fighter_ship.y < HEIGHT - fighter_ship.height:
        fighter_ship.y += MOVE

def bullet_handling(all_bullets):
    for bullet in all_bullets:
        bullet.y -= BULLET_MOVE
        if bullet.y < 0:
            all_bullets.remove(bullet)


def handle_enemies(enemies, all_bullets, fighter_ship):
    global LIVES
    for enemy in enemies:
        enemy.y += ENEMY_SHIP_SPEED + 1
        for bullet in all_bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                all_bullets.remove(bullet)
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            LIVES -= 1

        if enemy.colliderect(fighter_ship):
            COLLISION_SOUND.play()
            LIVES -= 1
            enemies.remove(enemy)

def game_over_display(text):
    game_over= LIVES_FONT.render(text, 1, WHITE)
    WINDOW.blit(game_over, (WIDTH//2-game_over.get_width()//2, HEIGHT//2-game_over.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global LEVEL, ENEMY_SHIP_SPEED, LIVES
    fighter_ship= pygame.Rect(WIDTH//2-SHIP.get_width()//2,HEIGHT//2 + HEIGHT//3, 40, 40)
    all_bullets= []
    enemies = []
    wave_size = 0
    clock= pygame.time.Clock()
    run= True
    while run:
        clock.tick(60)
        if len(enemies) == 0:
            LEVEL +=1
            wave_size +=5
            for i in range(0, wave_size):
                enemy = pygame.Rect(random.randrange(50, WIDTH-100), random.randrange(-1500 * LEVEL//2, -100),20, 20)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(all_bullets) < 6:
                    bullet= pygame.Rect(fighter_ship.x+fighter_ship.width//2, fighter_ship.y, 5, 10)
                    all_bullets.append(bullet)
                    BULLET_SHOT_SOUND.play()

        if LIVES == 0:
            text= "GAME OVER"
            game_over_display(text)
            run = False

        key_pressed= pygame.key.get_pressed()
        ship_movement(key_pressed, fighter_ship)
        bullet_handling(all_bullets)
        handle_enemies(enemies, all_bullets, fighter_ship)
        draw_window(fighter_ship, all_bullets, enemies)

    pygame.quit()

if __name__=="__main__":
    main()



