import asteroid
import math
import pygame
from pygame.locals import *
import random
import ship
import sys

'''Pygame constants'''
SCR_WIDTH, SCR_HEIGHT = 640, 480
FPS = 30

'''Misc stff'''
starfield = []
NUM_STARS = 45
asteroids = []
NUM_ASTEROIDS = 3

'''Pygame init'''
pygame.init()
fps_timer = pygame.time.Clock()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))

player = ship.Ship(SCR_WIDTH, SCR_HEIGHT)

def init_starfield():
	global starfield
	for i in range(NUM_STARS):
		x = random.random() * SCR_WIDTH
		y = random.random() * SCR_HEIGHT
		starfield.insert(i, (x,y))

init_starfield()

def init_asteroids():
	for i in range(NUM_ASTEROIDS):
		asteroids.append(asteroid.Asteroid(SCR_WIDTH, SCR_HEIGHT))

init_asteroids()

first_pass = True
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT or event.key == K_d:
				player.rotate_right = True
			elif event.key == K_LEFT or event.key == K_a:
				player.rotate_left = True
			if event.key == K_UP or event.key == K_w:
				player.thrusting = True
			if event.key == K_SPACE:
				player.fire = True
		if event.type == KEYUP:
			if event.key == K_RIGHT or event.key == K_d:
				player.rotate_right = False
			if event.key == K_LEFT or event.key == K_a:
				player.rotate_left = False
			if event.key == K_UP or event.key == K_w:
				player.thrusting = False
			if event.key == K_SPACE:
				player.fire = False
	
	if player.rotate_right:
		player.angle += player.ROTATE_SPEED
	elif player.rotate_left:
		player.angle -= player.ROTATE_SPEED
	
	if player.thrusting:
		vel = player.thrust(player.angle)
		player.xvel += vel[0]
		player.yvel += vel[1]
		if math.fabs(player.xvel) > player.MAX_VEL:
			player.xvel = math.copysign(player.MAX_VEL, player.xvel)
		if math.fabs(player.yvel) > player.MAX_VEL:
			player.yvel = math.copysign(player.MAX_VEL, player.yvel)
	else:
		if math.fabs(player.xvel) > 0.0:
			player.xvel += -(math.copysign(player.FRICTION, player.xvel))
		else:
			player.xvel = 0.0
		if math.fabs(player.yvel) > 0.0:
			player.yvel += -(math.copysign(player.FRICTION, player.yvel))
		else:
			player.yvel = 0.0
	if player.fire:
		player.fire_bullet(player.angle, player.points[0][0], player.points[0][1])

		player.fire = False

	if len(player.bullets) > 0:
		player.update_bullets()
	player.rotate(player.centx, player.centy)
	player.trans()
	player.centx += player.xvel
	player.centy += player.yvel
	
	centroid = player.wrap()
	player.centx = centroid[0]
	player.centy = centroid[1]

	# print('xvel = ' + str(xvel) + ', yvel = ' + str(yvel) + ', angle = ' + str(angle))

	screen.fill((32,32,32))
	for star in starfield:
		pygame.draw.rect(screen, (255,255,255), (star[0], star[1], 2, 2))
	for bullet in player.bullets:
		pygame.draw.rect(screen, (255, 255, 0), (bullet[1], bullet[2], 2, 2))
	for each_asteroid in asteroids:
		each_asteroid.move()
		each_asteroid.render(screen)	
	player.render(screen)

	pygame.display.flip()
	fps_timer.tick(FPS)

