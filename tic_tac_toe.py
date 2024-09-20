the_board = { 'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
             'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
             'low-l': ' ', 'low-m': ' ', 'low-r': ' ',}

def print_board(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

print_board(the_board)
