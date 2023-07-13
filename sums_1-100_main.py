def equation_converter(x):
  """takes a list of numbers and returns a string with the numbers beginning with "=" and having a '+' in between
  """
  string = "" #creates an empty string
  for i in range(len(x)):
    string += f"{x[i]} + " #adds numbers to string with "+" after each number
  string = string[0:-3] #removes the last +
  string = f"= {string}"#adds "=" to beginning
  return string

def sum_finder(x):
  """takes a variable and returns the sum of consecutive natural numbers, if not possible returns 'NOT possible'
  """
  for i in range (1, 100 +1): 
    consecutive_integers_list = [] #refreshes the list once the loop underneath is finished
    for j in range (i , 100 + 1):  
      consecutive_integers_list.append(j)
      if sum(consecutive_integers_list) == x:
        if consecutive_integers_list[0] != x:
          return equation_converter(consecutive_integers_list)
        else:
          return "is NOT possible."
      elif sum(consecutive_integers_list) < x:
        continue
    
#putting it in the file:
with open("sums.txt", "w") as f:
  for i in range (1, 100+1):  
    print(i, sum_finder(i), file = f)  