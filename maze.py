from util import DIRECTIONS, reverse, apply_vector

SIZE = get_world_size()

def get_substance_count():
	return SIZE * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	
def is_in_bounds(position):
	x, y = position
	return (x >= 0 and y >= 0 and x < SIZE and y < SIZE)
	
def get_neighbours():
	x = get_pos_x()
	y = get_pos_y()
	result = {}
	for d in DIRECTIONS:
		target = apply_vector((x, y), d)
		if is_in_bounds(target):
			result[d] = target
	return result
	
def run():
	count = get_substance_count()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, count)
	
	dest = measure()
	pos = (get_pos_x(), get_pos_y())
	visited = {pos}
	explore(visited)
	
def advance(direction, visited):	
	if not move(direction):
		return False
	pos = (get_pos_x(), get_pos_y())
	visited.add(pos)
	
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
		
	explore(visited)
	return True
	
def explore(visited):
	n = get_neighbours()
	for d in n:
		if get_entity_type() != Entities.Hedge:
			return
		if n[d] in visited:
			continue
		moved = advance(d, visited)
		if moved:
			move(reverse(d))
		
	