from enum import Enum


class Type(Enum):
    Empty = 0
    Zero = 1
    Cross = 2


class Map(object):
    def __init__(self):
        self.fields = [[Type.Empty, Type.Empty, Type.Empty],
                       [Type.Empty, Type.Empty, Type.Empty],
                       [Type.Empty, Type.Empty, Type.Empty]]

    def print(self):
        print('-------------')
        for i in range(3):
            print('|', end='')
            for j in range(3):
                if self.fields[i][j] == Type.Empty:
                    num = i * 3 + j + 1
                    print(f' {num} ', end='')
                elif self.fields[i][j] == Type.Zero:
                    print(' 0 ', end='')
                else:
                    print(' X ', end='')
                print('|', end='')
            print('\n-------------')

    def change(self, new_type, ind):    # ind--
        i = ind // 3
        j = ind % 3
        if not isinstance(new_type, Type):
            raise TypeError('Invalid type of tile')
        self.fields[i][j] = new_type

    def is_empty(self, ind):
        i = ind // 3
        j = ind % 3
        if self.fields[i][j] is Type.Empty:
            return True
        return False
