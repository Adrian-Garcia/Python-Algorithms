import pygame

pygame.init()

clock = pygame.time.Clock()
speed = 30

display_width = 500
display_height = 300

x = 100
y = 100
radius = 10
dx = 3
dy = 3

paddle_x = 10
paddle_y = 10
paddle_width = 3
paddle_height = 40

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
	if x - radius <= paddle_x + paddle_width and y > paddle_y and y < paddle_y + paddle_height:
		return True
	return False

def game_over():
	exit

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Let's Pong!")

while True:
	clock.tick(speed)

	pressed_key = pygame.key.get_pressed()

	if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
		if paddle_y + paddle_height + 10 <= display_height:
			paddle_y += 10

	if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w] :
		if paddle_y - 10 >= 0:
			paddle_y -= 10

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	display.fill((0, 0, 0))
	x += dx
	y += dy

	pygame.draw.rect(display, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
	pygame.draw.circle(display, (255, 255, 255), (x, y), radius)

	if x < radius:
		game_over()

	if hit_back() or hit_paddle():
		dx *= -1

	if hit_sides():
		dy *= -1

	pygame.display.update()


