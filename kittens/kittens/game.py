################################################################################
## Kittens in a Blender Game Logic                                            ##
## Creates and manages the game layout, cards, players, and win conditions    ##
################################################################################


CARD_TYPE = ['kitten', 'blend', 'action']
COLORS = ['blue', 'pink', 'green', 'yellow', 'purple']


class Player:
    def __init__(self, name, id, color):
        self.name = name
        self.id = id
        self.color = color


class Card:
    def __init__(self, type, title, owner_id=None):
        self.type = type
        self.title = title
        self.owner_id = owner_id
