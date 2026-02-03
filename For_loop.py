def main():
  print("Starting The Code Challenge")
  x = [0,10,20,30,40,50,60,70,80,90,100]
  for i in x:
    print(i)
  for i in range(0,len(x),2):
    print(x[i])
  User_input = input("Type a number 1-10 > ")
  User_input = int(User_input) + 1
  for i in range(0,User_input,1):
    print(x[i])
  print("Ending The Code Challenge")
main()
