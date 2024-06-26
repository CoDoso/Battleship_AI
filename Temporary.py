import random


# Globalisation of important Variables
global Ships_Remaining
global Player_Map
global Ship_Map

# Shoots a target and checks for remaining Ships
def call_shot(x, y):
  if Ship_Map[y][x] != 0:
    Player_Map[y][x] = "X"
    Hit_Ship = Ship_Map[y][x]    # X = Hit | # = Dead Ship | O = Miss | 0 = Empty(No Action yet)
    Ship_Map[y][x] = "X"
  else:
    Player_Map[y][x] = "O"

  Recorded_Ships = []
  for Row in range(10):
    for Square in range(10):
      if Ship_Map[Row][Square] not in Recorded_Ships and Ship_Map[Row][Square] not in ["#", "X", "O", 0]:
        Recorded_Ships.append(Ship_Map[Row][Square])
      if Ship_Map[Row][Square] == 3 and 3 in Recorded_Ships:
        Recorded_Ships.append(3)

  if Hit_Ship not in Recorded_Ships:
     for Row in range(10):
      for Square in range(10):
        if Inital_Ship_Map[Row][Square] == Hit_Ship:
          Ship_Map[y][x] = "#"
          Player_Map[y][x] = "#"
          Ships_Remaining.remove(Hit_Ship)
          
def Calc_Score(Score_Map):
  Highest_Score = 0
  
  for Row in range(10):
    for Square in range(10):
      Score = 0
      for Ship in Ships_Remaining:
        Valid_Placement = True
        for Tile in range(Ship):
            
          
          # East Check
            try:
                if Player_Map[Row][Square+Tile] != 0 or Player_Map[Row][Square+Tile] != "O":
                  Valid_Placement = False
                else:
                    if Player_Map[Row][Square+Tile] == "X":
                        Score += 10
                    else:
                        Score += 1
            except:
                pass

              # North Check
            try:
                if Player_Map[Row+Tile][Square] != 0 or Player_Map[Row][Square+Tile] != "O":  # 0 = Empty | O = Miss
                    Valid_Placement = False
                else:
                    if Player_Map[Row+Tile][Square] == "X":
                      Score += 10
                    else:
                      Score += 1
            except:
                pass
        # West Check
        try:
            if Player_Map[Row][Square-Tile] != 0 or Player_Map[Row][Square+Tile] != "O":
                Valid_Placement = False
            else:
                if Player_Map[Row][Square-Tile] == "X":
                    Score += 10
                else:
                    Score += 1
        except:
                pass

          # South Check
        try:
          if Player_Map[Row-Tile][Square] != 0 or Player_Map[Row][Square+Tile] != "O":
            Valid_Placement = False
          else:
            if Player_Map[Row-Tile][Square] == "X":
              Score += 10
            else:
              Score += 1
        except:
                pass
                  
      Score_Map[Row][Square] = Score
      if Score > Highest_Score:
        Highest_Score = Score
  return [Score_Map, Highest_Score]
  
   # 10x10 Grid creation
 
def create_Grid():   
  Grid = []
  for i in range(10):
    Grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])   
  return Grid

def create_map():
  
  Map = create_Grid()

  for Ship in [5, 4, 3, 3, 2]:  # Classic Ships
    while True:
      Starting_Point = [random.randint(0, 9), random.randint(0, 9)]  # Creates a Random Location on the map  [X|Y]
      Direction = random.randint(0, 3)   # Clockwise Rotation: 0 North, 1 East, 2 South, 3 West

        # Map[] Y Coords | Map[][] X Coords
      if Map[Starting_Point[1]][Starting_Point[0]] == 0 :
        
        # Checks each Square if its empty
        Valid_Placement = True
        for i in range(Ship):
          try:
              if Direction == 0:
                if Map[Starting_Point[1]+i][Starting_Point[0]] != 0:
                  Valid_Placement = False
                  break
                  
              elif Direction == 1:
                if Map[Starting_Point[1]][Starting_Point[0]+i] != 0:
                  Valid_Placement = False
                  break
                  
              elif Direction == 2:
                if Map[Starting_Point[1]-i][Starting_Point[0]] != 0:
                  Valid_Placement = False
                  break
                  
              elif Direction == 3:
                if Map[Starting_Point[1]+i][Starting_Point[0]-1] != 0:
                  Valid_Placement = False
                  break
          except:
              pass
        # If every Square is empty the Ship places itself.
        if Valid_Placement:
          for i in range(Ship):
            try:
                match Direction:
                  case 0:
                    Map[Starting_Point[1]+i][Starting_Point[0]] = Ship
                  case 1:
                    Map[Starting_Point[1]][Starting_Point[0]+i] = Ship
                  case 2:
                    Map[Starting_Point[1]-i][Starting_Point[0]] = Ship
                  case 3:
                    Map[Starting_Point[1]+i][Starting_Point[0]-1] = Ship
            except:
                pass
          break
  return Map

# Map = Grid with Values | Grid = Empty Grid
Player_Map = create_Grid()
Ship_Map = create_map()
Inital_Ship_Map = Ship_Map

# Variable creation
Ships_Remaining = [5, 4, 3, 3, 2]
Round = 0

# Main Ai Loop
while Ships_Remaining != []:
  Round += 1
  Scores = Calc_Score(Player_Map)
  print(Scores[0])  # Map
  print(Scores[1])  # Highest Score
  
  for Row in Player_Map:
    for Square in Player_Map[Row]:
      if Square == Scores[1]:
        call_shot(Square, Row)
