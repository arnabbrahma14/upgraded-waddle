import pygame
import random
import sys

pygame.init()

WIDTH=1200
HEIGHT=700

RED = (255, 0 ,0 )
BLUE = (0 , 0 , 255)
YELLOW = (0,251,250)
BACKGROUND_COLOR = (0,0,0)

player_size = 50
player_pos=[WIDTH/2 , HEIGHT-2*player_size ]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size) , 0]
enemy_list = [enemy_pos]

SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("arial", 35)

def set_level(score, SPEED):
	if score < 10:
		SPEED=10
	elif score <20:
		SPEED = 11 
	elif score < 30:
		SPEED = 12
	elif score < 40:
		SPEED = 13
	elif score <50:
		SPEED = 14 
	elif score < 60:
		SPEED = 15
	elif score < 70:
		SPEED = 16
	elif score < 80:
		SPEED = 17
	elif score < 90:
		SPEED = 18
	elif score < 100:
		SPEED = 19
	else:
		SPEED = score/5-2
	return SPEED


def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE ,(enemy_pos[0], enemy_pos[1], enemy_size ,enemy_size))

def update_enemy_positions(enemy_list, score):
	for idx,enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] <HEIGHT:
			enemy_pos[1] +=SPEED
		else:
			enemy_list.pop(idx)
			score +=1
	return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collison(enemy_pos, player_pos):
			return True
	return False


def detect_collison(player_pos,enemy_pos):
	p_x=player_pos[0]
	p_y=player_pos[1]

	e_x=enemy_pos[0]
	e_y=enemy_pos[1]
	f=False

	if (e_x>=p_x and e_x<= (p_x+player_size) )  and ( e_y>=p_y and e_y< (p_y+player_size) ):
		f=True
	if ( (e_x+enemy_size) >=p_x and (e_x+enemy_size) <= (p_x+player_size) )  and ( (e_y+enemy_size) >=p_y and (e_y+enemy_size) <= (p_y+player_size) ):
		f=True
	return f

while not game_over:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x=player_pos[0]
			y=player_pos[1]

			if event.key == pygame.K_LEFT:
				x -= player_size
			elif event.key == pygame.K_RIGHT:
				x += player_size

			player_pos = [x,y]
	screen.fill(BACKGROUND_COLOR)

	drop_enemies(enemy_list)
	score= update_enemy_positions(enemy_list, score)
	SPEED= set_level(score, SPEED)
	
	text = "Score: "+str(score)
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH-130, HEIGHT-40))

	if collision_check(enemy_list, player_pos):
		game_over = True
		break

	draw_enemies(enemy_list)

	pygame.draw.rect(screen, RED , (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(30)

	pygame.display.update()
