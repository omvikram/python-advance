import Cards

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        self.all_cards.pop(0)

    def add_cards(self, new_card):
        if(type(new_card) == type([])):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)
    
    def __str__(self):
        return "Player {} has {} cards".format(self.name, len(self.all_cards))


jose = Player("Jose")
print(jose)
new_card = Cards("Spades", "Seven")
jose.add_cards(new_card)
print(jose)
jose.add_cards([new_card,new_card,new_card])
print(jose)