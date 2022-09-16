import sys

words = []

for line in sys.stdin:
       words.append(line)

words = [i.strip() for i in words]
       
#sort begins here
anyChanges = True
while anyChanges == True:
       anyChanges = False
       for word in range(len(words)-1):
              word2 = word+1
              if words[word].lower() > words[word2].lower():
                     words[word], words[word2] = words[word2], words[word]
                     anyChanges = True


for word in words:
  out = []     
  out.append(f"{word}/n")
  sys.stdout.write(out)
