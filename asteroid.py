import pygame
import random

class Asteroid:
	def __init__(self, SCR_WIDTH, SCR_HEIGHT):
		self.SCR_WIDTH = SCR_WIDTH
		self.SCR_HEIGHT = SCR_HEIGHT
		self.centx = random.random() * SCR_WIDTH
		self.centy = random.random() * SCR_HEIGHT
		self.radius = 40	
		self.xvel = 1
		self.yvel = 1
		if random.random() > .5:
			self.xvel = -self.xvel
		if random.random() > .5:
			self.yvel = -self.yvel

	def move(self):
		self.centx += self.xvel
		self.centy += self.yvel
		if self.centx > self.SCR_WIDTH - 1:
			self.centx = 0
		if self.centx < 0:
			self.centx = self.SCR_WIDTH - 1
		if self.centy > self.SCR_HEIGHT - 1:
			self.centy = 0
		if self.centy < 0:
			self.centy = self.SCR_HEIGHT - 1

	def render(self, screen):
		pygame.draw.circle(screen, (255,255,255), (int(self.centx), int(self.centy)), self.radius, 1)
