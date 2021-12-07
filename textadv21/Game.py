# CSC 221 & CTS 285
# Text Adventure
# Robert Land
# 12/6/21

from Room import Room
from Player import Player
import random as rand
"""
Version history:
    v1 - built using Room references (basically a graph). 
        downside: you have to create all rooms, then link
        them together afterwards.
    v2 - used constant room IDs to make it possible to add
        and link rooms in one pass. 
        downside: "this looks like BASIC" (from the peanut gallery)
    v3 - realization: if the Room names are unique, that's a
        unique ID. I therefore changed
        the container for all Rooms to be a dictionary --
        now it's easy enough to look up the room by name.
"""
class Game: 
    """
    The Game class organizes all game data in a central location.
    Usage:
    - Set up game using your choice of room configurations
    - call loop()
    """
    def __init__(self):
        """ Initialize object (with no rooms) """
        self.rooms = { } # stored in dictionary
        # Player is currently used to hold current location (loc)
        self.player = Player() 
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
        self.win = False
        self.victoryRoom = None
        self.openRoom = None
        self.escapeOpen = False
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def output(self, message):
        """ output the message. Just uses print() in base class.
        You might for example subclass to use Flask, etc. """
        print(message)
    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        while self.isPlaying:
            if self.win == False:
                self.playerAction()
            else:
                print("You've escaped!")
                self.isPlaying = False
        print("Game over, thanks for playing")
    def end(self):
        """ finish game, inform user of score and turns played. """
        print("Congratulations, dead or alive, you escaped the station!")
    def playerAction(self):
        """ Ask user for input, validate it, update the game state. """
        command = input(">")
        command = command.lower()
        words = command.split() # split on whitespace
        if len(words) < 1:
            print("No input detected")
            return
        verb = words[0]
        if verb == "go":
            direction = words[1]
            self.commandGo(direction)    
        elif verb == "look":
            self.here.describe()
        elif verb == "quit":
            self.isPlaying = False
            print("quitting")
        elif verb == "get":
            item = words[1]
            self.commandGet(item)
        elif verb == "drop":
            item = words[1]
            self.commandDrop(item)
        else: # first word is verb
            print("I don't know how to", words[0])
    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: none
        side effect: player location is updated if possible.
        """
        # special case - you can't go fore from start room
        # (to the victory room) unless escapeOpen is True
        #print("@@@", self.here.name)
        if self.here.name == "Escape Hall": 
            if direction == "fore" or direction == "Fore":
                print("You step towards the escape craft...")
                #print("@@@escape open?", self.escapeOpen)
                if self.escapeOpen != True:
                    print("You must find a way to open this first...")
                    return
                else:
                    print("And you reach it.")
        if self.here.name == "Escape Pod 1 Launched":
            print("You sit in the seat.")
            deathLaunch = rand.randint(1,2)
            #print("@#@#@",deathLaunch)
            if deathLaunch == 1:
                print("The escape pod explodes as you launch from the station.")
                print("You died.")
                self.win = False
                self.isPlaying = False
                return
            if deathLaunch ==2:
                print("You have escaped the station through an escape pod.")
                self.win = True
                return
        if self.here.name == "Escape Pod 2 Launched":
            print("You sit in the seat.")
            deathLaunch = rand.randint(1,2)
            #print("@#@#@",deathLaunch)
            if deathLaunch == 1:
                print("The escape pod explodes as you launch from the station.")
                print("You died.")
                self.win = False
                self.isPlaying = False
                return
            if deathLaunch ==2:
                print("You have escaped the station through an escape pod.")
                self.win = True
                return
        # Can we go in the chosen direction from here?
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        else:   
            # this key does exist
            newRoomName = self.here.exits[direction]
            newRoom     = self.rooms[newRoomName]
            self.here   = newRoom
            if self.isVerbose:
                self.here.describe()
            if self.here == self.openRoom:
                #print("@@@ The escape mode is now active.")
                self.escapeOpen = True
            if self.here == self.victoryRoom:
                self.win = True    
    @property
    def here(self):
        return self.player.loc
    
    @here.setter
    def here(self, room):
        self.player.loc = room

def main():
    game = Game()
    game.setup()
    print("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()
