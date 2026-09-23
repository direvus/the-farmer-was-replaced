from __builtins__ import *
import basic
import maze
import util

SIZE = get_world_size()
PUMPKIN_SIZE = 6
	

def run_cell():
	x = get_pos_x()
	y = get_pos_y()
	if x < PUMPKIN_SIZE and y < PUMPKIN_SIZE:
		if get_entity_type() != Entities.Pumpkin:
			util.do_plant(Entities.Pumpkin, Grounds.Soil)
		util.water(0.6)
		if (x == PUMPKIN_SIZE - 1 and y == PUMPKIN_SIZE - 1 and can_harvest()):
			util.do_plant(Entities.Pumpkin, Grounds.Soil)
	else:
		basic.run_cell()
	move(East)


def run_drone(rows, cols):
	start_x = get_pos_x()
	start_y = get_pos_y()
	for y in range(rows):
		for x in range(cols):
			run_cell()
		util.go_to(start_x, get_pos_y() + 1)
	util.go_to(start_x, start_y)


def run():
	mega_pumpkin = True
	result = False
	update_max_petals()
	for x in range(SIZE):
		for y in range(SIZE):
			run_cell()
		move(North)
	return result
