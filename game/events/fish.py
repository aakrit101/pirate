from game.ship import *
from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random



class CatchAFish (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "fish is present in the ocean"
        self.fish = 1
        self.verbs['catch'] = self
        self.verbs['ingore'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "catch"):
            self.go = True
            r = random.randint(1,10)
            if (r < 5):
                self.result["message"] = "Luckily we caught a big fish."

            else:

                c = random.choice(config.the_player.get_pirates())
                if (c.lucky == False):
                    self.result["message"] = "Sorry captain, we could not catch the fish."
        elif (verb == "ignore"):
            print("Well, that's strange")
            self.go = False
        else:
            print ("Well, captain, we might regret not catching that fish, because our food is really low")
            self.go = True

    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "default message"

        while (self.go == False):
            print (" Praise lord, we have a fish, what's your command captain?")
            Player.get_interaction ([self])

        return self.result
