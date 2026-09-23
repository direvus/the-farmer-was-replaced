import util

SIZE = get_world_size()

def get_substance_count(size):
	return size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	
def is_in_bounds(position):
	x, y = position
	return (x >= 0 and y >= 0 and x < SIZE and y < SIZE)
	
def get_neighbours():
	x = get_pos_x()
	y = get_pos_y()
	result = {}
	for d in util.DIRECTIONS:
		target = util.apply_vector((x, y), d)
		if is_in_bounds(target):
			result[d] = target
	return result
	
def run_drone(size, row):
	util.go_to(0, row)
	start(size)

def start(size):
	count = get_substance_count(size)
	harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, count)
	run()

def run():
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
	
def dist_key(item):
	return item[2]

def explore(visited):
	n = get_neighbours()
	targets = []
	dest = measure()
	if dest == None:
		return
	for d in n:
		pos = n[d]
		if pos in visited:
			continue
		dist = util.get_distance(pos, dest)
		targets.append((d, pos, dist))
	util.sort(targets, dist_key)

	for target in targets:
		if get_entity_type() != Entities.Hedge:
			return
		direction = target[0]
		moved = advance(direction, visited)
		if moved:
			move(util.reverse(direction))
		
	
