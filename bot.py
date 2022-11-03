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
            print(f"Spawn at {tick.map.ports[0]}")
            return Spawn(tick.map.ports[0])

        # Si on est a un port et que nous sommes pas au
        if (tick.currentLocation in tick.map.ports):
            if (tick.map.ports.index(tick.currentLocation) not in tick.visitedPortIndices):
                print(f"Dock at {tick.currentLocation}")
                return Dock()

        for port in tick.map.ports:
            if (tick.map.ports.index(port) not in tick.visitedPortIndices):
                closestPort = port
                break

        # closestPort = tick.map.ports[1]
        # Calculates the closest port without any regards to topology or water level
        # for port in tick.map.ports[2:]:
        #     if (tick.map.ports.index(port) not in tick.visitedPortIndices) and (abs(tick.currentLocation.row - port.row) + abs(tick.currentLocation.column - port.column) < abs(tick.currentLocation.row - closestPort.row) + abs(tick.currentLocation.column - closestPort.column)):
        #         closestPort = port
        #         print(
        #             f"Closest port at {closestPort.row}: {closestPort.column}")

# Sail direction

        if (tick.currentLocation.row < closestPort.row) and (tick.currentLocation.column < closestPort.column):
            # (+1, +1)
            # Si hauteur_terrain >= eau en SE de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column + 1]) >= tick.tideSchedule[0]:
                return Anchor()
            else:
                print("Sail SE")
                return Sail('SE')

        if (tick.currentLocation.row < closestPort.row) and (tick.currentLocation.column > closestPort.column):
            # (+1, -1)
            # Si hauteur_terrain >= eau en SW de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column - 1]) >= tick.tideSchedule[0]:
                return Anchor()
            else:
                print("Sail SW")
                return Sail('SW')

        if (tick.currentLocation.row > closestPort.row) and (tick.currentLocation.column < closestPort.column):
            # (-1, +1)
            # Si hauteur_terrain >= eau en NE de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column + 1]) >= tick.tideSchedule[0]:
                return Anchor()
            else:
                print("Sail NE")
                return Sail('NE')

        if (tick.currentLocation.row > closestPort.row) and (tick.currentLocation.column > closestPort.column):
            # (-1, -1)
            # Si hauteur_terrain >= eau en NW de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column - 1]) >= tick.tideSchedule[0]:
                return Anchor()
            else:
                print("Sail NW")
                return Sail('NW')

        if (tick.currentLocation.row < closestPort.row) and (tick.currentLocation.column == closestPort.column):
            # (+1, 0)
            # Si hauteur_terrain >= eau en S de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column]) >= tick.tideSchedule[0]:
                return Anchor()
            else:
                print("Sail S")
                return Sail('S')

        if (tick.currentLocation.row > closestPort.row) and (tick.currentLocation.column == closestPort.column):
            # (-1, 0)
            # Si hauteur_terrain >= eau en N de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column]) >= tick.tideSchedule[0]:
                return Anchor()
            else:
                print("Sail N")
                return Sail('N')

        if (tick.currentLocation.row == closestPort.row) and (tick.currentLocation.column < closestPort.column):
            # (0, +1)
            # Si hauteur_terrain >= eau en E de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column + 1]) >= tick.tideSchedule[0]:
                return Anchor()
            else:
                print("Sail E")
                return Sail('E')

        if (tick.currentLocation.row == closestPort.row) and (tick.currentLocation.column > closestPort.column):
            # (0, -1)
            # Si hauteur_terrain >= eau en W de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column - 1]) >= tick.tideSchedule[0]:
                return Anchor()
            else:
                print("Sail W")
                return Sail('W')
