import unittest

from .game import Room
from .game import Game


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.x = 5
        self.y = 4
        self.name = "Room to test your unit"
        self.description = "You see units standing, ready for test."
        self.exits = ['This way', 'That way']
        self.room = Room(self.x, self.y, self.name, self.description, self.exits)

    def test_str(self):
        expected = f'{self.name}\n{self.description}'
        result = self.room.__str__()
        self.assertEqual(expected, result)

    def test_str_negative(self):
        result = self.room.__str__()
        self.assertNotEqual('', result)

    def test_check_exit_positive(self):
        result = self.room._check_exit('This way')
        self.assertTrue(result)

    def test_check_exit_negative(self):
        result = self.room._check_exit('No way')
        self.assertFalse(result)


class TestGame(unittest.TestCase):
    Directions = {
        "north": (0, -1),
        "south": (0, 1),
        "west": (-1, 0),
        "east": (1, 0)
    }

    def setUp(self):
        self.player_x = 0
        self.player_y = 0
        self.new_x = 0
        self.new_y = -1
        self.room1 = Room(0, 0, "Main room", "", ["north"])
        self.room2 = Room(0, -1, "Second room", "", ["south"])
        self.map = {(self.room1.x, self.room1.y): self.room1,
           (self.room2.x, self.room2.y): self.room2}
        self.game = Game(self.map)

    def test_move_positive(self):
        self.game._move(self.new_x, self.new_y)
        self.assertEqual(self.player_x + self.new_x, self.game.player_x)
        self.assertEqual(self.player_y + self.new_y, self.game.player_y)

    def test_move_negative(self):
        self.game._move(self.new_x, self.new_y)
        self.assertNotEqual(self.player_x + self.new_x - 1, self.game.player_x)
        self.assertNotEqual(self.player_y + self.new_y - 1, self.game.player_y)

    def test_get_room_positive(self):
        expected = self.map.get((self.new_x, self.new_y))
        rez = self.game._get_room( self.new_x, self.new_y)
        self.assertEqual(expected, rez)

    def test_get_room_negative(self):
        expected = self.map.get((self.new_x-1, self.new_y-1))
        rez = self.game._get_room(self.new_x, self.new_y)
        self.assertNotEqual(expected, rez)


if __name__ == '__main__':
    unittest.main()
