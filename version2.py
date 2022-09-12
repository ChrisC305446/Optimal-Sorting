import sys

words = []

for line in sys.stdin:
       if 'q' == line.rstrip():
              break
       
       words.append(line)

words = [i.strip() for i in words]
       
#sort begins here
anyChanges = True
while anyChanges == True:
       anyChanges = False
       forCount = 0
       for word in range(len(words)-1):
              word2 = word+1
              if words[word] > words[word2]:
                     words[word], words[word2] = words[word2], words[word]
                     anyChanges = True


for word in words:
  sys.stdout.write(f"{word}\n")
       
