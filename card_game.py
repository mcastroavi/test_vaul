import random
class Card:
     #["♣","♦","♥","♠"]
    suit_list=["Clubs","Diamonds","Hearts","Spades"]
    rank_list=["None","Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank_list[self.rank] +" of " + self.suit_list[self.suit]
   

class Deck:
    def __init__(self):
        self.cards = [] # All cards 
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s+= i * " " + str(self.cards[i]) + "\n"
        return s
    def shuffle(self):
        x = random.shuffle(self.cards)
        return x
    def take_five(self):
        c = ""
        for i in range(0,6):
            c+= i * " " + str(self.cards[i]) + "\n"
        return c
    def take_five_more(self):
        c2= ""
        for i in range(7, 13):
            c2+= i * " " + str(self.cards[i]) + "\n"
        return c2
    def high_card(self):
        return self.cards[1] == self.cards[2] 


d = Deck()
d.shuffle()
player1 = d.take_five()
player2 = d.take_five_more()
print("Player 1 cards deck: ","\n",player1)
print("Player 2 cards deck: ","\n",player2)

d.high_card()
print(d.high_card())
