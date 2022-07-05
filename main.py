'''
Luthira Abeykoon
'''

#import libraries
import pgzrun
import random 

#define title, width and height of display
TITLE = 'S-Shooter'
WIDTH = 800
HEIGHT = 512

#Initialize all actors, all of these objects are able to interact
back_bttn = Actor('back_bttn')
background = Actor('background')
hunting_sign = Actor('sign1')
lake_water_sign = Actor('sign2')
city_sign = Actor('sign3')
well_sign = Actor('sign4')
totem_sign = Actor('sign5')
campfire = Actor('campfire')
sprite = Actor('first_nation')
hunting_bg = Actor('hunting_bg')
hunter = Actor('hunter')
pelt = Actor('pelt')
meat = Actor('meat')
paper_info_hunting = Actor('paperhinfo')
paper_facts_hunting = Actor('paperhfacts')
paper_water_facts = Actor('paper_water_facts')
fwd_button = Actor('fwd_button')
water_mole_bg = Actor('waterbg')
clean_water = Actor('clean_water')
dirty_water = Actor('dirty_water')
totem_pole = Actor('totem_pole')
land_treaties = Actor('land_treaties')
water_bucket = Actor('water_bucket')
water_game_facts = Actor('water_game_facts')
htp = Actor('htp')

#Inilitalized list for the arrows and animals in the hunting game
arrows = []
animals = []
#boolean value to show when a new animal should be made
new_animal = True

#choose a random number between 1 and 3(excluding 3) to choose which animal gets drawn for the hunting game
x = random.randint(1,3)

#If the random number that was generated was 1 the animal that will be drawn is a seal.
if x == 1:
  animals.append(Actor('seal'))
  #Standard x position start
  animals[-1].x = 800
  #Random y value to make game interesting
  animals[-1].y = random.randint(30,495)
else:
  #Else the animal drawn will be a bird
  animals.append(Actor('bird'))
  #standard start x value
  animals[-1].x = 800
  #random start y value
  animals[-1].y = random.randint(30,495)

#positions for all actors
hunting_sign.pos=(50,155)
city_sign.pos = (750,155)
lake_water_sign.pos = (545,350)
well_sign.pos = (345,110)
totem_sign.pos = (400,225)
campfire.pos = (441,210)
sprite.pos = (377,276)
hunter.pos = (25,256)
pelt.pos = (19,160)
meat.pos = (26,160)
paper_info_hunting.pos = (400,258)
paper_facts_hunting.pos = (400,258)
totem_pole.pos = (400,258)
paper_water_facts.pos = (400,258)
land_treaties.pos = (400,258)
water_game_facts.pos = (400,258)
htp.pos = (400,258)
fwd_button.pos = (676,245)
water_bucket.pos = (528,363)
# clean_water.pos = (random.randint(30,780), random.randint(30,490))
#Random x and y positions for the water- whack-a-mole game
dirty_water.pos = (random.randint(30,780), random.randint(30,490))
#initliaze hunting score highscore list
hunting_highscores = []
#Posisitons and dimentions for start button, back button and credits button,
play_button = Rect(200,150, 200, 50)
htp_button = Rect(430,150, 200, 50)
credits = Rect(360,225,100,50)
back_bttn.pos = (20,20)

#All boolean values that will be used in the game, more will be expaled in depth in the following lines.
play_clicked = False
htp_clicked = False
credits_clicked = False
lobby = False
hunting_game = False
arrow_shot = False
new_animal = True
h_game_over = False
water_game = False
paper_load = False
next_page = False
well_clicked = False
h_game_start = False
water_end_screen = False
totem_pole_clicked = False
land_treaties_clicked = False
water_bucket_clicked = False

#Draw Function
def draw():
  #Inilitalized all global variables, most of which are boolean values that will be used to draw actors and screens
  global play_clicked,htp_clicked,credits_clicked,hunting_gdame,lobby,arrows,arrow_shot,h_game_over,hunting_score,paper_load,next_page,well_clicked,h_game_start,water_game,reset_timer, water_score,water_game_time,strikes,water_end_screen, totem_pole_clicked,land_treaties_clicked,water_bucket_clicked
  #Main menu of the game. If play button clicked, how to play clicked and credits clicked is false, this will run.
  if play_clicked == False and htp_clicked == False and credits_clicked == False:
    screen.fill("black")
    screen.draw.filled_rect(play_button, "white")
    screen.draw.textbox("Play", play_button, color=("black"))
    screen.draw.filled_rect(htp_button, "white")
    screen.draw.textbox("How To Play", htp_button, color=("black"))
    screen.draw.filled_rect(credits, "white")
    screen.draw.textbox("Credits", credits, color=("black"))
  #If the play button is clicked
  elif play_clicked == True:
    #fist page is the lobby
    if lobby == True:
      #loads the lobby map, defined in a function
      lobby_map()
      #if the well actor is clicked is true
      if well_clicked == True:
        #Display information/facts about water
        paper_water_facts.draw()
        #backbutton to escape and return to game
        back_bttn.draw()
      #If hunting paper laod is true
      if paper_load == True:
        #draw paper
        paper_info_hunting.draw()
        #draw foward button for next page
        fwd_button.draw()
        #if next page is true
        if next_page == True:
          #draw next page
          paper_facts_hunting.draw()
          #draw backbutton to escpae to lobby and return to game
          back_bttn.draw()
      if totem_pole_clicked == True:
        totem_pole.draw()
        back_bttn.draw()
      if land_treaties_clicked == True:
        land_treaties.draw()
        back_bttn.draw()
      if water_bucket_clicked == True:
        water_game_facts.draw()
        back_bttn.draw()
    #if hunting game is true performs the following lines
    elif hunting_game == True:
      #clears screen
      screen.clear()        
      hunting_bg.draw()
      hunter.draw()
      #Shows text- How to play (space to start)
      screen.draw.text("PRESS [SPACE] TO START",(370, 250), color=(200, 200, 200), background="black")
      #if the hunting game starts 
      if h_game_start == True:
      #the hunting game starts
        screen.clear()
        hunting_bg.draw()
        hunter.draw()
        screen.draw.text("Score: {}".format(hunting_score),(370, 20), color=(200, 200, 200), background="black")
        #if the boolean value arrow_shot is equal to true
      if arrow_shot == True:
        #draws the arrow from the list
        for arrow in arrows:
          arrow.draw()
          #draws the animal from the list
        for animal in animals:
          animal.draw()
    #If the hunting game ends, the following is executed, essentially the endscreen
    elif h_game_over == True:
      #end screen
      screen.clear() 
      screen.fill('black')
      screen.draw.text("GAME OVER!",(300, 195), color=(200, 200, 200), background="black")
      screen.draw.text("Score: {}".format(hunting_score),(350, 213), color=(200, 200, 200), background="black")
      h_score()
      #If there are no elements in the hunting highscores list (the game has never been played before)
      if len(hunting_highscores) == 0:
        screen.draw.text("Highscore: 0",(325, 235), color=(200, 200, 200), background="black")
      else:
        #Displays the currect highscore of the game
        screen.draw.text("Highscore: {}".format(h_score_highscore(hunting_highscores)),(325, 235), color=(200, 200, 200), background="black")

    #If the water game is true/ when the player clicks on the sign next to the lake
    if water_game == True:
      #The reset timer, used to move the bucket after every three seconds counts (60/second) so 3 seconds = 180
      reset_timer = reset_timer + 1
      #The water game is 30 seconds long, so it will count down from 1800
      water_game_time -=1
      #Draw the background
      water_mole_bg.draw()
      #Write all information (scores, strikes, time left)
      screen.draw.text("Score: {}".format(water_score),(725, 10), color=(200, 200, 200), background="black")
      screen.draw.text("Strike in: {}".format(reset_timer),(700, 30), color=(200, 200, 200), background="black")
      screen.draw.text("Time Remaining: {}".format(water_game_time),(618, 50), color=(200, 200, 200), background="black")
      screen.draw.text("Strikes: {}".format(strikes),(725, 70), color=(200, 200, 200), background="black")
      dirty_water.draw()
      #executes if end screen is true
      if water_end_screen == True:
        screen.clear()
        screen.fill('grey')
        screen.draw.text("GAME OVER!",(325, 195), color=(200, 200, 200), background="black")
        screen.draw.text("Score: {}".format(water_score),(350, 213), color=(200, 200, 200), background="black")
        back_bttn.draw()
        #If there are no elements in the water highscores list, it will return a value of 0
        if len(water_highscores) == 0:
          screen.draw.text("Highscore: 0",(325, 235), color=(200, 200, 200), background="black")
        else:
          #Else, it will display the highest recorded score after the run
          screen.draw.text("Highscore: {}".format(w_score_highscore(water_highscores)),(325, 235), color=(200, 200, 200), background="black")

  #If how to play is clicked
  elif htp_clicked == True:
    screen.clear()
    screen.fill("white")
    htp.draw()
    back_bttn.draw()
    #If credits is clicked
  elif credits_clicked == True:
    screen.clear()
    screen.fill("dim grey")
    back_bttn.draw()

#2 axis movement x and y for general lobby 
def movement_2axis():
  #for debugging purposes : Original value is 1.5
    if keyboard[keys.A]:
      sprite.x -=3
    elif keyboard[keys.D]:
      sprite.x+=3
    elif keyboard[keys.W]:
      sprite.y-=3
    elif keyboard[keys.S]:
      sprite.y+=3
#this built in python function makes it so that the space key for the hunting game is only registered for each time the space key is pressed and not for the time it is held for.
def on_key_down(key):
  global arrows,arrow_shot,h_game_start
  if key == keys.SPACE:
    #hunting game set to true
    h_game_start = True
    #arrow shot set to true
    arrow_shot = True
    #append teh arrow actor to the list of arrows, previously initialized
    arrows.append(Actor('arrow'))
    #draw arrow at proper x and y positions, respectively
    arrows[-1].x = hunter.x + 37
    arrows[-1].y = hunter.y - 1 
#Hunting score initliazed to 0
hunting_score = 0
#speed of animals set to 3 to start
speed = 3

#The following functions were to move the waterbucket in the water game, could possibly be implemeneted in future iterations
# choose_direction_f = True
# def choose_direction():
#   if choose_direction_f == True:
#     direction = random.randint(0,4)
#     print(direction)
#     return direction

# def direction():
#   global choose_direction_f
#   if direction == 0:
#     dirty_water.x +=1
#     choose_direction_f = False
#   elif direction == 1:
#     dirty_water.x-=1
#     choose_direction_f = False
#   elif direction == 2:
#     dirty_water.y+=1
#     choose_direction_f = False
#   elif direction == 3: 
#     dirty_water.y-=1
#     choose_direction_f = False

#Time given to play a round of teh water game. Since teh screen refreshes 60 times every second, 30 seconds is 1800 frames
water_game_time = 1800

#Update function
def update():
  #state all global variables
  global arrows,hunting_score,speed,hunting_game,h_game_over,reset_timer,strikes, water_end_screen,choose_direction_f,water_game_time,hunting_highscores
  #if play is clicked
  if play_clicked == True:
    #if lobby is true
    if lobby == True:
      #2 axis movement gets called
      movement_2axis()    
      #borders of the game, to make sure sprite does not exit the screen
      if 15 > sprite.x:
        sprite.x = 15
      elif 785 < sprite.x:
        sprite.x = 785
      if 115 > sprite.y:
        sprite.y = 115
      elif 450 < sprite.y:
        sprite.y = 440
        #if end screen is false and teh hunting game is true
    elif hunting_game == True and h_game_over == False:
      #moevemt along teh y axis
      if keyboard[keys.W]:
        hunter.y-=3
      elif keyboard[keys.S]:
        hunter.y+=3 
      
      #if teh arrow passes the screen, it will be removed from the list of arrows
      for arrow in arrows:
        if arrow.x > 800:
          arrows.remove(arrow)
        else:
          arrow.x += 10
      #for each animal drawn it will move towards the hunter at the variable speed along teh x axis
      for animal in animals:
          animal.x-=speed
          #if the animal reaches the end of the screen, end screen will be true
          if animal.x < 15:
            h_game_over = True
            hunting_highscores.append(h_score)
            hunting_game = False

      #if an arrow collides with an animal it will get removed from the list    
      for arrow in arrows:
        if arrow.colliderect(animal):
          arrows.remove(arrow)
          #a point to teh score will be added
          hunting_score+=1
          #speed of the animal will increase by 0.3
          speed+=0.3
          #animal will be generated at standard x position but random y position
          animal.pos = (810,random.randint(30,495))
      #sets borders for teh hunter (sprite) so it does not move off screen
      if 20 > hunter.y:
        hunter.y = 20
      elif 500 < hunter.y:
        hunter.y = 499
    
    #if water game is true
    if water_game == True:
      #resets teh timer after 240 frames (3 secs)
      if reset_timer == 240:
        #switches the position of the water
        dirty_water.pos = (random.randint(30,780), random.randint(30,490))
        #awards teh player with a strike
        strikes +=1
        #resets the reset timer
        reset_timer = 0
        #if teh player accululates 4 strikes the game will end
      if strikes == 4:
        #end screen is true
        water_end_screen = True
        strikes = 0
        #if teh timer runs out the game will be over 
      if water_game_time == 0:
        water_end_screen = True
  else:
    pass

#map for the lobby to load
def lobby_map():
  screen.clear()
  background.draw()
  well_sign.draw()
  hunting_sign.draw()
  lake_water_sign.draw()
  city_sign.draw()
  totem_sign.draw()
  campfire.draw()
  sprite.draw()
  pelt.draw()
  meat.draw()
  water_bucket.draw()


def water_game():
  screen.clear()

#initlaize water game score, reset timer for water game and strikes for water game
water_score = 0
reset_timer = 0
strikes = 0

#on mouse down function
def on_mouse_down(pos):
  #debugging purposes
  print(pos)
  #state all global variables
  global play_clicked,htp_clicked,credits_clicked,lobby,hunting_game,h_game_over, water_game,paper_load,next_page,well_clicked,water_score,reset_timer, choose_direction_f,strikes,totem_pole_clicked,land_treaties_clicked,water_bucket_clicked,water_end_screen
  #collition with play button
  if play_button.collidepoint(pos):
    play_clicked = True
    if hunting_game == True:
      lobby = False
    else:
      lobby = True
  
  #collisiton with how to play button
  elif htp_button.collidepoint(pos):
    htp_clicked = True
  #collition with how to play button
  elif credits.collidepoint(pos):
    credits_clicked = True
  #collisiton with back button 
  if back_bttn.collidepoint(pos):
    credits_clicked = False
    htp_clicked = False
    totem_pole_clicked = False
    land_treaties_clicked = False
    water_bucket_clicked = False
  #hunting_sign
  if 15 <= sprite.x <=85 and 120<=sprite.y <=168:
    if hunting_sign.collidepoint(pos):
      hunting_game = True
      h_game_over = False
      lobby = False
      print('True')
  #make sure sprite is in range to be able to click on signs and actors in the game in this case the pelt and meat 
  if 15 <= sprite.x <=85 and 120<=sprite.y <=168:
    if pelt.collidepoint(pos) or meat.collidepoint(pos):
      paper_load = True
      back_bttn.pos = (20,20)
    #load paper with info and facts
    if paper_load == True:
      if back_bttn.collidepoint(pos):
        paper_facts_hunting.pos = (900,1000)
        paper_info_hunting.pos = (900,1000)
        back_bttn.pos = (900,1000)
      #draw fowards button
      if fwd_button.collidepoint(pos):
        fwd_button.pos = (900,1000)
        next_page = True
  #make sure sprite is in range to be able to click on signs and actors 
  if 495<=sprite.x<=568 and 323<=sprite.y<=377:
    if lake_water_sign.collidepoint(pos):
      water_game = True
      water_end_screen = False
      lobby = False
#if water game is true
  if water_game == True:
    #collides with position
    if dirty_water.collidepoint(pos):
      #resets timer to 0
      reset_timer = 0
      #adds score
      water_score +=1
      # choose_direction_f = True
      dirty_water.pos = (random.randint(30,780), random.randint(30,490))
    else: 
      #if teh player does not click on teh water, awarded with a strike
      strikes +=1
      #if end screen is true
    if water_end_screen == True:
      if back_bttn.collidepoint(pos):
        lobby = True
        if lobby == True:
          water_game = False

    # if lobby == True:
    #   water_end_screen = False
  if 199 <= sprite.y<= 250 and 366<= sprite.x<= 417:
    if totem_sign.collidepoint(pos):
      totem_pole_clicked = True
  if 123<= sprite.y <=173 and 698 <= sprite.x <=772:
    if city_sign.collidepoint(pos):
      land_treaties_clicked = True
  if 332<= sprite.y <=380 and 500 <= sprite.x <=550:
    if water_bucket.collidepoint(pos):
      water_bucket_clicked = True
  #make sure sprite is in range to be able to click on signs and actors 
  if 303 <= sprite.x <= 400 and 100 <= sprite.y <=370:
    if well_sign.collidepoint(pos):
      back_bttn.pos = (20,20)
      well_clicked = True
    #if well is clicked, draw back button to escape
    if well_clicked == True:
      if back_bttn.collidepoint(pos):
        paper_water_facts.pos = (900,1000)
        back_bttn.pos = (900,1000)
        
#top score for future iteration
top_scores = {}
#display highscore function for hunting game
def h_score_highscore(hunting_highscores):
  hunting_highscores.sort(reverse=True)
  hunting_highscore = hunting_highscores[0]
  return hunting_highscore
#initialize list for water game
water_highscores = []
#display highscore function for water game
def w_score_highscore(water_highscores):
  water_highscores.sort(reverse=True) 
  water_highscore = water_highscores[0]
  return water_highscore

#hunting score sheet 
def h_score():
  global hunting_score,lobby,h_game_over
  hunting_score = str(hunting_score)
  name_false = True name_false == True:
    try:
      name = input(('Please enter the name you wish to be displayed on the leaderboard: '))
      name_false = False
    except:
      name = input(('Please enter the name you wish to be displayed on the leaderboard: '))
    with open('top_scores.txt', 'w') as f:
      f.write(name)
      f.write('')
      f.write(hunting_score)
      f.write('\n')
      lobby = True
      h_game_over = False

# def leaderboard():
#   global top_scores
#   with open('top_scores.txt','r') as f:
#     for line in f:
#       (key, val) = line.split()

pgzrun.go()