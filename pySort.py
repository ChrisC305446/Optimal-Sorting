import sys

words = []

for line in sys.stdin:
       if 'q' == line.rstrip():
              break
       
       words.append(line)
       
words.sort()
print(words)
       
