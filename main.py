class Tomato:
    states = {1: 'зеленый', 2: 'зелено-желтый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._state += 1

    def is_ripe(self):
        if self.states == 3:
            return True
        else:
            return False


class TomatoBush:
    def __init__(self, amount):
        a = []
        for i in range(amount):
            a.append(Tomato(None))
        self.tomatoes = a

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:
            if i._state != 3:
                return False
        return True

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Сбор урожая')
            self._plant.give_away_all()
        else:
            print('Недостаточно спелые помидоры')

    @staticmethod
    def knowledge_base():
        print(
            'Садовник Яна 21 год,очень хозяйственная девушка,немного строгая,но уверяю,что помидоры у нее самые лучшие!')


if __name__ == '__main__':
    bush1 = TomatoBush(9)
    gardener1 = Gardener('Виктория', bush1)
    gardener1.knowledge_base()
    gardener1.work()
    gardener1.harvest()
    gardener1.work()
    gardener1.work()
    gardener1.harvest()
