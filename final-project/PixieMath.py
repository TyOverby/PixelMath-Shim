from jarray import array
import java.awt.Color as Color

class game_master:

   parent_pixie = 0 #Holds the window number of the base pixie image.
   team1 = []
   team2 = []

   def __init__():
      pmOpenImage(1, "pixie.png") #Opens up base pixie image and moves off of screen.
      self.parent_pixie = 1
      screensize= pmGetScreenSize()
      pmPositionWindow(parent_pixie, screensize[0],screensize[1],0,0)

   def get_parent_pixie(self):
      return int(self.parent_pixie)


   def setup_pixies(self, player, color): #Takes an array of colors and a player number,  
      screensize= pmGetScreenSize()#Then creates new pixies.
      
      if player == 1:

               

   def create_pixie(self, player, pixienum, color):
      pixiename = "Pixie " + str(pixienum)
      window = windownum
      formula = ("if s1(x,y) = 1 then (s1(x,y)*"+str(color)+") else s1(x,y)")
      pmNewComputedImage(window, pixiename,  pmGetImageWidth(self.parent_pixie), pmGetImageHeight(parent_pixie), formula)     

class pixie:

   color = (0,0,0)
   team = 0 #Team 0 = Player 1, Team 1 = Player 2
   pixie_num = 0
   window = 0
   x_pos = 0
   y_pos = 0

   parent_pixie_w = pmGetImageWidth(game_master.get_parent_pixie())
   parent_pixie_h = pmGetImageHeight(game_master.get_parent_pixie())


   def __init__(color, team, pixienum, window):
      self.color = color
      self.team = team
      self.pixie_num = pixie_num
      self.window = window
      screensize = pmGetScreenSize()
      

      if team == 0:
         self.window = 1 + int(pixie_num) #Plus one because window 1 is the parent pixie.

         if pixienum < 3:
            self.x_pos = (screensize[0]/2 + (2*self.parent_pixie_w)
         else:
            self.x_pos = (screensize[0]/2 + (1*self.parent_pixie_w)

      if team == 1:
         self.window = 1 + int(pixie_num) + 6

         if pixienum < 3:
            self.x_pos = (screensize[0]/2 - (2*self.parent_pixie_w)
         else:
            self.x_pos = (screensize[0]/2 - (1*self.parent_pixie_w)

      if team == 0:

         if pixienum =< 2:
            self.y_pos = (screensize[1] - (2*self.parent_pixie_h)
         elif pixienum =< 4:
            self.y_pos = (screensize[1] - (1*self.parent_pixie_h)
         else:
            self.y_pos = (screensize[1] - (0*self.parent_pixie_h)

      if team == 1:

         if pixienum =< 2:
            self.y_pos = (screensize[1] - (2*self.parent_pixie_h)
         elif pixienum =< 4:
            self.y_pos = (screensize[1] - (1*self.parent_pixie_h)
         else:
            self.y_pos = (screensize[1] - (0*self.parent_pixie_h)


   def position():
      pmPositionWindow(self.window, self.x_pos, self.y_pos, 0, 0) 

   def draw():
      pixiename = "Pixie " + str(self.pixie_num)
      formula = ("if s1(x,y) = 1 then (s1(x,y)*"+str(color)+") else s1(x,y)")
      pmNewComputedImage(self.window, pixiename, self.parent_pixie_w, self.parent_pixie_h, formula)