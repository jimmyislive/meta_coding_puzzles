from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  
  min_problem_count = 0
  
  evenPresent = False
  oddPresent = False
  
  for i in range(len(S)):
    if S[i] % 2 == 0:
      evenPresent = True
    else:
      oddPresent = True
      
  S.sort()
  
  if S[-1] % 2 == 0:
      min_problem_count = S[-1]/2
      if oddPresent:
        return int(min_problem_count + 1)
      else:
        return int(min_problem_count)
  else:
      min_problem_count = S[-1]//2 + 1
      return int(min_problem_count)
  
