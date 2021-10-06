import pygame, random, serial
from pygame import *
class GAMES():
	def SNAKEGAME(self):
		def MAIN_GAME():
			pygame.init()
			width, height = 32, 16#Real size in game is one more than the inputed values
			boxSize = 25
			screenwidth, screenheight = width*boxSize+boxSize, height*boxSize+boxSize
			screen=pygame.display.set_mode((screenwidth,screenheight))
			keys= [False, False, False, False]
			Game = True
			playerpositions = [[0,0],[1,0],[2,0]]
			snakebody = []
			direction = 1
			colorRed = (255, 0, 0)
			colorBlack = (0,0,0)
			colorBlue = (0,0,255)
			colorGreen = (0,255,0)
			foodonscreen = False
			xfood, yfood = 0,0
			delete = False
			foodcords = True
			#gameover = pygame.image.load("/Leandri/FPS/resources/images/gameover.png")
			waitforanswer = True

			def addnewpiece(direction, delete):#Function to add new piece to end of tail. If the snake has eaten food, dont delete the other piece.
				if delete == False:
					playerpositions.pop(0)
				if direction == 0:
					#X value
					playerpositions.append([playerpositions[len(playerpositions)-1][0]])
					#Y value
					playerpositions[len(playerpositions)-1].append(playerpositions[len(playerpositions)-2][1]-1)
				elif direction == 1:
					#X value of new coord
					playerpositions.append([playerpositions[len(playerpositions)-1][0]+1])#subtract one from length to call lists
					#Y value of new coord
					playerpositions[len(playerpositions)-1].append(playerpositions[len(playerpositions)-2][1])#subtract two, one for length and one to go to previous list after appended new value in previous step
				elif direction == 2:
					#X value
					playerpositions.append([playerpositions[len(playerpositions)-1][0]])
					#Y value
					playerpositions[len(playerpositions)-1].append(playerpositions[len(playerpositions)-2][1]+1)
				elif direction == 3:
					#X value
					playerpositions.append([playerpositions[len(playerpositions)-1][0]-1])
					#Y value
					playerpositions[len(playerpositions)-1].append(playerpositions[len(playerpositions)-2][1])
			def death():#Function to draw the words for the death screen
				pygame.font.init()
				font = pygame.font.Font(None, 50)
				deathtext = font.render("You Died!", True, colorRed)
				textRect_deathtext = deathtext.get_rect()
				textRect_deathtext.centerx = screen.get_rect().centerx
				textRect_deathtext.centery = screen.get_rect().centery-60
				screen.blit(deathtext, textRect_deathtext)
				font2 = pygame.font.Font(None, 30)
				playagain = font.render("Press p to play again", True, colorRed)
				textRect_playagain = playagain.get_rect()
				textRect_playagain.centerx = screen.get_rect().centerx
				textRect_playagain.centery = screen.get_rect().centery
				screen.blit(playagain, textRect_playagain)
			
			def drawgame():
				#Draw food
				pygame.draw.rect(screen, colorBlue, (xfood*boxSize,yfood*boxSize,boxSize,boxSize), 0)
					
				#Draw snake boxes
				for i in playerpositions:
					pygame.draw.rect(screen, colorGreen, (i[0]*boxSize,i[1]*boxSize,boxSize,boxSize), 0)
				pygame.display.update()
			
			def deathscreen():#Function that puts all of the functions together for the death screen
				drawgame()
				death()
				pygame.display.update()
			
			drawgame()#Update the screen

			while Game:
				pygame.time.delay(200)
				screen.fill(colorBlack)
				for event in pygame.event.get():
					#Check if the event is the x button
					if event.type==pygame.QUIT:
						#If it is, quit the game pygame.quit()
						pygame.quit()
						exit(0)
					if event.type == pygame.KEYDOWN:
						if event.key==K_w:
							keys[0]=True
						elif event.key==K_d:
							keys[1]=True
						elif event.key==K_s:
							keys[2]=True
						elif event.key==K_a:
							keys[3]=True
				#Set direction of snake
				for x in range(len(keys)):
					if keys[x] == True:
						direction = x
						keys[x] = False
						
				#Check if eaten food
				if playerpositions[len(playerpositions)-1] == [xfood, yfood]:
					foodonscreen = False
					delete = True
					addnewpiece(direction, delete)
				else:
					#Create next piece for snake
					delete = False
					addnewpiece(direction, delete)
				#Food
				if foodonscreen == False:
					foodcords = True
					while foodcords:
						xfood = random.randint(0,width)
						yfood = random.randint(0,height)
						foodcords = False
						if [xfood, yfood] in playerpositions:
							foodcords = True
						foodonscreen = True
						
				#Check if death
				snakebody = []
				for x in range(len(playerpositions)-2):
					snakebody.append(playerpositions[x])
				if playerpositions[len(playerpositions)-1] in snakebody:
					deathscreen()
					Game = False
				else:#Check if snake head is out of bounds
					if playerpositions[len(playerpositions)-1][0] < 0:
						deathscreen()#If it is, end the game
						Game = False
					elif playerpositions[len(playerpositions)-1][0] > width:
						deathscreen()
						Game = False
					elif playerpositions[len(playerpositions)-1][1] < 0:
						deathscreen()
						Game = False
					elif playerpositions[len(playerpositions)-1][1] > height:
						deathscreen()
						Game = False
					else:
						drawgame()

				#print('Test Serial')
				#ser = serial.Serial("/dev/cu.usbserial-FTGNKMFP")  # open serial port
				#print(ser.name)         # check which port was really used
				#ser.write('M1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16')     # write a string
				#ser.close()
					
			while waitforanswer:#This is used so the game doesnt quit immediately as it has something to wait for	
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key==K_p:
							print('RESTARTING')
							MAIN_GAME()


		MAIN_GAME()
