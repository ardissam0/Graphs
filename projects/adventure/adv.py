from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#reverse the direction
oposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}


# UPER:
# set up directions for plater to follow
# loop through all exits
# set up visited rooms to turn around
# if the room has not been visited then add to new path
# update using recursion
# return path
# fill the traversal path with bfs function

def bfs(starting_room, visited=set()):
    # track new path
    path =[]

    # loop through exits
    # use get exits in room.py
    for direction in player.current_room.get_exits():
        player.travel(direction)
        # if the player is in visited room
        if player.current_room in visited:
            # then turn to another direction
            player.travel(oposite_directions[direction])
        # otherwise if it has not been visited
        else:
            # add to new path
            visited.add(player.current_room)
            path.append(direction)
            # update using recursion
            path = path + bfs(player.current_room, visited)
            player.travel(oposite_directions[direction])
            path.append(oposite_directions[direction])
    # return the path
    return path

#fill in list with bfs current position
traversal_path = bfs(player.current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

# set a Queue for the bfs function
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self, value):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)