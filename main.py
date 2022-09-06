import sys

words = []
for line in sys.stdin:
  words.append(line.rstrip())
  print(words)
  #make words array from stdin
  
