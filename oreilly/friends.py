from operator import or_
from functools import reduce


class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection in self.connections:
            return False

        self.connections.append(connection)
        return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True

        return False

    def names(self):
        return reduce(or_, self.connections, set())

    def connected(self, name):
        my_connections = (connection for connection in self.connections
                          if name in connection)
        return reduce(or_, my_connections, set()) - {name}
