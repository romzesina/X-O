positions = {
    '00': '-',
    '01': '-',
    '02': '-',
    '10': '-',
    '11': '-',
    '12': '-',
    '20': '-',
    '21': '-',
    '22': '-'
}

def draw_board():
        
    print (' ', 0, 1, 2)
    print (0, positions['00'], positions['01'], positions['02'])
    print (1, positions['10'], positions['11'], positions['12'])
    print (2, positions['20'], positions['21'], positions['22'])

def take_input(player_token):

    while True:
        value = input('Куда ввести: ' + player_token + ' ? ')
        if not (value in positions):
            print('Такой ячейки нет!')
            continue
        if positions[value] in 'XO':
            print('Эта клетка занята')
            continue
        if value in positions:
            positions[value] = player_token
        break


def check_win():

    wins_coord = {
        'win_com1': (positions['00'],positions['01'],positions['02']), 
        'win_com2': (positions['10'],positions['11'],positions['12']), 
        'win_com3': (positions['20'],positions['21'],positions['22']), 
        'win_com4': (positions['00'],positions['10'],positions['20']), 
        'win_com5': (positions['01'],positions['11'],positions['11']), 
        'win_com6': (positions['02'],positions['12'],positions['22']), 
        'win_com7': (positions['00'],positions['11'],positions['22']), 
        'win_com8': (positions['02'],positions['11'],positions['20'])
    }
    
    if ('X', 'X', 'X') in list(wins_coord.values()):
        return 'X'
    elif ('O', 'O', 'O') in list(wins_coord.values()):
        return 'O'
    else:
        return False 

def main():

    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        winner = check_win()
        if winner:
            draw_board()
            print(winner, 'выиграл!')
            break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья!')
            break

main()






        

