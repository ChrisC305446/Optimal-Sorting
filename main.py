alpha_to_num = {
  " ":-1,
  "a":0,
  "á":0,
  "å":0,
  "b":1,
  "c":2,
  "d":3,
  "e":4,
  "è":4,
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
  "ô":14,
  "p":15,
  "q":16,
  "r":17,
  "s":18,
  "t":19,
  "u":20,
  "ü":20,
  "û":20,
  "v":21,
  "w":22,
  "x":23,
  "y":24,
  "z":25,
  "é":4
}

def sort(unfiltered):
  #sort as .lower()
  
  filtered = unfiltered

  largest_string = 0
  for word in filtered:
    if word.__len__() > largest_string:
      largest_string = word.__len__()
  #find length of largest word
  for index, word in enumerate(filtered):
    filtered[index] = " " + word.ljust(largest_string+2)
  #pad so all words are the same size

  
  for str_index in range(0,largest_string): #what character is being tested
    while True: # while current character index isnt sorted
        changed = False
        for index, word in enumerate(filtered):
          index_mod = 1#for ignoring apostrophes
          next_index_mod = 1
          negative_index_mod = 0# to account for apostrophe based index errors
          negative_next_index_mod = 0
          if filtered.__len__() != index+1: #if not at end of array
            

            if word.lower()[str_index+index_mod] == "'":
              index_mod += 1
            if filtered[index+1].lower()[str_index+next_index_mod] == "'":
              next_index_mod += 1
           
              #print(f"alpha_to_num[{word}.lower()[{str_index}+{index_mod}]] == {alpha_to_num[word.lower()[str_index+index_mod]]}, alpha_to_num[{filtered[index+1]}.lower()[{str_index}+{next_index_mod}]] == alpha_to_num[filtered[index+1].lower()[str_index+next_index_mod]]")  
            if alpha_to_num[word.lower()[str_index+index_mod]] > alpha_to_num[filtered[index+1].lower()[str_index+next_index_mod]]:
              if str_index != 0:   
            
                for num in range(str_index-1+index_mod,-1,-1): # iterate up string
                  if word.lower()[str_index] == "'":
                    negative_index_mod += 1
                  if filtered[index+1].lower()[str_index] == "'":
                    negative_next_index_mod += 1
                  try:
                    if alpha_to_num[word.lower()[num-negative_index_mod]] == alpha_to_num[filtered[index+1].lower()[num-negative_next_index_mod]]: #if prior characters same
                      continue#no problems
                    break
                  except:
                    pass
                    # print(word,filtered[index+1])
                else: # if all characters same
                  temp =filtered[index]#swap
                  filtered[index] = filtered[index+1]
                  filtered[index+1] = temp
                  changed = True
              else:
                temp =filtered[index]#swap
                filtered[index] = filtered[index+1]
                filtered[index+1] = temp
                changed = True
        if changed == False: #sorted
          break # move on to next character
           
  for index, word in enumerate(filtered):
    filtered[index] = filtered[index].rstrip()
    filtered[index] = filtered[index].lstrip()
  #remove spaces
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
