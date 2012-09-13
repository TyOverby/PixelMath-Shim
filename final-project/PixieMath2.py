from jarray import array
import java.awt.Color as Color
import math
import BattleFrame
import SetupFrame
import Logic
import time
class Game_Master:

   parent_pixie = 1 #Holds the window number of the base pixie image.
   team_arrays = []
   team0 = [] #Holds player 1's pixie instances
   team1 = [] #Holds player 2's pixie instances
   battlepixie0 = [] #Holds player 1's selected pixie
   battlepixie1 = [] #Holds player 2's selected pixie
   health0 = 100 #Health values for each player
   health1 = 100
   health_drawn = False #Have the health windows already been drawn?
   health_w0 = 0 #Window numbers for health
   health_w1 = 0
   title_w = 0

   def __init__(self):
      pmCalculatorSetVisible(False)
      pmHideProgress()
      self.parent_pixie = pmOpenImage(0, "pixie.png") #Opens up a 'parent' pixie image for PixelMath to reference
      screensize= pmGetScreenSize()
      pmSetVisible(self.parent_pixie, False)
      self.title_w = pmOpenImage(0, "title.png")
      pmPositionWindow(self.title_w, screensize[0]/2 - 200,(-20),0,0)
      self.draw_health()

   def get_parent_pixie(self):
      return int(self.parent_pixie)


   def setup_pixies(self, player): #Takes an array of colors from the SteupFrame and creates pixie objects for each team.
      team_array = SetupFrame.getTeamColors(player)
      self.team_arrays.append(team_array)
      for index, i in enumerate(team_array):
         red = int(i.getRed())
         green = int(i.getGreen())
         blue = int(i.getBlue())
         color = (red, green, blue)

         pixie = Pixie(self,color, player, (index+1))

         if player == 0:
            self.team0.append(pixie)

         elif player == 1:
            self.team1.append(pixie)

   def draw_pixies(self, team):
      for i in team:
         i.draw()
         i.tween()

   def get_team(self, team):
      if team == 0:
         return self.team0
      elif team == 1:
         return self.team1
      else:
         return self.team0
         print "ERROR INVALID TEAM NUMBER"

   def draw_health(self):
      pmClose(self.health_w0)
      pmClose(self.health_w1)
      self.health_drawn = True

      screensize = pmGetScreenSize()
      self.health_w0 = pmNewComputedImage("Player 1", 300, 40, "if x < "+str(self.health0*3)+" then RGB(255,0,0) else 255")
      self.health_w1 = pmNewComputedImage("Player 2", 300, 40, "if x < (300-"+str(self.health1*3)+") then 255 else RGB(255,0,0)")
      pmPositionWindow(self.health_w0,(screensize[0]/2 - 370),screensize[1]-250,0,0)
      pmPositionWindow(self.health_w1,(screensize[0]/2+50),screensize[1]-250,0,0)

   def apply_damage(self, player, amount):
      if player == 0:
         self.health0 = amount
         return  self.health0

      elif player == 1:
         self.health1 = amount
         return  self.health1

   def animate_combat(self, attacker): #Pass the player number (0 or 1) of the attacking player
      if attacker == 0:
         atk_pixie = self.battlepixie0[0]
         atk_movement = (5, 30)
         def_pixie = self.battlepixie1[0]
         def_movement = (15, 3)

      elif attacker == 1:
         atk_pixie = self.battlepixie1[0]
         atk_movement = ((-5), 30)
         def_pixie = self.battlepixie0[0]
         def_movement = ((-15), 3)


      pmSetSource1(def_pixie.get_window()) #Creates the 'hit' pixie
      hit_pixie = pmNewComputedImage("XXXXXXX", pmGetImageWidth(self.parent_pixie),pmGetImageHeight(self.parent_pixie),"s1(x, abs(y+8*sin(x/3+1)) mod 100)")
      pmSetVisible(hit_pixie, False)

      a_pixie_pos = atk_pixie.get_pos() #This block animates the attacker's 'hop'.
      atk_pixie.set_target(a_pixie_pos[0]+atk_movement[0], a_pixie_pos[1]+atk_movement[1])
      atk_pixie.tween()
      atk_pixie.set_target(a_pixie_pos[0], a_pixie_pos[1])
      atk_pixie.tween()


      d_pixie_pos = def_pixie.get_pos() #This block animates the defender's hit animation.
      def_pixie.set_target(d_pixie_pos[0]+def_movement[0], d_pixie_pos[1]+def_movement[1])
      def_pixie.tween()
      def_pixie.set_target(d_pixie_pos[0], d_pixie_pos[1])#Reset target to home before overwriting position
      pmPositionWindow(hit_pixie, d_pixie_pos[0], d_pixie_pos[1], 0, 0) #
      pmSetVisible(hit_pixie, True)
      pmSetVisible(def_pixie.get_window(), False)
      time.sleep(1.5)
      pmSetVisible(hit_pixie, False)
      pmClose(hit_pixie)
      pmSetVisible(def_pixie.get_window(), True)

      def_pixie.tween() #Returns Defender to Battle Position
      pmSetSource1(self.parent_pixie) #Resets source image to Parent Pixie


   def return_pixies(self):

      for p in self.battlepixie0:
         home_x = (p.get_home()[0])
         home_y = (p.get_home()[1])
         p.set_target(home_x,home_y)
         self.battlepixie0.remove(p)
         p.tween()
      for p in self.battlepixie1:
         home_x = (p.get_home()[0])
         home_y = (p.get_home()[1])
         p.set_target(home_x,home_y)
         self.battlepixie1.remove(p)
         p.tween()

      print self.battlepixie0, self.battlepixie1


class Pixie:

   color = (0,0,0)
   team = 0 #Team 0 = Player 1, Team 1 = Player 2
   pixienum = 0 #The pixie's position (1-6)in the team
   window = 0 #The PixelMath window number of the pixie.
   x_pos = 0 #Screen position coordinates of this pixie
   y_pos = 0
   x_target = 0
   y_target = 0
   x_home = 0
   y_home = 0

   speed = 5
   parent_pixie_w = 128
   parent_pixie_h = 100
   drawn = False #Has this pixie been drawn before?
   windowsize = (0,0)




   def __init__(self, game_master, color, team, pixienum):
      self.color = color
      self.team = team
      self.pixienum = pixienum
      self.window = 0
      screensize = pmGetScreenSize()
      self.windowsize = pmGetWindowSize(game_master.get_parent_pixie())
      self.parent_pixie_w = pmGetImageWidth(game_master.get_parent_pixie())
      self.parent_pixie_h = pmGetImageHeight(game_master.get_parent_pixie())

      if team == 0: #Sets up screen positions of each pixie so they appear in appropriate screen locations.

         if pixienum % 2 == 0:
            self.x_pos = 0+self.windowsize[0]
         else:
            self.x_pos = 0

      if team == 1:

         if pixienum % 2 == 0:
            self.x_pos = (screensize[0]- self.windowsize[0])
         else:
            self.x_pos = (screensize[0] - 2*self.windowsize[0])

      if team == 0:

         if pixienum <= 2:
            self.y_pos = (0)
         elif pixienum <= 4:
            self.y_pos = (1*self.windowsize[1])
         else:
            self.y_pos = (2*self.windowsize[1])

      if team == 1:

         if pixienum <= 2:
            self.y_pos = (0)
         elif pixienum <= 4:
            self.y_pos = (1*self.windowsize[1])
         else:
            self.y_pos = (2*self.windowsize[1])

      self.x_target = self.x_pos
      self.y_target = self.y_pos
      self.x_home = self.x_pos
      self.y_home = self.y_pos

   def get_color(self):
      return self.color

   def get_window(self):
      return self.window

   def get_pos(self):
      return (self.x_pos, self.y_pos)

   def get_home(self):
      return (self.x_home, self.y_home)

   def set_target(self, x, y):
      self.x_target = x
      self.y_target = y

   def position(self): #Update the position of the Pixie's window.
      pmPositionWindow(self.window, self.x_target, self.y_target, 0, 0)
      print self.pixienum, self.x_pos, self.y_pos

   def draw(self): #Tells pixel math to render the pixie's image.
      if self.drawn == True:
         pmClose(self.window)
      pixiename = "Pixie " + str(self.pixienum)
      formula = ("if s1(x,y) = 128 then RGB("+str(self.color[0])+","+str(self.color[1])+","+str(self.color[2])+") else s1(x,y)")
      self.window = pmNewComputedImage(pixiename, self.parent_pixie_w, self.parent_pixie_h, formula)
      if not self.drawn:
         self.drawn = True

   def select(self, gamemaster): #Select this pixie for battle
      if self.team == 0:
         gamemaster.battlepixie0.append(self)
         #self.x_home = self.x_pos
         #self.y_home = self.y_pos
         self.x_target = pmGetScreenSize()[0]/2  - (self.windowsize[0])
         self.y_target = pmGetScreenSize()[1]/2 - self.windowsize[1]

      if self.team == 1:
         gamemaster.battlepixie1.append(self)
         self.x_home = self.x_pos
         self.y_home = self.y_pos
         self.x_target = (pmGetScreenSize()[0]/2)
         self.y_target = (pmGetScreenSize()[1]/2) - self.windowsize[1]

   def tween(self): #Tweens to current x and y pos.
      x_dist = self.x_target - self.x_pos
      y_dist = self.y_target - self.y_pos
      x_reached = False
      y_reached = False

      while not x_reached or not y_reached:

         if not x_reached:
            x_dist = self.x_target - self.x_pos
            if x_dist == 0:
               x_reached = True
            elif abs(x_dist)< self.speed:
               self.x_pos = self.x_target
               x_reached = True

            if x_dist > 0:
               self.x_pos += self.speed
            elif x_dist < 0:
               self.x_pos -= self.speed

         if not y_reached:
            y_dist = self.y_target - self.y_pos
            if y_dist == 0:
               y_reached = True
            elif abs(y_dist)< self.speed:
               self.y_pos = self.y_target
               y_reached = True

            if y_dist > 0:
               self.y_pos += self.speed
            elif y_dist < 0:
               self.y_pos -= self.speed

         pmPositionWindow(self.window, self.x_pos, self.y_pos, 0, 0)


game_master = Game_Master() #Setup
game_master.draw_health()

game_master.setup_pixies(0)
game_master.setup_pixies(1)

game_master.draw_pixies(game_master.team0) #Pixies to middle
game_master.draw_pixies(game_master.team1)

pts0 = 100
pts1 = 100

for round in range(6*2):
    t0s, t1s = BattleFrame.getResults(round%2==0, game_master.team_arrays[0], game_master.team_arrays[1])

    game_master.team0[t0s].select(game_master)
    game_master.team1[t1s].select(game_master)

    game_master.battlepixie0[0].tween()
    game_master.battlepixie1[0].tween()

    game_master.animate_combat(abs(round%2-1))

    color0 = game_master.battlepixie0[0].get_color()
    color1 = game_master.battlepixie1[0].get_color()
    if(round%2==0):
        pts0 -= math.floor(Logic.getPoints(color0,color1)*50)
    else:
        pts1 -= math.floor(Logic.getPoints(color1,color0)*50)

    if pts0<=0 or pts1<=0:
        break

    game_master.apply_damage(1,pts1)
    game_master.apply_damage(0,pts0)
    game_master.draw_health()
    game_master.return_pixies()

    print "===Points==="
    print "Team 0 points: ", int(pts0)
    print "Team 1 points: ", int(pts1)
    print ""
