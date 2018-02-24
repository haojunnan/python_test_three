#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Rain(Sprite):
	"""创建一个雨滴"""
	def __init__(self,al_setting,screen):
		"""初始化雨滴并确定其位置"""
		super(Rain,self).__init__()
		self.screen = screen
		self.al_setting = al_setting
		self.image = pygame.image.load("rain.bmp")
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.y = float(self.rect.y)
	def update(self):
		"""如果雨滴未到达底边，继续下落"""
		self.y += self.al_setting.rain_speed
		self.rect.y = self.y
