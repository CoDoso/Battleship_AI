import random
import Gen_Map as Generator


global Map
global Ships_Remaining


Player_Map = Generator.create_Grid()
Ship_Map = []
Generator.create_map(Ship_Map)
Ships_Remaining = [5, 4, 3, 3, 2]

def Calc_Score(Score_Map):
  Highest_Score = 0
  
  for Row in range(9):
    for Square in range(10):
      Score = 0
      for Ship in Ships_Remaining:
        Valid_Placement = True
        for Tile in range(Ship):
          if Player_Map[Row][Square+Tile] != 0:
            Valid_Placement = False
          else:
            Score += 1
          if Player_Map[Row+Tile][Square] != 0:
            Valid_Placement = False
          else:
            Score += 1
          if Player_Map[Row][Square-Tile] != 0:
            Valid_Placement = False
          else:
            Score += 1
          if Player_Map[Row-Tile][Square] != 0:
            Valid_Placement = False
          else:
            Score += 1
      Score_Map[Row][Square] = Score
      if Score > Highest_Score:
        Highest_Score = Score
  return [Score_Map, Highest_Score]
