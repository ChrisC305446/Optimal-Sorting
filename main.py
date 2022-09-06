def sort(unfiltered):
  filtered = unfiltered
  
  return filtered

#########sort function

import sys

words = []
try:
  for line in sys.stdin:
    words.append(line.rstrip())
    print(words)
    #make words array from stdin
except:
  raise Exception(f"invalid input from stdin: {sys.stdin}")
  #error catch
###########turn stdin into array of strings


output = sort(words)
print(f"sorted array = {output}")
###########output
