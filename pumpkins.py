from __builtins__ import *
import util
import maze

SIZE = get_world_size()
PUMPKIN_SIZE = 6
	
sunflowers = {}
max_petals = 0


def update_max_petals():
    global sunflowers
    global max_petals
    max_petals = 0
    for pos in sunflowers:
        max_petals = max(max_petals, sunflowers[pos])
    return max_petals


def run_cell():
    global sunflowers
    global max_petals

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
    elif SIZE >= 10 and y >= SIZE - 2 and x < 10:
        petals = measure()
        if get_entity_type() != Entities.Sunflower:
            util.do_plant(Entities.Sunflower, Grounds.Soil)
            petals = measure()
            sunflowers[(x, y)] = petals
            update_max_petals()

        if petals >= max_petals and can_harvest():
            harvest()
            plant(Entities.Sunflower)
            petals = measure()
            sunflowers[(x, y)] = petals
            update_max_petals()

        if petals > max_petals:
            max_petals = petals
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
    update_max_petals()
    for y in range(rows):
        for x in range(SIZE):
            run_cell()
        move(North)
    for y in range(rows):
        move(South)


def run():
	mega_pumpkin = True
	result = False
    update_max_petals()
	for x in range(SIZE):
		for y in range(SIZE):
            run_cell()
		move(North)
	return result
