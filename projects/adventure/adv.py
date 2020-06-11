from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

opposite_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}
starting_room = player.current_room
visited = {}  # dictionary
# print(len(world.rooms))
previous_directions = [None]
curr_room = starting_room
previous_room = None 
next_direction = None

while len(visited) < len(world.rooms): 
	# put current room in visited  with empty routes
	print("start", curr_room)
	if curr_room.id not in visited:
		curr_exits = curr_room.get_exits()
		exits = {}
		# build up current visited dictionary with exits not visited
		# visited[curr_room.id] = {"n": "?", "s": "?", "w": "?", "e": "?"}
		for ext in curr_exits:
			exits[ext] = "?"
			visited[curr_room.id] = exits
			
	print("visited:", visited)
	# While number of rooms visited not = to all rooms

	# check if current room have any exits
	for direction in curr_exits:
		# check if the visited room have any unvisited exits
		if visited[curr_room.id][direction] == "?":
			player.travel(direction)
			traversal_path.append(direction)
			next_direction = direction
			previous_room = curr_room
			curr_room = player.current_room # set current room to new room
			
			# update visited
			exits = {}
			for ext in curr_room.get_exits():
				exits[ext] = "?"
				visited[curr_room.id] = exits

			visited[previous_room.id][direction] = curr_room.id # set previous room direction to new room
			visited[curr_room.id][opposite_directions[direction]] = previous_room.id #set new room direction to old room

	print("next direction:",next_direction)
	print("curr_room", curr_room)
	print("new visited:", visited)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
	player.travel(move)
	visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
	print(
		f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
	)
else:
	print("TESTS FAILED: INCOMPLETE TRAVERSAL")
	print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")