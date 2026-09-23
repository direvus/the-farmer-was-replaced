from __builtins__ import *

DIRECTIONS = (North, East, South, West)
OPPOSITE = {North: South, East: West, South: North, West: East}
VECTORS = {
	North: (0, 1),
	East: (1, 0),
	West: (-1, 0),
	South: (0, -1)}

def water(target):
	if get_water() < target and num_items(Items.Water) > 0:
		use_item(Items.Water)
		
def do_harvest():
	# If there's something to harvest at the current location, harvest it.
	if can_harvest():
		harvest()
		
def do_plant(entity, ground):
	# Opportunistically harvest and then ensure the entity is planted.
	#
	# If there is something to harvest at the current location, first harvest
	# it.  Then, ensure that the ground type is correct for the desired
	# planting (till the ground if it isn't correct). Finally, plant the
	# desired entity if it's not already present.
	do_harvest()
	if get_ground_type() != ground:
		till()
	if get_entity_type() != entity:
		plant(entity)
		
def fertilise(entity, ground):
	do_plant(entity, ground)
	if num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
		while not can_harvest():
			do_a_flip()
		harvest()
		do_plant(entity, ground)
		
def reverse(direction):
	return OPPOSITE[direction]
	
def apply_vector(position, direction):
	x, y = position
	dx, dy = VECTORS[direction]
	return (x + dx, y + dy)

def get_rows():
	# Return the number of rows to be covered by each drone
	return get_world_size() // max_drones()

def get_distance(pos1, pos2):
    # Return Manhattan distance between two positions
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def go_to(x, y):
    dx = x - get_pos_x()
    dy = y - get_pos_y()

    if dx > 0:
        direction = East
    else:
        direction = West
    for _ in range(abs(dx)):
        move(direction)

    if dy > 0:
        direction = North
    else:
        direction = South
    for _ in range(abs(dy)):
        move(direction)

def sort(items, key):
    clean = False
    while not clean:
        clean = True
        for i in range(len(items) - 1):
            a = items[i]
            b = items[i + 1]

            if key(a) > key(b):
                clean = False
                items[i] = b
                items[i + 1] = a

