#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# tuple ipv list --> niet veranderbaar
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#boolean waarde is nodig voor de while loop


# In[2]:


class Card(): 
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[3]:


class Deck():

    #geen attribute nodig, want er is geen user input
    #alle decks horen hetzelfde te zijn
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  

#welke kaarten zitten er in de deck?  
    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


# In[4]:


class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0   
    
    def add_card(self,card):
        #from deck.deal()
        self.cards.append(card)
        self.value += values[card.rank] 
        
        #track aces
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        #ace is bij begin 11, stel value > 21
        #dan switch je de ace naar 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


# In[5]:


class Chips:
    
    def __init__(self, total = 100):
        self.total = total 
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# In[6]:


def take_bet(chips):
    #als 'playing' True is
    while True:
        
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Whoops. Please provide an integer")
        else: 
            if chips.bet > chips.total:
                print(f"Sorry, you can't exceed {chips.total}")
            else:
                break
    


# In[7]:


def hit(deck,hand):
    
    #kaart van deck
    single_card = deck.deal()
    #kaart toevoegen aan hand
    hand.add_card(single_card)
    #is het een ace? 
    hand.adjust_for_ace()


# In[8]:


def hit_or_stand(deck,hand):
    global playing  # wanneer player stand kiest, moet niet heel het spel stoppen
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        #je pakt de eerste letter van de string[0]
        if x[0].lower() == 'h':
            hit(deck,hand) 

        elif x[0].lower() == 's':
            print("You stand. Dealer is playing.")
            playing = False
        
        #extra
        else:
            print("Sorry, please enter an 'h' or 's'.")
            continue
        break


# In[9]:


def show_some(player, dealer):
    #show only one of dealers cards
    print("\nDealer's hand: ")
    print("First card hidden")
    print(dealer.cards[1])
    
    #show two cards of the player
    print("\nYour hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of your hand: {player.value}")
    
def show_all(player, dealer):
    print("\nDealer's hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand: {dealer.value}")
    
    
    print("\nYour hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of your hand: {player.value}")


# In[10]:


#scenario's uitwerken
def player_busts(player,dealer,chips):
    print("YOU BUST")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("YEAH, YOU WIN")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("DEALER BUSTS, YOU WIN")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS")
    chips.lose_bet()
    
def push(player,dealer):
    print("YOU AND DEALER TIE")


# In[ ]:

  
player_chips = Chips()    
    # Set up the Player's chips
while True:
    print("Welcome to this game of Black Jack, enjoy!")

    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    # Create & shuffle the deck, deal two cards to each player
    
    take_bet(player_chips)
    # Prompt the Player for their bet

    show_some(player_hand, dealer_hand)
    # Show cards (but keep one dealer card hidden)

    
    while playing:
        
        hit_or_stand(deck, player_hand)
        # Prompt for Player to Hit or Stand
        
        show_some(player_hand, dealer_hand)
        # Show cards (but keep one dealer card hidden)
 
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
        # If player's hand exceeds 21, run player_busts() and break out of loop
            break
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
        show_all(player_hand, dealer_hand)
        # Show all cards
    
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else: 
            push(player_hand, dealer_hand)
        # Run different winning scenarios
        
    print(f"\n Player total chips are at: {player_chips.total}")
    # Inform Player of their chips total 
    new_game = input("Would you like to play another hand? y/n")
    
    if new_game[0].lower() == 'y':
        playing = True
        
    else:
        print("Thank you for playing")
        break

        
    # Ask to play again

    


# In[ ]:




