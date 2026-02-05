def my_math(x,y) :
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

def main():
  my_num_1 = 5
  my_num_2 = 4
  sum = my_math(my_num_1, my_num_2)
  print("The sum of", my_num_1, "+", my_num_2, "=",sum)
  product = my_math_multiply(my_num_1, my_num_2)
  print("The product of", my_num_1, "*", my_num_2, "=",product)
  even = my_math_even(my_num_1, my_num_2)
  print(even)

main()
