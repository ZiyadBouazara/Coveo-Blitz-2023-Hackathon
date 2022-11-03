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

        # Si le premier port et dernier port sont les memes, la partie est fini
        # if (tick.visitedPortIndices[0] == tick.visitedPortIndices.pop()) and (len(tick.visitedPortIndices) > 1):
        #     tick.isOver = True
        #     return tick.isOver

        # Si tout les ports ont ete visite, on retourn au spawn port
        if (len(tick.visitedPortIndices) == len(tick.map.ports)):
            closestPort == tick.spawnLocation

        # Si on est a un port et qu'il n'a pas encore ete visite OU que on est au port du spawn et que le nombre de ports visite n'est pas nul (i.e. pas au debut de la partie)
        if (tick.currentLocation in tick.map.ports):
            if (tick.map.ports.index(tick.currentLocation) not in tick.visitedPortIndices) or ((tick.currentLocation == tick.spawnLocation) and (len(tick.visitedPortIndices) > 1)):
                print(f"Dock at {tick.currentLocation}")
                return Dock()

        # for port in tick.map.ports:
        #     if (tick.map.ports.index(port) not in tick.visitedPortIndices):
        #         closestPort = port
        #         break

        #closestPort = tick.map.ports[1]
        # Calculates the closest port without any regards to topology or water level
        for port in tick.map.ports[1:]:
            if (tick.map.ports.index(port) not in tick.visitedPortIndices) and ((abs(tick.currentLocation.row - port.row) + abs(tick.currentLocation.column - port.column)) < (abs(tick.currentLocation.row - closestPort.row) + abs(tick.currentLocation.column - closestPort.column))):
                closestPort = port
                print(
                    f"Closest port at {closestPort.row}: {closestPort.column}")

# Sail direction

        if (tick.currentLocation.row < closestPort.row) and (tick.currentLocation.column < closestPort.column):
            # (+1, +1)
            # Si hauteur_terrain >= eau en SE de currentLoc
            if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column + 1]) >= tick.tideSchedule[0]:

                # TEST SI E est clear, si oui, sail E
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('E')
                # TEST SI S est clear, si oui, sail S
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('S')
                # TEST SI NE est clear, si oui, sail NE
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('NE')
                # TEST SI SW est clear, si oui, sail SW
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('SW')
                # TEST SI N est clear, si oui, sail N
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('N')
                # TEST SI W est clear, si oui, sail W
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('W')
                # TEST SI NW est clear, si oui, sail NW
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('NW')
                else:  # on est donc dans un cul-de-sac, donc anchor
                    return Anchor()

            else:
                print("Sail SE")
                return Sail('SE')

        if (tick.currentLocation.row < closestPort.row) and (tick.currentLocation.column > closestPort.column):
            # (+1, -1)
            # Si hauteur_terrain >= eau en SW de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column - 1]) >= tick.tideSchedule[0]:

                # TEST SI W est clear, si oui, sail W
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('W')
                # TEST SI S est clear, si oui, sail S
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('S')
                # TEST SI NW est clear, si oui, sail NW
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('NW')
                # TEST SI SE est clear, si oui, sail SE
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('SE')
                # TEST SI N est clear, si oui, sail N
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('N')
                # TEST SI E est clear, si oui, sail E
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('E')
                # TEST SI NE est clear, si oui, sail NE
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('NE')
                else:
                    return Anchor()

            else:
                print("Sail SW")
                return Sail('SW')

        if (tick.currentLocation.row > closestPort.row) and (tick.currentLocation.column < closestPort.column):
            # (-1, +1)
            # Si hauteur_terrain >= eau en NE de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column + 1]) >= tick.tideSchedule[0]:

                # TEST SI N est clear, si oui, sail N
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('N')
                # TEST SI E est clear, si oui, sail E
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('E')
                # TEST SI SE est clear, si oui, sail SE
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('SE')
                # TEST SI NW est clear, si oui, sail NW
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('NW')
                # TEST SI W est clear, si oui, sail W
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('W')
                # TEST SI S est clear, si oui, sail S
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('S')
                # TEST SI SW est clear, si oui, sail SW
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('SW')
                else:
                    return Anchor()

            else:
                print("Sail NE")
                return Sail('NE')

        if (tick.currentLocation.row > closestPort.row) and (tick.currentLocation.column > closestPort.column):
            # (-1, -1)
            # Si hauteur_terrain >= eau en NW de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column - 1]) >= tick.tideSchedule[0]:

                # TEST SI N est clear, si oui, sail N
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('N')
                # TEST SI W est clear, si oui, sail W
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('W')
                # TEST SI SW est clear, si oui, sail SW
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('SW')
                # TEST SI NE est clear, si oui, sail NE
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('NE')
                # TEST SI E est clear, si oui, sail E
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('E')
                # TEST SI S est clear, si oui, sail S
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('S')
                # TEST SI SE est clear, si oui, sail SE
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('SE')
                else:
                    return Anchor()

            else:
                print("Sail NW")
                return Sail('NW')

        if (tick.currentLocation.row < closestPort.row) and (tick.currentLocation.column == closestPort.column):
            # (+1, 0)
            # Si hauteur_terrain >= eau en S de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column]) >= tick.tideSchedule[0]:

                # TEST SI SE est clear, si oui, sail SE
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('SE')
                # TEST SI SW est clear, si oui, sail SW
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('SW')
                # TEST SI W est clear, si oui, sail W
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('W')
                # TEST SI E est clear, si oui, sail E
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('E')
                # TEST SI NE est clear, si oui, sail NE
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('NE')
                # TEST SI NW est clear, si oui, sail NW
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('NW')
                # TEST SI N est clear, si oui, sail N
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('N')
                else:
                    return Anchor()

            else:
                print("Sail S")
                return Sail('S')

        if (tick.currentLocation.row > closestPort.row) and (tick.currentLocation.column == closestPort.column):
            # (-1, 0)
            # Si hauteur_terrain >= eau en N de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column]) >= tick.tideSchedule[0]:

                # TEST SI NE est clear, si oui, sail NE
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('NE')
                # TEST SI NW est clear, si oui, sail NW
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('NW')
                # TEST SI W est clear, si oui, sail W
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('W')
                # TEST SI E est clear, si oui, sail E
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('E')
                # TEST SI SE est clear, si oui, sail SE
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('SE')
                # TEST SI SW est clear, si oui, sail SW
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('SW')
                # TEST SI S est clear, si oui, sail S
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('S')
                else:
                    return Anchor()

            else:
                print("Sail N")
                return Sail('N')

        if (tick.currentLocation.row == closestPort.row) and (tick.currentLocation.column < closestPort.column):
            # (0, +1)
            # Si hauteur_terrain >= eau en E de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column + 1]) >= tick.tideSchedule[0]:

                # TEST SI NE est clear, si oui, sail NE
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('NE')
                # TEST SI SE est clear, si oui, sail SE
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('SE')
                # TEST SI S est clear, si oui, sail S
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('S')
                # TEST SI N est clear, si oui, sail N
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('N')
                # TEST SI NW est clear, si oui, sail NW
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('NW')
                # TEST SI SW est clear, si oui, sail SW
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('SW')
                # TEST SI W est clear, si oui, sail W
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('W')
                else:
                    return Anchor()

            else:
                print("Sail E")
                return Sail('E')

        if (tick.currentLocation.row == closestPort.row) and (tick.currentLocation.column > closestPort.column):
            # (0, -1)
            # Si hauteur_terrain >= eau en W de currentLoc -> ANCHOR
            if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column - 1]) >= tick.tideSchedule[0]:

                # TEST SI NW est clear, si oui, sail NW
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('NW')
                # TEST SI SW est clear, si oui, sail SW
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column - 1]) < tick.tideSchedule[0]:
                    return Sail('SW')
                # TEST SI S est clear, si oui, sail S
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('S')
                # TEST SI N est clear, si oui, sail N
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column]) < tick.tideSchedule[0]:
                    return Sail('N')
                # TEST SI NE est clear, si oui, sail NE
                if (tick.map.topology[tick.currentLocation.row - 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('NE')
                # TEST SI SE est clear, si oui, sail SE
                if (tick.map.topology[tick.currentLocation.row + 1][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('SE')
                # TEST SI E est clear, si oui, sail E
                if (tick.map.topology[tick.currentLocation.row][tick.currentLocation.column + 1]) < tick.tideSchedule[0]:
                    return Sail('E')
                else:
                    return Anchor()

            else:
                print("Sail W")
                return Sail('W')
