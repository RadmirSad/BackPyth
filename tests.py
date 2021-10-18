import game as my
import unittest
from map import Map, Type


class TestMap(unittest.TestCase):
    def setUp(self):
        self.my_map = Map()

    def test_changing_valid(self):
        self.my_map.change(Type.Zero, 0)
        self.assertIs(self.my_map.fields[0][0], Type.Zero)

    def test_changing_invalid(self):
        with self.assertRaises(TypeError):
            self.my_map.change(5, 0)

    def test_is_empty(self):
        for i in range(3, 7):
            self.my_map.change(Type.Zero, i)
            self.assertFalse(self.my_map.is_empty(i))
        for k in range(3):
            self.assertTrue(self.my_map.is_empty(k))
        for j in range(7, 9):
            self.assertTrue(self.my_map.is_empty(j))


class TestGame(unittest.TestCase):
    def setUp(self):
        players = ('First', 'Second')
        self.tic_tac = my.Game(players[0], players[1])

    def test_input_valid_name(self):
        self.assertTrue(my.valid_name('Alex'))

    def test_input_invalid_name(self):
        with self.assertRaises(ValueError):
            my.valid_name('Adam3')

    def test_input_int_valid(self):
        print('Enter "15"')
        self.assertEqual(my.new_int(), 15)

    def test_input_int_invalid(self):
        print('Enter any symbol except numbers:')
        with self.assertRaises(ValueError):
            my.new_int()

    def test_get_name_valid(self):
        print('Enter the name "Sveta"')
        self.assertEqual(my.get_name(), 'Sveta')

    def test_get_name_invalid(self):
        print('Enter "bad" string:')
        self.assertEqual(my.get_name(), 'Invalid name')

    def test_construct_invalid(self):
        dop_players = ('Fir1', 'Sec')
        with self.assertRaises(ValueError):
            my.Game(dop_players[0], dop_players[1])

    def test_move_valid(self):
        print('Enter the next values: -1, 4, 4, 7')
        self.tic_tac.move(Type.Zero)
        self.assertEqual(self.tic_tac.tiles.fields[1][0], Type.Zero)
        self.tic_tac.move(Type.Cross)
        self.assertEqual(self.tic_tac.tiles.fields[2][0], Type.Cross)

    def test_check(self):
        self.tic_tac.tiles.change(Type.Zero, 6)
        self.assertFalse(self.tic_tac.check()[0])
        self.tic_tac.tiles.change(Type.Zero, 4)
        self.assertFalse(self.tic_tac.check()[0])
        self.tic_tac.tiles.change(Type.Zero, 2)
        self.assertTrue(self.tic_tac.check()[0])
        self.tic_tac.tiles.change(Type.Cross, 2)
        self.tic_tac.tiles.change(Type.Zero, 3)
        self.tic_tac.tiles.change(Type.Cross, 0)
        self.tic_tac.tiles.change(Type.Zero, 1)
        self.tic_tac.tiles.change(Type.Cross, 5)
        self.tic_tac.tiles.change(Type.Zero, 8)
        self.tic_tac.tiles.change(Type.Cross, 7)
        end = self.tic_tac.check()
        self.assertFalse(end[0])
        self.assertTrue(end[1])


if __name__ == '__main__':
    unittest.main()
