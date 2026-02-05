def my_math_add(x,y) :
  z=x+y
  return z

def my_math_multiply(x,y):
  z = x * y
  return z

def my_math_even(x,y):
  z = x + y
  if(z % 2 == 1):
    z = z + 1
  return z

def my_math(x,y,sign):
  if(sign == "+"):
    z = my_math_add(x,y)
  elif(sign == "-"):
    z = x - y
  elif(sign == "*"):
    z = my_math_multiply(x,y)
  elif(sign == "/"):
    z = x / y
  return z  

def main():
  keep_going = "Y"
  while(keep_going != "N"):
    Num_1 = input("Type your 1st number > ")
    Num_2 = input("Type your 2nd number > ")
    opperation = input("Type your Operation > ")
    try:
      Num_1 = int(Num_1)
      Num_2 = int(Num_2)
      answer = my_math(Num_1,Num_2, opperation)
      print("The answer is:",answer)
      keep_going = input("Keep going?(Y/N) > ")
    except:
      print("Error.")
    

main()
