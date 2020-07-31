from random import randint


class Battleship:
    """
    Base class for battleship game
    """

    def __init__(self, size):
        """
         :param size:playboard size
        """
        self.size = size

    def field_ships_gen(self):
        self.field_ships = [['~'] * self.size for _ in range(self.size)]
        for n in range(8):
            ship_row = randint(0, self.size - 1)
            ship_col = randint(0, self.size - 1)
            self.field_ships[ship_col][ship_row] = 'o'
        print('Поле кораблей')
        for i in range(self.size):
            for j in range(self.size):
                print(self.field_ships[i][j], end='  ')
            print()
        return self.field_ships

    def field_shots_gen(self):
        self.field_shots = [['~'] * self.size for _ in range(self.size)]
        print('Поле выстрелов')
        for i in range(self.size):
            for j in range(self.size):
                print(self.field_shots[i][j], end='  ')
            print()
        return self.field_shots

    def check_coord(self, x, y):
        try:
            if self.field_ships[x][y] == 'o':
                self.field_shots[x][y] = 'x'
                print('ВЫ ПОПАЛИ, ПРОДОЛЖАЙТЕ В ТОМ ЖЕ ДУХЕ!!!!')
            else:
                print('Мимо!\nПопробуйте еще раз!')
        except:
            print('Укажите правильное значение')

    def run(self):
        player_ship_1 = Battleship.field_ships_gen(self)
        player_shot_1 = Battleship.field_shots_gen(self)
        while True:
            print('Сделайте ход!')
            try:
                x = int(input("x:"))
                y = int(input("y:"))
                player_check_1 = Battleship.check_coord(self, x, y)
            except:
                print('Укажите правильное значение')


size = 10
battle = Battleship(size)

battle.run()







