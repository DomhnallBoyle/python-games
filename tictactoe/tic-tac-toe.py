from random import randint

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.peg = None
        self.player_moves = []


def computer():
    pass


def opponent():
    players = [Player(raw_input("Player {} name: ".format(i))) for i in range(1, 3)]

    numbers = [0, 1]
    pegs = ['X', 'O']
    random_number = randint(0, 1)
    peg = raw_input("{}, please pick a peg (X, O): ".format(players[random_number].name))
    while peg not in pegs:
        peg = raw_input("{}, please pick a peg (X, O): ".format(players[random_number].name))

    players[random_number].peg = peg
    numbers.remove(random_number)    
    
    if peg == 'O':
        players[numbers[0]].peg = 'X'
    else:
        players[numbers[0]].peg = 'O'
        
    for player in players:
        print "{} - {}".format(player.name, player.peg)
    print "LETS PLAY!!"

    gameover = False
    available_coords = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    all_moves = {}
    width, height = 3, 3
    board = [[0 for x in range(width)] for y in range(height)]
    while not gameover:
        #loop through players taking selecting turns
        for player in players:
            while True:
                try:
                    co_ord = raw_input('{}, select a board position e.g. 01: '.format(player.name))
                    if co_ord in available_coords:
                        player.player_moves.append([int(i) for i in co_ord])
                        available_coords.remove(co_ord)
                        break
                except ValueError:
                    print 'Incorrect co-ordinates given'

        #print board after each turn
        all_moves[players[0].peg] = players[0].player_moves
        all_moves[players[1].peg] = players[1].player_moves

        for x in range(width):
            for y in range(height):
                for key, value in all_moves.items():
                    for position in value:
                        if position[0] == x and position[1] == y:
                            board[x][y] = key

        print_board(board)

        check_winner(players, board)


def check_winner(players, board):
    positions_groups = (
        [[(x, y) for y in range (3)] for x in range(3)] +
        [[(x, y) for x in range(3)] for y in range(3)] +
        [[(d, d) for d in range(3)]] +
        [[(2-d, d) for d in range(3)]]
    )

    for positions in positions_groups:
        values = [board[x][y] for (x, y) in positions]
        if len(set(values)) == 1 and values[0]:
            peg = values[0]
            for player in players:
                if peg == player.peg:
                    print '{} WINS!'.format(player.name)
    

def print_board(board):
                            
    print '    0   1   2'
    print '-----------'
    for i in range(0, 3):
        print '{} |'.format(i),
        for j in range(0, 3):
            print '{}  '.format(board[i][j]),
        print
        

if __name__ == "__main__":
    print "Tic-Tac-Toe by Domhnall Boyle\n"
    select_mode = "Please select a mode:\n1) Vs Computer\n2) Vs Opponent\n"

    while True:
        try:
            mode = int(raw_input(select_mode))
            if mode in [1, 2]:
                break
        except ValueError:
            print "1 or 2 please!"
    #print_board({})
    if mode is 1:
        computer()
    else:
        opponent()
