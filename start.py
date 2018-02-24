#coding:gb2312
import pygame
import functions as gf
from rain import Rain
from pygame.sprite import Group
from settings import Settings
def run_game():
	#初始化
	pygame.init()
	al_setting = Settings()
	#初始化屏幕
	screen = pygame.display.set_mode((al_setting.screen_width,
	al_setting.screen_height))
	pygame.display.set_caption("rains")
	#创建雨滴实例和组
	rain = Rain(al_setting,screen)
	rains = Group()
	#获得雨滴组
	gf.rain_get(al_setting,screen,rains)
	while True:
		#鼠标键盘点击事件
		gf.check_event()
		#更新雨滴组
		gf.rain_update(al_setting,screen,rains)
		#更新屏幕
		gf.screen_update(al_setting,screen,rains)
run_game()
