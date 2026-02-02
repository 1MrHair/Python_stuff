def main():
  cycle = 0
  User_input = input("Enter a number greater than 20 > ")
  try:
    User_input = int(User_input)
  except:
    print("Not a number.")
    User_input = 0
  if(User_input > 20):
    while (cycle < 5):
      print(User_input)
      User_input = User_input/2
      cycle = cycle + 1
  else:
    print("Bad input")

main()
