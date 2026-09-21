from __builtins__ import *
import util
import maze

SIZE = get_world_size()
PUMPKIN_SIZE = 6
	
def run_cell():
    if get_entity_type() == Entities.Hedge:
        maze.run()

    x = get_pos_x()
    y = get_pos_y()
    if x < PUMPKIN_SIZE and y < PUMPKIN_SIZE:
        if get_entity_type() != Entities.Pumpkin:
            util.do_plant(Entities.Pumpkin, Grounds.Soil)
        util.water(0.6)
        if (x == PUMPKIN_SIZE - 1 and y == PUMPKIN_SIZE - 1 and can_harvest()):
            util.do_plant(Entities.Pumpkin, Grounds.Soil)
    else:
                
        diagonal = (x - y) % 3
        if diagonal == 0:
            util.do_plant(Entities.Tree, Grounds.Grassland)
            util.water(0.6)
        elif diagonal == 1:
            util.do_plant(Entities.Carrot, Grounds.Soil)
            util.water(0.6)
        elif diagonal == 2:
            util.fertilise(Entities.Grass, Grounds.Grassland)
    move(East)

def run_drone():
    rows = util.get_rows()
    for y in range(rows):
        for x in range(SIZE):
            run_cell()
        move(North)
    for y in range(rows):
        move(South)


def run():
	mega_pumpkin = True
	result = False
	max_sunflower = 0
	for x in range(SIZE):
		for y in range(SIZE):
            run_cell()
		move(North)
	return result
