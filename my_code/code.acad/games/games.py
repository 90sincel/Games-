import random

money = 100

#code for deck and cards 
def random_card(wager):
  deck = [[i] * 4 for i in range(1, 13)]
  cards = [j for i in deck for j in i]
  
def random_walk(wager, call):
  flip = random.randint(1, 2)
  if flip == 1:
    print("It's heads!")
  if flip == 2:
    print("It's tails!")
  if flip == 1 and call.lower() == "heads":
    print("You got it champ!, {} was right, you're up {}".format(call, wager))
  elif flip == 2 and call.lower() == "tails":
    print("You got it champ!. {} was right, you're up {}".format(call, wager))
  else: 
    print("Sorry! You're down {}".format(wager))

def Cho_han(wager, call):
  dice_1 = random.randint(1, 6)
  dice_2 = random.randint(1, 6)
  outcome = dice_1 + dice_2
  result = 0
  if outcome % 2 == 0:
    result = 1
    print("Even!")
  else:
    result = 2
    print("Odd!")
  if result == 1 and call.lower() == "even":
    print("Master predictor, you're now up {}".format(wager))
  elif result == 2 and call.lower() == "odd":
    print("Master predictor, you're now up {}".format(wager))
  else:
    print("Fortune favors the persistent! Give me {} bucks though.".format(wager))

def random_card(wager):
  deck = [[i] * 4 for i in range(1, 13)]
  cards = [j for i in deck for j in i]
  #random choice of card from deck. Probability of choosing same card = 0, second code line
#card1 == the player / card2 == the computer
  card1 = random.choice(cards)
  cards.remove(card1)
  card2 = random.choice(cards)
  cards.remove(card2)
  #let the games begin 
  if card1 > card2:
    print("You drew a {}, which beats a {}. You won ${}!".format(card1, card2, wager))
  elif card1 < card2:
    print("You drew a {}, which losses to a {}. You lost ${}!".format(card1, card2, wager))
  else:
    print("It's a tie! You keep the wager!")
random_card(60)

def roulette(wager, call):
  wheel = random.randint(0, 36)
#odd vs. even
#Logic for odd and even
  if type(call) == int and call == wheel:
    print("{}! Nice playing, you're up ${}.".format(wheel, wager * 35))
    return +(wager * 35)
  elif type(call) == int and call != wheel:
    print("{}! Fortune favors the persistent friend".format(wheel))
    return -wager
  elif call.lower() == "odd" and (wheel % 2 != 0):
    print("{} odd! Nice playing, you're up ${}.".format(wheel, wager))
    return +wager
  elif call.lower() == "even" and wheel % 2 == 0:
    print("{} even! Nice playing, you're up ${}.".format(wheel, wager))
    return +wager
  else:
    print("{}! Fortune favors the persistent friend".format(wheel))
    return -wager 
