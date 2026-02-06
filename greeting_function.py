def greet(lang):
  if lang == 'es':
    return'Hola'
  elif lang == 'fr':
    return'Bonjour'
  elif lang == 'po':
    return 'Witam'
  elif lang == 'ro':
    return 'Buna ziua'
  elif lang == 'ge':
    return 'Guten Tag'
  else:
    return'Hello'

def main():
  User_name = input("What is your name? > ")
  User_language = input("What is your 1st language(ge = german, fr = french)? > ")
  print(greet(User_language) + ", " + User_name + "!")


main()
