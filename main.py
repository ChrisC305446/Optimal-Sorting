
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
def is_sorted(unfiltered,str_index): # takes in array and tests if 
  if index == 0: # first character
    for index, word in unfiltered:
       if unfiltered.__len__() != index+1: #if not at end of array
        if alpha_to_num[word.lower()[str_index]] > alpha_to_num[unfiltered[index+1].lower()[str_index]]:
          return False # not ordered
  else: # allow characters to be unordered if character before on both characters is different (only return false if unordered and character before is same on both)
    for index, word in unfiltered:
       if unfiltered.__len__() != index+1: #if not at end of array
        if alpha_to_num[word.lower()[str_index]] > alpha_to_num[unfiltered[index+1].lower()[str_index]]:
          #if all prior characters in word the same!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
          return False # not ordered

def sort(unfiltered):
  #sort as .lower()
  
  filtered = unfiltered

  largest_string = 0
  for word in filtered:
    if word.__len__() > largest_string:
      largest_string = word.__len__()
  #find length of largest word
  for index, word in enumerate(filtered):
    filtered[index] = word.ljust(largest_string+2)
  #pad so all words are the same size

  str_index = 0
  for char in range(0,largest_string): #what character is being tested
    while is_sorted(filtered,str_index) == False: # while current character index isnt sorted
      for index, word in enumerate(filtered):# pass through array and swap values
        if filtered.__len__() != index+1: #if not at end of array
        
    
          word = filtered[index] #update reference
          
          #swap values
          if alpha_to_num[word.lower()[str_index]] > alpha_to_num[filtered[index+1].lower()[str_index]]: #if number version of character at string index greater than number version of character at string index one element ahead
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
  sys.stdout.write(f"{word}")#output as stdout 
###########output
