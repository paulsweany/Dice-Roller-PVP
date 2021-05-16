import random

def gameSetup(): #Sets up the game with a quantity of players, their names, and a quantity dice each player will roll.
  global diceQty
  global players
  print("\nWelcome to... DICE. ROLLER. PVP!\n")
  diceQty = int(input("How many dice should each player roll? "))
  playerQty = int(input("How many players are there? "))
  players = []
  for i in range(playerQty):
    players.append(str(input(f"What is player {i + 1}'s name? ")))
  print("Great! Here's who is playing:", *players, sep = " ")
  print()
  print(f"Each player will roll {diceQty} dice. There will be {playerQty} rounds; one for each player.\n")
  input("Press ENTER to start the game...\n")

def rollDice():
  scores = []
  currentPlayer = 0 #Variable to cycle through each player.
  for i in players:
    playerScore = []
    playerName = players[currentPlayer]
    for i in range(diceQty): #Rolls a die.
      playerScore.append(random.randint(1,6))
      print(f"{playerName} rolled a {playerScore[i]}! Their current score is {sum(playerScore)}.\n")
    scores.append(sum(playerScore)) #Adds the players total dice rolls to a list.
    currentPlayer = currentPlayer + 1
    print(f"{playerName}'s round is finished. Their final score is {sum(playerScore)}\n")
    highScore = sorted(scores, reverse = True) #Finds the current highest score.
    i = 0
    while scores[i] != highScore[0]:
      i += 1
    else:
      playerLead = players[i] #Need to create a tie-breaker
      print(f"{playerLead} is currently in the lead with a roll of {highScore[0]}!\n")
    if currentPlayer < len(players): #Either goes to the next round or prints final scores.
      input("Press ENTER to go to the next round...\n")
    else:
      print(f"{playerLead} wins with a total of {highScore[0]}!\n")
      print("Score Board:")
      for i in range(len(players)):
        print(f"{players[i]}: {scores[i]}")
      #Players and scores will be stored in a dictionary - scoreBoard.append{"player[i]": scores[i]}

gameSetup()
rollDice()
