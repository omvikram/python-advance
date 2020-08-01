import Cards
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') #Tuple
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') #Tuple
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14} #Dictionary

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Cards(suit, rank))
                
    def shuffle(self):
        return random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)


d = Deck()
    
print(d.all_cards[0])
print(d.all_cards[-1])    

d.shuffle()

print(d.all_cards[0])
print(d.all_cards[-1])

d.deal_one()
print(d.all_cards[0])
print(d.all_cards[-1])





