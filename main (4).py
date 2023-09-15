#Define the base class playerclass player:
class player:
 def player(self):
  print("the player is playing cricket")
#Define the derived class Batsman
class Batsman(player):
 def play(self):
  print("The Batsman is batting:")
#define the derived class Bowlers
class Bowler(player):
 def play(self):
  print("The bowler is bowling:")
#create objects of Batsman and bowlers classes
  batsman=Batsman()
  bowler=Bowler()
#call the play() method for each object
  batsman.play()
  bowler.play()
