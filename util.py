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
	if can_harvest():
		harvest()
		
def do_plant(entity, ground):
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
