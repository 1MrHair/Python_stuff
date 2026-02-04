def US_conversion(x,multi):
    x = int(x)
    multi = float(multi)
    x = x*multi
    return x

User_input_money = input("Enter US dollar amount > ")
User_input_mutli = input("Enter Conversion rate > ")

money = US_conversion(User_input_money, User_input_mutli)
print("Your money converted > ", money)
