import util

def get_neighbours(start_x, start_y, rows, cols):
	directions = {North, East}
	x = get_pos_x()
	y = get_pos_y()
	
	if x >= start_x + cols - 1:
		directions.remove(East)
	if y >= start_y + rows - 1:
		directions.remove(North)
	
	return directions
	
	
def run_drone(rows, cols):
	start_x = get_pos_x()
	start_y = get_pos_y()
	
	for y in range(rows):
		for x in range(cols):
			if get_entity_type() != Entities.Cactus:
				util.do_plant(Entities.Cactus, Grounds.Soil)
			if x < cols - 1:
				move(East)
		if y < rows - 1:
			util.go_to(start_x, start_y + y + 1)
				
	util.go_to(start_x, start_y)
	
	swapped = True
	while swapped:
		swapped = False
		for y in range(rows):
			for x in range(cols):
				size = measure()
				n = get_neighbours(start_x, start_y, rows, cols)
				for d in n:
					other = measure(d)
					if other < size:
						swap(d)
						swapped = True
						break
				if x < cols - 1:
					move(East)
			if y < rows - 1:
				util.go_to(start_x, start_y + y + 1)
		util.go_to(start_x, start_y)
		
	while not can_harvest():
		do_a_flip()
	harvest()