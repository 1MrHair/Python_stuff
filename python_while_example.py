def main():
   print("Starting The Code Challenge")
   Correct_num = 6
   User_input = 0
 
   while (User_input != Correct_num):
     User_input = input("Guess the number 1-10 > ")
     try:
       User_input = int(User_input)
     except:
       print("Not a number! Try again > ")
   print("Correct!")
   print("Ending The Code Challenge")

main()
