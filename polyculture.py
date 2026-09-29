import util


def is_in_bounds(min_x, min_y, rows, cols, pos):
	x, y = pos
	return (
			x >= min_x and y >= min_y and 
			x < min_x + cols and y < min_y + rows)
			

def run_drone(min_x, min_y, rows, cols):
	x = min_x + (cols // 2)
	y = min_y + (rows // 2)
	util.go_to(x, y)
	util.do_plant(Entities.Carrot)
	util.water(1.0)
	cells = [(x, y)]
	
	while True:
		entity, location = get_companion()
		if not is_in_bounds(min_x, min_y, rows, cols, location):
			break
		if location in cells:
			break
			
		util.go_to_pos(location)
		util.do_plant(entity)
		util.water(1.0)
		cells.append(location)
	
	while len(cells) > 0:
		location = cells.pop(0)
		util.go_to_pos(location)
		while not can_harvest():
			do_a_flip()
		harvest()