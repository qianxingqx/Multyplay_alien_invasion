
import sys
import pygame
from bullet import Bullet
from bullet2 import Bullet2
from alien import Alien
from random import randint
from time import sleep
# 创建随机数
#random_num = randint(-10, 10)

def fire_bullet(ai_settings, screen, ship, bullets, ship2):
	# 创建一颗子弹
	
	if len(bullets) < ai_settings.bullets_num:
		new_bullet = Bullet(ai_settings, screen, ship, ship2)
		bullets.add(new_bullet)

def fire_bullets2(ai_settings, screen, ship, bullets, ship2, bullets2):

	if len(bullets2) < ai_settings.bullets_num:
		new_bullet = Bullet2(ai_settings, screen, ship2)
		bullets2.add(new_bullet)


def fire_bullet3(ai_settings, screen, ship, bullets, ship2):
	# 创建一颗子弹
	
	if len(bullets) < ai_settings.bullets_num:
		new_bullet = Bullet(ai_settings, screen,ship, ship2)
		bullets.add(new_bullet)
		#bullets.x = ship2.rect.centerx
		#bullets.y = ship2.rect.top
		new_bullet.weizhi(ship2)
	
		
def fire_conti(ai_settings, screen, ship, bullets, ship2):
	# 子弹持续发射
	if ship.flag:
		fire_bullet(ai_settings, screen, ship, bullets, ship2)

def check_keydown(event, ai_settings, screen, ship, bullets, ship2, bullets2):
	""" 按下按键 """
	# 飞船移动
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	
	elif event.key == pygame.K_d:
		ship2.moving_right = True
	elif event.key == pygame.K_a:
		ship2.moving_left = True
	elif event.key == pygame.K_w:
		ship2.moving_up = True
	elif event.key == pygame.K_s:
		ship2.moving_down = True
	
	# 退出游戏
	elif event.key == pygame.K_q:
		sys.exit()
	# 创建一颗子弹
    # 按键 P 和 O：飞船一子弹单发
    # 数字键 8：飞船二子弹连发
    # 数字键 9：飞船二子弹单发
	elif event.key == pygame.K_KP9: 
		fire_bullet(ai_settings, screen, ship, bullets, ship2)
	elif event.key == pygame.K_p:
		fire_bullets2(ai_settings, screen, ship, bullets, ship2, bullets2)
	elif event.key == pygame.K_o:
		fire_bullet3(ai_settings, screen, ship, bullets, ship2)	

		
	elif event.key == pygame.K_KP8:
		ship.flag = True
		


def check_keyup(event, ai_settings, screen, ship, bullets, ship2, bullets2):
	""" 松开按键 """
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
	
	elif event.key == pygame.K_d:
		ship2.moving_right = False
	elif event.key == pygame.K_a:
		ship2.moving_left = False
	elif event.key == pygame.K_w:
		ship2.moving_up = False
	elif event.key == pygame.K_s:
		ship2.moving_down = False
		
	elif event.key == pygame.K_KP8:
		ship.flag = False
		
		
def check_events(ai_settings, stats, screen, ship, bullets, aliens, play_button, scoreboard, ship2, bullets2):
	""" 响应按键和鼠标事件 """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		# 检测是否按下鼠标
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, scoreboard, ship2, bullets2)
		
		# 按下按键
		elif event.type == pygame.KEYDOWN:
			check_keydown(event, ai_settings, screen, ship, bullets, ship2, bullets2)
		
		# 松开按键
		elif event.type == pygame.KEYUP:
			check_keyup(event, ai_settings, screen, ship, bullets, ship2, bullets2)		


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, scoreboard, ship2, bullets2):
	# 检测鼠标
	
	# 单击Play
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		# 隐藏鼠标光标
		#pygame.mouse.set_visible(False)
		
		# 重置游戏设置
		ai_settings.init_dynamic()
		
		# 重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True
		
		# 重置记分牌图像
		scoreboard.prep_score()
		scoreboard.prep_high_score()
		scoreboard.prep_level()
		scoreboard.prep_ships()
		
		# 清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()
		bullets2.empty()
		
		# 创建一群新外星人，并让飞船居中
		create_fleet(ai_settings, screen, ship, aliens, ship2, bullets2)
		ship.center_ship()

def update_screen(ai_settings, stats, screen, ship, bullets, aliens, play_button, scoreboard, ship2, bullets2):
	""" 更新屏幕上的图像，并切换到新屏幕 """
	
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet() # 遍历编组红的每个精灵，都调用draw_bullet()
		
	for bullet in bullets2.sprites():
		bullet.draw_bullet() # 遍历编组红的每个精灵，都调用draw_bullet()
	# 绘制飞船
	ship.blitme()
	ship2.blitme()
	# 绘制外星人
	aliens.draw(screen)
	# 显示得分
	scoreboard.show_score()
	
	# 如果游戏处于非活动状态，就绘制Play按钮
	if not stats.game_active:
		play_button.draw_button()
	# 让最近绘制的屏幕可见，即刷新屏幕
	pygame.display.flip()


def update_bullets(ai_settings, stats, screen, ship, bullets, aliens, scoreboard, ship2, bullets2):
	# 更新子弹的位置，是删除已消失的子弹
	
	# 更新子弹位置
	bullets.update()
	bullets2.update()
	
	# 连续发射子弹
	fire_conti(ai_settings, screen, ship, bullets, ship2)
	
	# 删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#print(len(bullets))
	for bullet in bullets2.copy():
		if bullet.rect.bottom <= 0:
			bullets2.remove(bullet)
	# 检查是否有子弹和外星人碰撞，如果有，则删除相应的子弹和外星人
	check_bullet_alien_collisions(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2)

	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2)
	
def check_bullet_alien_collisions(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2):
	# 响应子弹和外星人的碰撞

	#collisions = pygame.sprite.groupcollide(bullets, bullets, True, False)
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) or pygame.sprite.groupcollide(bullets2, aliens, True, True)
	collisions2 = pygame.sprite.groupcollide(bullets2, aliens, True, True)
	#print(collisions)
	
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			scoreboard.prep_score()
	
	if collisions2:
		for aliens in collisions2.values():
			stats.score += ai_settings.alien_points * len(aliens)
			scoreboard.prep_score()
		check_high_score(stats, scoreboard)
		
	if len(aliens) == 0:
		# 删除现有的子弹并新建一群外星人
		bullets.empty()
		bullets2.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, ship, aliens, ship2, bullets2)
		
		# 提高等级
		stats.level += 1
		scoreboard.prep_level()



def get_number_aliens_x(ai_settings, alien_width):
	# 计算每行能容纳的外星人数量
	available_space_x = ai_settings.screen_width - 2 * alien_width # 将左右两边空出一些间隔
	number_aliens_x = int(available_space_x / (2 * alien_width)) # 每个外星人之间含有间隔
	return number_aliens_x
	
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	# 创建一个外星人并将其放在当前行
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
	alien.rect.x = alien.x
	aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
	# 计算屏幕可以容纳多少行外星人
	available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
	number_rows = int(available_space_y/(2*alien_height))
	return number_rows


def create_fleet(ai_settings, screen, ship, aliens, ship2, bullets2):
	# 创建外星人群
	
	# 创建一个外星人，并计算能够容纳多少个外星人
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	
	# 创建第一行外星人
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			if randint(0, 1):
				create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
	# 有外星人到达边缘时采取相应的措施
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break
			

def change_fleet_direction(ai_settings, aliens):
	# 将外星人整体下移，并改变他们的方向
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	alien.ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2):
	# 更新外星人位置，检查外星人和飞船的碰撞
	
	# 检查外星人是否碰撞到到左右边缘
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	
	# 外星人与飞船碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2)
		
	# 外星人与屏幕底部碰撞
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2)



def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2):
	# 响应被外星人碰撞到的飞船，即碰撞发生
	if stats.ships_left > 0:
		stats.ships_left -= 1 # 飞船数减1
		# 更新记分牌
		scoreboard.prep_ships()
		# 清空
		aliens.empty()
		bullets.empty()
		bullets2.empty()
		# 创建新的外星人，并重新放置飞船
		create_fleet(ai_settings, screen, ship, aliens, ship2, bullets2)
		ship.center_ship()
		# 暂停
		sleep(0.5)
	else:
		stats.game_active = False
		#pygame.mouse.set_visible(True)
	

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2):
	# 检查是否有外星人到达了屏幕底端
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2)
			break

def check_high_score(stats, scoreboard):
	# 检查是否诞生了新的最高得分
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		scoreboard.prep_high_score()
