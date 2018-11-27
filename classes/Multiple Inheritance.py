class Mario:
    def move(self):
        print('I am moving!')


class Shroom:
    def eat_shroom(self):
        print('Now I am big')


class BigMario(Mario, Shroom):
    pass #cancel the need to implement anything else in this class


bm = BigMario()
bm.move()
bm.eat_shroom()