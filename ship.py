# import asteroids
import math
import pygame

class Ship:
	angle = 0
	rotate_left = False
	rotate_right = False
	thrusting = False
	fire = False
	xvel = 0
	yvel = 0
	# centx = 0
	# centy = 0
	ROTATE_SPEED = 9
	THRUST = .5
	MAX_VEL = 5
	FRICTION = .025
	BULLET_VEL = 8
	BULLET_LIFE = 60
	# bullets = []
	BASE_LENGTH = 5	
	# points = []
	RADIUS = 10

	def __init__(self, SCR_WIDTH, SCR_HEIGHT):
		for i in range(3):
			self.SCR_WIDTH = SCR_WIDTH
			self.SCR_HEIGHT = SCR_HEIGHT
			self.centx = SCR_WIDTH / 2
			self.centy = SCR_HEIGHT / 2
			x = self.centx + math.cos(math.radians(self.angle + (i * 120))) * self.RADIUS
			y = self.centy + math.sin(math.radians(self.angle + (i * 120))) * self.RADIUS
			self.points = []
			self.points.insert(i, (x,y))
			self.bullets = []

	def rotate(self, centx, centy):
		global angle
		self.points = []
		for i in range(3):
			x = self.centx + math.cos(math.radians(self.angle + (i * 120))) * self.RADIUS
			y = self.centy + math.sin(math.radians(self.angle + (i * 120))) * self.RADIUS
			self.points.insert(i, (x, y))
		
	def wrap(self):
		if self.centx > self.SCR_WIDTH:
			self.centx = 0
		if self.centx < 0:
			self.centx = self.SCR_WIDTH
		if self.centy > self.SCR_HEIGHT:
			self.centy = 0
		if self.centy < 0:
			self.centy = self.SCR_HEIGHT
		return (self.centx, self.centy)	

	def trans(self):
		translated = []
		for i in range(3):
			x = self.points[i][0] + self.xvel
			y = self.points[i][1] + self.yvel
			translated.insert(i,(x,y))	
		self.points = translated

	def thrust(self, angle):
		xvel = math.cos(math.radians(angle)) * self.THRUST
		yvel = math.sin(math.radians(angle)) * self.THRUST
		return (xvel, yvel)

	def fire_bullet(self, angle, x, y):
		self.bullets.append([self.angle, x, y, Ship.BULLET_LIFE])

	def update_bullets(self):
		for bullet in self.bullets:
			bullet[3] -= 1
			if bullet[3] > 0:
				bullet[1] = bullet[1] + math.cos(math.radians(bullet[0])) * Ship.BULLET_VEL
				bullet[2] = bullet[2] + math.sin(math.radians(bullet[0])) * Ship.BULLET_VEL
			else:
				self.bullets.remove(bullet)


	def render(self, screen):
		pygame.draw.line(screen, (255,255,255), (self.points[0][0], self.points[0][1]), (self.points[1][0], self.points[1][1]))
		pygame.draw.line(screen, (255,255,255), (self.points[2][0], self.points[2][1]), (self.points[0][0], self.points[0][1]))
		pygame.draw.line(screen, (255,255,255), (self.centx, self.centy), (self.points[1][0], self.points[1][1]))
		pygame.draw.line(screen, (255,255,255), (self.centx, self.centy), (self.points[2][0], self.points[2][1]))	
