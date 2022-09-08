import enum


alpha_to_num = {
  " ":-1,
  "a":0,
  "b":1,
  "c":2,
  "d":3,
  "e":4,
  "f":5,
  "g":6,
  "h":7,
  "i":8,
  "j":9,
  "k":10,
  "l":11,
  "m":12,
  "n":13,
  "o":14,
  "p":15,
  "q":16,
  "r":17,
  "s":18,
  "t":19,
  "u":20,
  "v":21,
  "w":22,
  "x":23,
  "y":24,
  "z":25
}
def isSorted(unfiltered):
  pass

def sort(unfiltered):
  #sort as .lower()
  
  filtered = unfiltered

  str_index = 0
  #while isSorted() == False:
  
  for index, word in enumerate(filtered):
    if filtered.__len__() != index+1: #if not at end of array
      
      #make strings same length with spaces
      if filtered[index].__len__() > filtered[index+1].__len__(): #pad word ahead
        filtered[index+1].rjust(filtered[index].__len__())
      if filtered[index].__len__() < filtered[index+1].__len__(): #pad current word
        filtered[index].rjust(filtered[index+1].__len__())
      if alpha_to_num[word[str_index]] > alpha_to_num[filtered[index+1][str_index]]: #if number version of character at string index greater than number version of character at string index one element ahead
        temp =filtered[index]
        filtered[index] = filtered[index+1]
        filtered[index+1] = temp
      
        
  str_index += 1 #what character in string is being tested
  
  
  return filtered

#########sort function





import sys

words = []
try:
  for line in sys.stdin:#make words array from stdin
    
    if line.rstrip() == "!end":
      break # for ending stdin on vscode
    
    words.append(line.rstrip())
   
   
    
except:
  raise Exception(f"invalid input from stdin: {sys.stdin}")
  #error catch

###########turn stdin into array of strings






output = sort(words)

for word in output:
  sys.stdout.write(f"{word}\n")#output as stdout 
###########output
