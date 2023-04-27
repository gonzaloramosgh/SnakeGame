

import pygame
import random

''' Pygame Initializer'''
pygame.init()

'''Pygame Window Config'''
HEIGHT = 400
WIDTH = 600

''' RGB Colors '''
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

window = pygame.display.set_mode ((HEIGHT, WIDTH))
pygame.display.set_caption ('Snake Game')
fps = pygame.time.Clock ()

font = pygame.font.Font(None,50)
font2 = pygame.font.Font(None,35)
run = True


'''Snake Class'''
class Snake ():
	def __init__(self):
		self.head = [100, 150]
		self.body = [ [100, 150], [90, 150], [80, 150] ]


class Food ():
	def __init__(self):
		self.pos_x = random.randint (2, 38) * 10
		self.pos_y = random.randint (12, 55) * 10
		self.pos = [self.pos_x, self.pos_y]


_snake = Snake ()
_food = Food ()
move = 'wait'
score = 0
level = 1


while run:
	for event in pygame.event.get ():
		if event.type == pygame.QUIT:
			run = False
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if move != 'down':
					move = 'up'
				else:
					pass
			if event.key == pygame.K_DOWN:
				if move != 'up':
					move = 'down'
				else:
					pass
			if event.key == pygame.K_LEFT:
				if move != 'right':
					move = 'left'
			if event.key == pygame.K_RIGHT:
				if move != 'left':
					move = 'right'
				else:
					pass
				#
			#
		#
	#
	if move == 'wait':
		pass
	if move == 'up':
		_snake.head[1] -= 10
	if move == 'down':
		_snake.head[1] += 10
	if move == 'left':
		_snake.head[0] -= 10
	if move == 'right':
		_snake.head[0] += 10

	_snake.body.insert(0, list(_snake.head))

	if _snake.head == _food.pos:
		score += 1
		_food = Food()
	else:
		_snake.body.pop()
	window.fill ((0, 0, 0))

	''' Draw Snake '''
	for pos in _snake.body:
		pygame.draw.rect(window, GREEN, pygame.Rect(pos[0],pos[1],10,10),2,2,2,2)


	''' Collision Detection '''
	if move != 'wait':
		for i in _snake.body[1::]:
			if _snake.head == i:
				window.fill(BLACK)
				score -= 1
				move = 'wait'
				print('Toca')


	''' Snake Speed Config '''
	if score < 5:
		fps.tick(10)
	if score >= 5 and score < 10:
		fps.tick(15)
		level = 2
	if score >= 10:
		fps.tick(20)
		level = 3


	if _snake.head[0] > 380 or _snake.head[0] < 10:
		run = False
	if _snake.head[1] > 580 or _snake.head[1] < 110:
		run = False


	pygame.draw.rect(window,RED,pygame.Rect(_food.pos[0],_food.pos[1],10,10))
	pygame.draw.rect(window,(0,255,100),pygame.Rect(0,100,400,500),10)
	pygame.draw.rect(window,(0,255,100),pygame.Rect(0,0,400,99),10)

	'''Render Score and Level info'''

	text = font.render('Score',True,(255,100,10))
	text2 = font.render ('Level', True, (255, 100, 10))
	text3 = font.render (str(score), True, (255, 100, 10))
	text4 = font.render (str(level), True, (255, 100, 10))
	text5 = font2.render (str(fps), True, (255, 100, 10))
	window.blit(text,(15,20))
	window.blit (text3, (120, 20))
	window.blit(text2,( 250,20))
	window.blit(text4,( 350,20))
	window.blit(text5,( 60,45))


	pygame.display.flip()

pygame.quit ()