from tkinter import *
import random
root = Tk()
root.title('Крестики-нолики')
game_run = True
field = []

def new_game():
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True

def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        check_win('X')
        if game_run:
            computer_move()
            check_win('O')

# Функция для перебора возможных комбинаций выигрыша, образующих линию 
def check_win(smb):
    for n in range(10):
        for j in range (5):
            check_line(field[n][0], field[n][1], field[n][2],field[n][3],field[n][4], smb)
            check_line(field[n][j+1], field[n][j+2], field[n][j+3],field[n][j+4],field[n][j+5], smb)
            check_line(field[0][n], field[1][n], field[2][n],field[3][n], field[4][n], smb)
            check_line(field[j+1][n], field[j+2][n], field[j+3][n],field[j+4][n], field[j+5][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], field[3][3], field[4][4], smb)        
    for n in range(6):
        for j in range (5): 
            check_line(field[n][j+1], field[n+1][j+2], field[n+2][j+3], field[n+3][j+4], field[n+4][j+5], smb)
            check_line(field[n+4][j+1], field[n+3][j+2], field[n+2][j+3], field[n+1][j+4], field[n][j+5], smb)
    for n in range(6):
        for j in range (5):         
            check_line(field[n+4][j], field[n+3][j+1], field[n+2][j+2], field[n+1][j+3], field[n][j+4],smb)        
            
def check_line(a1,a2,a3,a4,a5,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] =a4['background'] = a5['background']= 'pink'
        global game_run
        game_run = False

def can_win(a1,a2,a3,a4,a5,smb):
    res = False
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == ' ':
        a5['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a1['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == ' ' and a5['text'] == smb:
        a4['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ' and a4['text'] == smb and a5['text'] == smb:
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == ' ':
        a5['text'] = 'O'
        res = True

    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == ' ':
        a1['text'] = 'O'
        res = True         
    return res

#Действия компьютера
def computer_move():
    for n in range(10):
        for j in range (5):
            if can_win(field[n][0], field[n][1], field[n][2],field[n][3],field[n][4], 'O'):
                return
            if can_win(field[n][j+1], field[n][j+2], field[n][j+3],field[n][j+4],field[n][j+5], 'O'):
                return     
            if can_win(field[0][n], field[1][n], field[2][n],field[3][n], field[4][n], 'O'):
                return
            if can_win(field[j+1][n], field[j+2][n], field[j+3][n],field[j+4][n], field[j+5][n], 'O'):
                return
    if can_win(field[0][0], field[1][1], field[2][2], field[3][3], field[4][4], 'O'):
        return            
    for n in range (6):    
        for j in range (5):   
            if can_win(field[n][j+1], field[n+1][j+2], field[n+2][j+3], field[n+3][j+4], field[n+4][j+5], 'O'):
                return  
            if can_win(field[n+4][j+1], field[n+3][j+2], field[n+2][j+3], field[n+1][j+4], field[n][j+5], 'O'):
                return    
    for n in range(6):
        for j in range (5):                         
            if can_win(field[n+4][j], field[n+3][j+1], field[n+2][j+2], field[n+1][j+3], field[n][j+4], 'O'):
                return             
          
    for n in range(10):
        for j in range (5):
            if can_win(field[n][0], field[n][1], field[n][2],field[n][3],field[n][4], 'X'):
                return
            if can_win(field[n][j+1], field[n][j+2], field[n][j+3],field[n][j+4],field[n][j+5], 'X'):
                return   
    if can_win(field[0][0], field[1][1], field[2][2], field[3][3], field[4][4], 'X'):
        return  
    if can_win(field[4][0], field[3][1], field[2][2], field[1][3], field[0][4], 'X'):
        return     
    for n in range (6):
        for j in range (5):          
            if can_win(field[n][j+1], field[n][j+2], field[n][j+3],field[n][j+4],field[n][j+5], 'X'):
                return  
            if can_win(field[n+4][j+1], field[n+3][j+2], field[n+2][j+3], field[n+1][j+4], field[n][j+5], 'X'):
                return 
    for n in range(6):
        for j in range (5):                         
            if can_win(field[n+4][j], field[n+3][j+1], field[n+2][j+2], field[n+1][j+3], field[n][j+4], 'X'):
                return            
    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

for row in range(10):
    line = []
    for col in range(10):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=10, column=0, columnspan=10, sticky='nsew')
root.mainloop()                            
