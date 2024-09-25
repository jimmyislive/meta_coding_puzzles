# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  opp = {
    'A': 'B',
    'B': 'A'
  }
  
  final = ""
  
  for i in range(N):
    final += opp[C[i]]
    
  return final

