from typing import List
# Write any import statements here
from collections import deque

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  
  count_dishes_eaten = 0
  
  eaten_q = deque([])
  cache = set()
  
  for i in range(N):
    
    if D[i] not in cache:
      count_dishes_eaten += 1
      eaten_q.append(D[i])
      cache.add(D[i])
      
      if len(eaten_q) > K:
        popped_item = eaten_q.popleft()
        cache.remove(popped_item)
            
  return count_dishes_eaten

