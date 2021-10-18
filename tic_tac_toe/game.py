from map import Map, Type


def new_int():
    ind = input()
    if not ind.isdigit():
        raise ValueError('Incorrect type of index')
    ind = int(ind)
    return ind


def valid_name(name):
    if name.isalpha():
        return True
    else:
        raise ValueError('Invalid player\'s name')


def get_name():
    try:
        name = input()
        if valid_name(name):
            return name
    except ValueError:
        return 'Invalid name'


class Game(object):
    def __init__(self, fir, sec):
        self.tiles = Map()
        if not fir.isalpha():
            raise ValueError('Incorrect name')
        if not sec.isalpha():
            raise ValueError('Incorrect name')
        self.players = (fir, sec)

    def move(self, new_type):
        for_ind = False
        ind = 0
        while not for_ind:
            print('Select the number of tile that you want to change:')
            try:
                ind = new_int()
            except ValueError:
                print('Incorrect index. You should enter an integer value')
                continue
            for_ind = True if 0 < ind < 10 else False
            if not for_ind:
                print('Tile with this number does not exist')
                continue
            if not self.tiles.is_empty(ind - 1):
                print('This tile is not empty.'
                      ' You should enter the number of the empty tile')
                for_ind = False
        ind -= 1
        self.tiles.change(new_type, ind)

    def check(self):
        win_comb = ((0, 1, 2), (0, 3, 6), (0, 4, 8), (1, 4, 7),
                    (2, 5, 8), (2, 4, 6), (3, 4, 5), (6, 7, 8))
        for each in win_comb:
            i = each[0] // 3
            j = each[0] % 3
            if (self.tiles.fields[i][j] ==
                self.tiles.fields[each[1] // 3][each[1] % 3] ==
                self.tiles.fields[each[2] // 3][each[2] % 3]) & \
                    (self.tiles.fields[i][j] is not Type.Empty):
                return True, False
        draw = True
        for i in range(3):
            for j in range(3):
                if self.tiles.fields[i][j] == Type.Empty:
                    draw = False
                    break
        return False, draw

    def start(self):
        end = False
        player_id = 0
        while not end:
            self.tiles.print()
            print(f'{self.players[player_id]}, your turn')
            self.move(Type(player_id + 1))
            end = self.check()
            if end[0]:
                self.tiles.print()
                print(f'Player {self.players[player_id]} is winner!')
                continue
            if end[1]:
                print('Friendship wins!!')
                break
            player_id = (player_id + 1) % 2
