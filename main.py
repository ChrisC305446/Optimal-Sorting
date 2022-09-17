import sys

words = []

for line in sys.stdin:
       if 'q' == line.rstrip():
              break
       words.append(line)

words = [i.strip() for i in words]
       
def partition(l, r, nums):
       pivot, ptr = words[r], l
       for i in range(l, r):
              if words[i] <= pivot:
                     words[i], words[ptr] = words[ptr], words[i]
                     ptr += 1
       nums[ptr], nums[r] = nums[r], nums[ptr]
       return ptr

def quicksort(l, r, words):
       if len(words) == 1:
              return words
       if l < r:
              pi = partition(l, r, words)
              quicksort(l, pi-1, words)
              quicksort(pi+1, r, words)
       return words

words = quicksort(0, len(words)-1, words)

for word in words:
       sys.stdout.write(f"{word}\n")
