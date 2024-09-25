# Write any import statements here
import math

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  
  num_uniform_ints = 0
  
  # find the number of digits
  num_of_digits = int(math.log10(A)) + 1
  completeFlag = False
  
  
  # populate the candidate list
  candidate_list = []
  start = int("1"*num_of_digits)
  
  while start < B: 
    for i in range(1,10):
      candidate_list.append(start * i)

    for ele in candidate_list:
      if ele >= A and ele <= B:
        num_uniform_ints += 1

      if ele >= B:
        completeFlag = True
        break

    if completeFlag:
      break
      
    num_of_digits += 1
    candidate_list = []
    start = int("1"*num_of_digits)
    
  return num_uniform_ints


