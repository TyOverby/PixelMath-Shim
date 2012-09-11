from jarray import array
import java.awt.Color as Color
import BattleFrame
import SetupFrame

class Game_Master:

   parent_pixie = 1 #Holds the window number of the base pixie image.
   team_arrays = []
   team0 = [] #Holds player 1's pixie instances
   team1 = [] #Holds player 2's pixie instances
   battlepixie0 = [] #Holds player 1's selected pixie
   battlepixie1 = [] #Holds player 2's selected pixie

   def __init__(self):
      self.parent_pixie = pmOpenImage(0, "pixie.png") #Opens up a 'parent' pixie image for PixelMath to reference
      screensize= pmGetScreenSize()
      pmPositionWindow(self.parent_pixie, screensize[0],screensize[1],0,0)

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
      parent_pixie_w = pmGetImageWidth(game_master.get_parent_pixie())
      parent_pixie_h = pmGetImageHeight(game_master.get_parent_pixie())

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

   def get_color(self):
      return self.color

   def get_window(self): 
      return self.window

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
         self.x_home = self.x_pos
         self.y_home = self.y_pos
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
      

game_master = Game_Master()

game_master.setup_pixies(0)
game_master.setup_pixies(1)

game_master.draw_pixies(game_master.team0)
game_master.draw_pixies(game_master.team1)

for round in range(1):
    t0s, t1s = BattleFrame.getResults(True, game_master.team_arrays[0], game_master.team_arrays[1])
    print t0s, t1s
    
    game_master.team0[t0s].select(game_master)
    game_master.team1[t1s].select(game_master)
    game_master.battlepixie0[t0s].tween()
    game_master.battlepixie1[t1s].tween()
