import sys

words = []

for line in sys.stdin:
       if 'q' == line.rstrip():
              break
       words.append(line)

words = [i.strip() for i in words]
       
#sort begins here
#anyChanges = True
#while anyChanges == True:
#       anyChanges = False
#       forCount = 0
#       for word in range(len(words)-1):
#              word2 = word+1
#              if words[word].lower() > words[word2].lower():
#                     words[word], words[word2] = words[word2], words[word]
#                     anyChanges = True

def split(left, right, words):
       last, first = words[right], left
       for i in range(left, right):
              if words[i] <= first:
                     words[i], words[first] = words[first], words[i]
                     first += 1
              nums[first], nums[right] = nums[right], nums[first]
              return first

def quicksort(left, right, words):
       if len(words) == 1:
              return words
       if left < right:
              mid = split(left, right, words)
              quicksort(left, mid-1, words)
              quicksort(mid+1, right, words)
       return words

words = quicksort(words[0], words[len(words)-1], words)
              
for word in words:
  sys.stdout.write(f"{word}\n")
