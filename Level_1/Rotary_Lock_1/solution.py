from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  
  if C[0] != 1:
    C.insert(0, 1)
    M += 1
  
  min_num_seconds = 0
  
  for i in range(1, M):
    start = i - 1
    
    if C[start] == C[i]:
      continue
      
    if C[start] < C[i]:
      cloclwise_secs = abs(C[start] - C[i])
      anticlockwise_secs = abs(C[start] - 1) + abs(N + 1 - C[i])
    else:
      cloclwise_secs = abs(N + 1 - C[start]) + (C[i] - 1)
      anticlockwise_secs = abs(C[start] - C[i])
      
    min_num_seconds += min(cloclwise_secs, anticlockwise_secs)

    
  return min_num_seconds

