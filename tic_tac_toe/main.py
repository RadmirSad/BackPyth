import game as my

if __name__ == '__main__':
    print('Enter the first player\'s name:')
    first = my.get_name()
    print(f'The first player\'s name: {first}')
    print('Enter the second player\'s name:')
    second = my.get_name()
    print(f'The second player\'s name: {second}')
    tic_tac = my.Game(first, second)
    tic_tac.start()
