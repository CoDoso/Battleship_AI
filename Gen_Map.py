import random


def create_map(Map):
  
  for i in range(9):
    Map.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # 10x10 Grid creation

  for Ship in [5, 4, 3, 3, 2]:  # Classic Ships
    while True:
      Starting_Point = [random.randint(0, 9), random.randint(0, 9)]  # Creates a Random Location on the map  [X|Y]
      Direction = random.randint(0, 3)   # Clockwise Rotation: 0 North, 1 East, 2 South, 3 West

        # Map[] Y Coords | Map[][] X Coords
      if Map[Starting_Point[1]][Starting_Point[0]] == 0 :
        
        # Checks each Square if its empty
        Valid_Placement = True
        for i in range(Ship):
          
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

        # If every Square is empty the Ship places itself.
        if Valid_Placement:
          for i in range(Ship):
            match Direction:
              case 0:
                Map[Starting_Point[1]+i][Starting_Point[0]] = Ship
              case 1:
                Map[Starting_Point[1]][Starting_Point[0]+i] = Ship
              case 2:
                Map[Starting_Point[1]-i][Starting_Point[0]] = Ship
              case 3:
                Map[Starting_Point[1]+i][Starting_Point[0]-1] = Ship
          break
  return Map
