from game_message import Tick, Action, Spawn, Sail, Dock, Anchor, directions


class Bot:
    def __init__(self):
        print("Initializing your super mega duper bot")

    def get_next_move(self, tick: Tick) -> Action:
        """
        Here is where the magic happens, for now the move is random. I bet you can do better ;)
        """
        if tick.currentLocation is None:
            # If the current location is null, that means that we have to spawn.
            return Spawn(tick.map.ports[0])

        # Si on est a un port et que nous sommes pas au
        if (tick.currentLocation in tick.map.ports) and (tick.currentTick != tick.totalTicks):
            return Anchor()

        closestPort = tick.map.ports[1]
        # Calculates the closest port without any regards to topology or water level
        for port in tick.map.ports[2:]:
            if (map.ports.index(port) not in tick.visitedPortIndices) and (abs(tick.currentLocation['row'] - port['row']) + abs(tick.currentLocation['column'] - port['column']) < abs(tick.currentLocation['row'] - closestPort['row']) + abs(tick.currentLocation['column'] - closestPort['column'])):
                closestPort = port

        nextTicks = []
        for i in directions:  # Calculer le parcours le plus rapide vers le port en fonction de la topologie et des marees, mettre ce parcours dans une liste qui sera accessible aux coups suivants
            x = 1

        # return Sail()
