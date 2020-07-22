'''Без использования библиотек, создать класс для представления информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд.'''


class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if value <= 23:
            self._hours = value
        else:
            self._hours = 23
            print(f'{h} недопустимое число в параметре Hours')
    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        if value <= 59:
            self._minutes = value
        else:
            self._minutes = 59
            print(f'{m} недопустимое числов в параметре  Minutes')

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        if value <= 59:
            self._seconds = value
        else:
            self._seconds = 59
            print(f'{s} недопустимое числов в параметре Seconds')

    def time_shift(self, add_second, add_minutes, add_hours):

        shifted_second = s + add_second
        shifted_minutes = m + add_minutes
        shifted_hours = h + add_hours
        new_seconds = shifted_second % 60
        new_minutes = shifted_minutes % 60
        new_hours = shifted_hours % 24

        return new_hours, new_minutes, new_seconds

    def __repr__(self):
        return f" Time: {self.hours}:{self.minutes}:{self.seconds} "

    def __str__(self):
        return f"Time: {self.hours}:{self.minutes}:{self.seconds} "


h = 23
m = 44
s = 35

seconds_shift = 20
minutes_shift = 10
hours_shift = 2

time_info = Time(h, m, s)

add_time = time_info.time_shift(seconds_shift, minutes_shift, hours_shift)

print(time_info)
