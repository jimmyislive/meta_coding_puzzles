from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  R.reverse()
  
  max = R[0]
  deflate_count = 0
  
  for i in range(1, len(R)):
    if R[i] >= max:
      R[i] = max - 1
      deflate_count += 1
    
    max = R[i] 
    
    if max == 1 and i != (len(R) - 1):
      return -1
    
  return deflate_count

