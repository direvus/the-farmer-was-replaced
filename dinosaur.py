import util


def wait_for_apple_affordable():
	while not util.is_affordable(Entities.Apple):
		do_a_flip()
		
		
def is_in_bounds(min_x, min_y, rows, cols, pos):
	x, y = pos
	return (
			x >= min_x and y >= min_y and 
			x < min_x + cols and y < min_y + rows)


def get_neighbours(min_x, min_y, rows, cols, pos):
	x, y = pos
	directions = set()
	if x > min_x:
		directions.add(West)
	if y > min_y:
		directions.add(South)
	if x < min_x + cols - 1:
		directions.add(East)
	if y < min_y + rows - 1:
		directions.add(North)
	return directions
	

def distance_key(target):
	return target[2]
	
	
def find_path(bounds, dest, visited, tail):
	min_x, min_y, rows, cols = bounds
	
	pos = visited[len(visited) - 1]
	directions = get_neighbours(min_x, min_y, rows, cols, pos)
	targets = []
	for d in directions:
		t = util.apply_vector(pos, d)
		if t in visited or t in tail:
			continue
		if t == dest:
			return [d]
		p = util.get_distance(t, dest)
		targets.append((d, t, p))
	if len(targets) == 0:
		return None

	if len(tail) > 0:
		tail.pop()
	tail.insert(0, pos)

	util.sort(targets, distance_key)
	for target in targets:
		v = list(visited)
		v.append(target[1])
		path = find_path(bounds, dest, v, tail)
		if path:
			path.insert(0, target[0])
			return path
	return None

	
def run_drone(min_x, min_y, rows, cols):
	bounds = (min_x, min_y, rows, cols)
	wait_for_apple_affordable()
	change_hat(Hats.Dinosaur_Hat)
	if get_entity_type() != Entities.Apple:
		change_hat(Hats.Gray_Hat)
		return
	pos = util.get_pos()	
	tail = []
	while True:
		wait_for_apple_affordable()
		dest = measure()
		if not (dest and is_in_bounds(min_x, min_y, rows, cols, dest)):
			change_hat(Hats.Gray_Hat)
			return

		pos = util.get_pos()
		path = find_path(bounds, dest, [pos], tail)
		if path:
			for direction in path:
				move(direction)
		else:
			change_hat(Hats.Gray_Hat)
			return

		
	
	