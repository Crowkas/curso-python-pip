import random

def choose_option():
  options = ('piedra','papel','tijera')
  user_option = input('piedra, papel o tijera: ')
  user_option = user_option.lower()
 
  if not user_option in options:
    print('Invalid option')
    #continue
    return None, None
  
  computer_option = random.choice(options)

  print('User_option: ', user_option)
  print('Computer_option: ', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('User gano')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('Computer gano')
      computer_wins +=1
  elif user_option == 'papel':
    if computer_option == 'Piedra':
      print('papel gana a tijera')
      print('User gano')
      user_wins += 1
    else: 
      print('tijera gana a papel')
      print('Computer gano')
      computer_wins +=1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('User gano')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('Computer gano')
      computer_wins +=1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND:', rounds)
    print('*' * 10)
    
    print('Computer score:', computer_wins)
    print('User score:', user_wins) 
    rounds +=1
    
    user_option, computer_option = choose_option()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    
    if computer_wins == 3:
      print('*' * 10)
      print("Computer WINS")
      print('*' * 10)
      break
      
    if user_wins == 3:
      print('*' * 10)
      print("User WINS")
      print('*' * 10)
      break
    
run_game()
