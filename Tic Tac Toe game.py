#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


# In[2]:


# Write a function that can print out a board of 3*3
def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("-----------")
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("-----------")
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    


# In[3]:


test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']


# In[4]:


#Write a function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():
    marker=''
    while not (marker == 'X'or marker == 'O'):
        
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[5]:


#Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and 
#assigns it to the board.

def position_marker(board, position, marker):
    board[position]= marker


# In[6]:


# Write a function that takes in a board and checks to see if someone has won
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[7]:


#Write a function that uses the random module to randomly decide which player goes first.
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[8]:


#Write a function that returns a boolean indicating whether a space on the board is freely available

def space_check(board,position):
    return board[position]==' '


# In[9]:


#Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise
def board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True    


# In[10]:


#Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. 
#If it is, then return the position for later use.

def players_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position(1-9): '))
        
    return position


# In[14]:


#Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    return input('DO yo want to play again?  ').lower().startswith('y')


# In[76]:


pip install emoji # to make the game little attractive


# In[11]:


from emoji import emojize
x = emojize(":smiling_face_with_sunglasses:")
x


# In[15]:


# combined all the functions using while loop to run the game
print("Welcome to the Tic Tac Toe!", x)
while True:
    #Reset the board
    the_Board= [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')
    play_game= input('Are you ready to play ? ')
    if play_game.lower()[0]=='y':
        game_on= True
    else:
        game_on=False
        
        
    
    while game_on:
        if turn =='Player 1':                  #Player 1 turn
            display_board(the_Board)
            position= players_choice(the_Board)
            position_marker(the_Board, position, player1_marker) 
            
            if win_check(the_Board,player1_marker):
                display_board(the_Board)
                print('Congratulation! Player1 has won')
                game_on= False
            else:
                if board_check(the_Board):
                    display(the_Board)
                    print('The game is draw')
                    break
                else:
                    turn= 'Player 2'
        else:                                 #Player 2  turn   
            display_board(the_Board)
            position = players_choice(the_Board)
            position_marker(the_Board, position, player2_marker)
             
            if win_check(the_Board, player2_marker):
                display_board(the_Board)
                print('Congratulation! Player2 has won')
                game_on= False
            else:
                if board_check(the_Board):
                    display_board(the_Board)
                    print('The game is draw')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
        
        


# In[ ]:





# In[ ]:





# In[ ]:




