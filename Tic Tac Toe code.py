#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Maak het bord aan
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])


# In[2]:


#Controleer of het bord goed is
#gegevens zijn gegeven

test_board = ['#',' ',' ',' ',' ','X','O','X','O','X']
display_board(test_board)


# In[3]:


#De input moet gelijk zijn aan X of O
#Spelers kunnen kiezen welke waarde ze willen zijn

def player_input():
    marker = ' '
    
    while marker != 'X' or marker != 'O': 
        
        marker = input("Player 1: Choose your marker: X or O: ").upper()
    
        if marker.upper() == 'X':
            return ('X', 'O')
        
        elif marker.upper() == 'O':
            return ('O', 'X')
    #extra toegevoegd: waarom moet een speler opnieuw input geven?
        else:
            print("Sorry, I did not understand that. Please enter an X or O.")
            continue
        


# In[4]:


player_input()


# In[5]:


#een positie in het bord moet gelijk staan aan een marker
def place_marker(board, marker, position):
    
    board[position] = marker


# In[6]:


place_marker(test_board, '<3', 2)
display_board(test_board)


# In[7]:


#heeft er iemand gewonnen?
def win_check(board,mark):
    
    #3 rijen
    #3 colommen
    #2 zijwaarts
    
        return ((board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[1] == board[5] == board[9] == mark) or
        (board[3] == board[5] == board[7] == mark))

    
    


# In[8]:


win_check(test_board, 'O')


# In[9]:


#welke speler mag er eerst

import random

def choose_first():
    first = random.randint(0,1)
    
    if first == 0:
        return("Player 1")
    else:
        return("Player 2")


# In[10]:


choose_first()


# In[11]:


#is de plek leeg?

def space_check(board,position):
    
    if board[position] == ' ':
        return True
    else:
        return False


# In[12]:


space_check(test_board, 1)


# In[13]:


def full_board_check(board):
    
    for key in range(1,10):
        #als space_check True antwoord, dan is het bord niet vol
        if space_check(board,key):
            return False
    return True 


# In[14]:


full_board_check(test_board)


# In[15]:


#de speler moet een positie in het bord kiezen
def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
 
        #extra toevoegd: waarom moeten we opnieuw kiezen? 
    
        try:
            position = int(input('Choose your next position: (1-9) '))
        #als het geen integer is
        except:
            print("Whoops, that is not a number")
            continue
            
        #als het wel een integer is, maar...
        else: 
            if position not in [1,2,3,4,5,6,7,8,9]:
                print("Whoops, that is not a number between 1 and 9")
                continue
            elif not space_check(board,position):
                print("Whoops, that place has already been filled")
                continue  

        return position
       
   
        
  
            


# In[16]:


player_choice(test_board)


# In[17]:


def replay():
    
    choice = input ('Do you want to play the game again? Reply yes or no: ').lower()
    
    if choice == 'yes':
        return True
    else:
        pass


# In[18]:


replay()


# In[19]:


#het spel laten lopen

print('Welcome to Tic Tac Toe!')

while True:
    
    #bord opzetten
    #welke speler wilt wat zijn
    #welke speler mag eerst
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ": you may start")
    
    play_game = input('Ready to play? yes or no? ')
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False
        
    
    while game_on:
        
        if turn == "Player 1":
            #bord zien
            display_board(the_board)
    
            #positie kiezen
            position = player_choice(the_board)
            
            #invullen van de positie
            place_marker(the_board,player1_marker,position)
            
            #gewonnen?
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print ('Congratulations player 1, you have won! =D' )
                game_on = False
           
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game")
                    game_on = False
                    
                else:
                    turn = "Player 2"
            
        else:
                    
            display_board(the_board)
            
            #positie kiezen
            position = player_choice(the_board)
            
            #invullen van de positie
            place_marker(the_board,player2_marker,position)
            
            #gewonnen?
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print ('Congratulations player 2, you have won! =D ')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game")
                    game_on = False
                else:
                    turn = "Player 1"
                        
    if not replay():
        break


# In[ ]:





# In[ ]:




