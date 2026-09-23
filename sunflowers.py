import util


def get_max_petals(flowers):
    result = 0
    for k in flowers:
        result = max(result, flowers[k])
    return result


def run_cell(flowers):
    max_petals = get_max_petals(flowers)
    petals = measure()
    p = util.get_pos()
    if get_entity_type() != Entities.Sunflower:
        util.do_plant(Entities.Sunflower, Grounds.Soil)
        util.water(1.0)
        petals = measure()
        flowers[p] = petals
        max_petals = get_max_petals(flowers)

    if petals >= max_petals and can_harvest():
        harvest()
        plant(Entities.Sunflower)
        util.water(1.0)
        petals = measure()
        flowers[p] = petals
        max_petals = get_max_petals(flowers)

    return flowers


def run_drone(rows, cols, flowers):
	start_x = get_pos_x()
	start_y = get_pos_y()
    if len(flowers) < rows * cols:
        for y in range(rows):
            for x in range(cols):
                flowers = run_cell(flowers)
                move(East)
            util.go_to(start_x, get_pos_y() + 1)
    else:
        max_petals = get_max_petals(flowers)
        for pos in flowers:
            if flowers[pos] == max_petals:
                util.go_to(pos[0], pos[1])
                run_cell(flowers)

    util.go_to(start_x, start_y)
    return flowers


def run():
	mega_pumpkin = True
	result = False
	update_max_petals()
	for x in range(SIZE):
		for y in range(SIZE):
			run_cell()
		move(North)
	return result
