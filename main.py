def sort(unfiltered):
  filtered = unfiltered
  
  return filtered

#########sort function

import sys

words = []
try:
  for line in sys.stdin:
    if line.rstrip() == "!end":
      break # for ending stdin on vscode
    words.append(line.rstrip())
    print(words)
    #make words array from stdin
except:
  raise Exception(f"invalid input from stdin: {sys.stdin}")
  #error catch
###########turn stdin into array of strings


output = sort(words)

for word in output:
  sys.stdout.write(f"{word}\n")
###########output
