import string

def make_board(board):
    format_board(board)
    #print('  ┼', '───┼', sep='')
    for row_number, row in enumerate(board):
        print('  ┼', end='')
        for column_number, column in enumerate(row):
            print('───┼', sep='', end='')
        print('\n', row_number + 1, end='│')
        for column_number, column in enumerate(row):
            print(column,end='')
        print()
    print('  ┼', end='')
    for column_number, column in enumerate(row):
        print('───┼', sep='', end='')
    print()
    print(' ', end='')
    for letter in range(len(board[0])):
        print(f'   {string.ascii_uppercase[letter]}', end='')
    print()

def format_board(board):
    for row_number, row in enumerate(board):
        for column_number, column in enumerate(row):
            board[row_number][column_number] = f' {column} │'

if __name__ == '__main__':
    board = [['1','2','3','4','5'],['1','2','3','4','5'],['1','2','3','4','5']]
    make_board(board)