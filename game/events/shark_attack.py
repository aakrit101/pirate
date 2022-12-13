from game import event
import random
from game.combat import Combat
from game.combat import Shark
from game.display import announce

class DangerousSharkAttack (event.Event):

    def __init__(self):
        self.name = " dangerous shark attack"

    def process (self, world):
        result = {}
        result["message"] = "the sharks have been taken care off!"
        monsters = []
        min = 2
        uplim = 6
        if random.randrange(2) == 0:
            min = 1
            uplim = 5
            monsters.append(Shark("Very Big Shark"))
            monsters[0].speed = 1.2*monsters[0].speed
            monsters[0].health = 2*monsters[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        while n <= n_appearing:
            monsters.append(Shark(" kill, ignore or cage shark "+str(n)))
            n += 1
        announce ("Captain we are under a massive shark attack!")
        Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result
