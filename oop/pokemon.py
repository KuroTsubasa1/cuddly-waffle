class Pokemon:
    hp = None
    atk = None
    type = None

    def __init__(self, hp, atk, type):

        self.hp = hp
        self.atk = atk
        self.type = type

    def loose_life(self, damage):
        self.hp = self.hp - damage


morris = Pokemon(999, 10, 'SWAGGER')

lasse = Pokemon(100, 5, 'Lasse')

lasse.loose_life(50)

print(morris.hp)

print(lasse.hp)



