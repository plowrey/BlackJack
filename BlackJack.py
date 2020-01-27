#Rules of BlackJack
#The dealer deals 2 cards to the player
#Then gives himself 2 cards; one face up and one facedown
#The player then is given the option to get another card or stay
#if hit and bust, the player loses
#if player gets 21 or "BlackJack", they win
#if they stay and still arent at 21
#the dealer reveals his second card
#the dealer can draw another card to try and get to 21
#if the dealer goes over 21 or "busts", the player wins


import random


#function for player drawing 2 cards
#def random_card(c1, c2):
#    print('Your Cards are:', '|', c1, '|', c2, '|')
#    tot = c1 + c2
#    if tot > 21:
#        print('Bust! Start Over')
#    else:
#        print('Your Total is', tot)
#random_card(random.randint(1, 13), random.randint(1, 13))

#shows what the dealers first card is
dealer_card1 = random.randint(1, 13)
print('______________________________________')
print('The dealer drew:', dealer_card1)
print('______________________________________')

c1 = random.randint(1, 13)
c2 = random.randint(1, 13)
print('Your Cards are:', '|', c1, '|', c2, '|')
tot = c1 + c2
if tot > 21:
    print('Bust! Start Over')
elif tot == 21:
    print('BlackJack! You Win!')
else:
    print('Your Total is', tot)

#code that asks player if they want to hit or stay
hit = 'y'
while hit == 'y':
    hit = str(input('"y" to hit or "n" to stay: '))
    if hit == 'n':
        break
    new = random.randint(1, 13)
    print('Your card is:', '|', new, '|')
    tot = tot + new
    if tot > 21:
        print('Bust! You Lose!')
    elif tot == 21:
        print('BlackJack! You Win!')
    else:
        print('Your New Total is: ', tot)
print('______________________________________')

#code to find out what dealers hidden card is
dealer_hidden = random.randint(1, 13)
print('Dealers Cards are', '|', dealer_card1, '|', dealer_hidden, '|')
dealer_total = dealer_card1 + dealer_hidden
while dealer_total < 17:
    next_card = random.randint(1,13)
    print('Dealer Hit- The Card is: ', '|', next_card, '|')
    dealer_total = dealer_total + next_card
print('Dealers Total is', dealer_total)


#code determines who has won the game
if dealer_total > 21:
        print('The Dealer has busted! You Win!')
elif dealer_total < tot:
    print('Dealer has', dealer_total, 'You Lose!')
elif dealer_total > tot:
    print('You have', tot, 'You Win!')
else:
    print('You have', tot,',' 'Dealer has', dealer_total, 'Push!')
