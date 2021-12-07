# CSC 221 & CTS 285
# Text Adventure
# Robert Land
# 12/6/21
# MyGame - implements game specific functions
from Game import Game
from Room import Room
from Player import Player
class MyGame(Game):    
    """ the Game class should be subclassed to add
    game specific features, including the world setup. 
    """
    def setup(self):
        """ Load your own rooms in the method of your choosing.
        Consider a GameLoader class that might read these
        from a file...
        """
        loader = MyGameLoader()
        self.rooms, self.victoryRoom, self.openRoom, self.escP1C, \
            self.escP2C = loader.setup()
        # starting location
        self.here = self.rooms["Cryo Room"]
        # Let's do a turn 1 look , to orient the player
        self.here.describe()
class MyGameLoader:
    """ just used to put all the room setup in a separate class,
    and if needed, a separate file.""" 
    def setup(self):
        ''' Relic Code. Unused.
        winHall1 = Room( "Escape Hall", 
                        "This is an average corridor, arrivals and exits are found through the fore doors.",
                        { "aft": "Cryo Room",
                          "port": "Corridor Port",
                          "starboard": "Corridor Starboard"} )
        '''
        winHall2 = Room( "Escape Hall", 
                        "This is an average corridor, arrivals and exits are found through the fore doors.",
                        { "fore": "Escape Access",
                          "aft": "Cryo Room",
                          "port": "Corridor Port",
                          "starboard": "Corridor Starboard"} )
        startRoom = Room ( "Cryo Room",
                           "A number of pods are here, with the occupants missing and you've recently awoken. The station sirens and emergency lights are on.",
                           { "fore" : "Escape Hall"} )
        
        portCorr = Room ( "Corridor Port", 
                         "This corridor runs on the port side of the station. It curves around the cryo bay.",
                         { "fore" : "Escape Hall",
                          "aft" : "Aft Corridor",
                          "port": "Exterior Port Corridor"} )
        starCorr = Room ( "Corridor Starboard", 
                         "This corridor runs on the starboard side of the station. It curves around the cryo bay. The lights are flickering and the view glass is cracked. "\
                             "\nThe maintenance hatch is damaged, but functional; Passage into the starboard maintenance is possible.",
                         { "fore" : "Escape Hall",
                          "aft" : "Aft Corridor",
                          "starboard":"Exterior Starboard Corridor"} )
        aftCorr = Room ( "Aft Corridor",
                        "This corridor curves along the aft half of the station, a door is left open further aft.",
                        {"port": "Corridor Port",
                         "starboard": "Corridor Starboard",
                         "aft":"Open Room"})
        openRoom = Room ("Open Room",
                        "A sensor beeps and flashes as you enter. The room is dark, and empty.",
                        {"fore": "Aft Corridor"})
        
        victoryRoom = Room ("Escape Access",
                            "Come on then, leave! You're right there!",
                            {"fore": "Escape Ship"})
        extPortRoom = Room ("Exterior Port Corridor",
                            "This corridor runs along the internal hull plating of the station, a maintenance access, of sorts.",
                            {"starboard":"Corridor Port",
                             "aft":"Escape Pod 1 Launched"})
        extStarRoom = Room("Exterior Starboard Corridor",
                            "This corridor runs along the internal hull plating of the station, a maintenance access, of sorts.",
                            {"port":"Corridor Port",
                             "aft":"Escape Pod 2 Launched"})
        escP1 = Room("Escape Pod 1",
                     "This rickety escape pod has seen better days, are you sure you want to risk it?",
                     {"aft":"Escape Pod 1 Launched",
                      "fore":"Exterior Port Corridor"})
        escP2 = Room("Escape Pod 2",
                     "This rickety escape pod has seen better days, are you sure you want to risk it?",
                     {"aft":"Escape Pod 2 Launched",
                      "fore":"Exterior Starboard Corridor"})
            
        escP1C = Room("Escape Pod 1 Launched",
                     "Good luck. The door closed behind you and the window quickly goes from the pod's station to the exterior of the station.",
                     {"aft":"Escape Pod 1 Launched",
                      "fore":"Escape Pod 1 Launched",
                      "port":"Escape Pod 1 Launched",
                      "starboard":"Escape Pod 1 Launched"})
        escP2C = Room("Escape Pod 2 Launched",
                      "Good luck. The door closed behind you and the window quickly goes from the pod's station to the exterior of the station.",
                      {"aft":"Escape Pod 2 Launched",
                      "fore":"Escape Pod 2 Launched",
                      "port":"Escape Pod 2 Launched",
                      "starboard":"Escape Pod 2 Launched"})
        rooms = { winHall2.name: winHall2, 
                    startRoom.name: startRoom,
                    portCorr.name: portCorr,
                    starCorr.name: starCorr,
                    aftCorr.name: aftCorr,
                    openRoom.name: openRoom,
                    victoryRoom.name: victoryRoom,
                    extPortRoom.name: extPortRoom,
                    escP1.name: escP1,
                    escP1C.name: escP1C,
                    escP2.name: escP2,
                    escP2C.name: escP2C,
                    extStarRoom.name: extStarRoom}
        self.escP1C = escP1C
        self.victoryRoom = victoryRoom
        self.openRoom = openRoom
        #if Room == victoryRoom:
           # self.win = True       
        '''
        if self.escapeOpen == True:
            rooms.update({ winHall2.name: winHall2, 
                    startRoom.name: startRoom,
                    portCorr.name: portCorr,
                    starCorr.name: starCorr,
                    aftCorr.name: aftCorr,
                    openRoom.name: openRoom,
                    victoryRoom.name: victoryRoom})
        '''
        return rooms, victoryRoom, openRoom, escP1C, escP2C
# Startup
def main():
    game = MyGame()
    game.setup()
    game.output("Starting game -- enter command.")
    game.loop()
    game.end()
if __name__ == "__main__":
    main()

