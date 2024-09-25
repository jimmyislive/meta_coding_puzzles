from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  total = R*C
  if total <= 0:
    return 0
  
  battleship_count = 0
  
  for i in range(R):
    for j in range(C):
      if G[i][j] == 1:
        battleship_count += 1
        
  return battleship_count/total

