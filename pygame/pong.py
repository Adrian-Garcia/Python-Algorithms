import pygame
import random

pygame.init()

clock = pygame.time.Clock()
speed = 30

display_width = 500
display_height = 300

x = 100
y = 100
radius = 10
dx = 6
dy = 6

paddle_x = 10
paddle_y = 10
paddle_width = 3
paddle_height = 40

play_score = 0


def randomize_start():
    global x, y, dy
    x = random.randint(int(display_width / 4), display_width - 20)
    y = random.randint(10, display_height - 10)

    if random.randint(0, 2) % 2 == 0:
        dy *= -1


def hit_back():
    if x + radius > display_width:
        return True
    return False


def hit_sides():
    if y - radius < 0:
        return True
    if y + radius > display_height:
        return True
    return False


def hit_paddle():
    global play_score

    if (
        x - radius <= paddle_x + paddle_width
        and y > paddle_y
        and y < paddle_y + paddle_height
    ):
        play_score += 100
        return True
    return False


def game_over():
    global play_score

    end_game = True
    display.fill((0, 0, 0))

    font_title = pygame.font.Font(None, 36)
    font_instructions = pygame.font.Font(None, 24)

    announcement = font_title.render("Game Over", True, (255, 255, 255))
    announcement_rect = announcement.get_rect(
        center=(int(display_width / 2), int(display_height / 3))
    )
    display.blit(announcement, announcement_rect)

    qinstructions = font_instructions.render("Press q to Quit", True, (255, 255, 255))
    qinstructions_rect = qinstructions.get_rect(
        center=(int(display_width / 2), int(display_height / 1.5))
    )
    display.blit(qinstructions, qinstructions_rect)

    rinstructions = font_instructions.render("Press r to Resume", True, (255, 255, 255))
    rinstructions_rect = rinstructions.get_rect(
        center=(int(display_width / 2), int(display_height / 1.3))
    )
    display.blit(rinstructions, rinstructions_rect)

    final_score = "Final score: " + str(play_score)

    score_announce = font_instructions.render(final_score, True, (255, 255, 255))
    score_announce_rect = score_announce.get_rect(
        center=(int(display_width / 2), int(display_height / 2))
    )
    display.blit(score_announce, score_announce_rect)

    pygame.display.flip()

    while end_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

                if event.key == pygame.K_r:
                    end_game = False


display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Let's Pong!")

display.fill((0, 0, 0))

welcome_screen = pygame.font.Font(None, 30)
welcome = welcome_screen.render("Let's Play Pong!", True, (255, 255, 255))
welcome_rect = welcome.get_rect(
    center=(int(display_width / 2), int(display_height / 3))
)

startmsg = welcome_screen.render(
    "Hit 'y' to start or autostart in 10 seconds", True, (255, 255, 255)
)
startmsg_rect = startmsg.get_rect(
    center=(int(display_width / 2), int(display_height / 4))
)

display.blit(welcome, welcome_rect)
display.blit(startmsg, startmsg_rect)

pygame.display.flip()
pygame.time.set_timer(pygame.USEREVENT, 5000)

timer_active = True
while timer_active:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            timer_active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                timer_active = False

randomize_start()

while True:
    clock.tick(speed)

    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        if paddle_y + paddle_height + 10 <= display_height:
            paddle_y += 10

    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        if paddle_y - 10 >= 0:
            paddle_y -= 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill((0, 0, 0))
    x += dx
    y += dy

    pygame.draw.rect(
        display, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height)
    )
    pygame.draw.circle(display, (255, 255, 255), (x, y), radius)

    if x < radius:
        game_over()
        randomize_start()
        dx = abs(dx)
        play_score = 0

    if hit_back() or hit_paddle():
        dx *= -1

    if hit_sides():
        dy *= -1

    pygame.display.update()
