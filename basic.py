import util


def run_cell():
	# Farm diagonal rows of trees, carrots and grass
	x = get_pos_x()
	y = get_pos_y()
	diagonal = (x - y) % 3

	if diagonal == 0:
		util.do_plant(Entities.Tree, Grounds.Grassland)
		util.water(0.6)
	elif diagonal == 1:
		util.do_plant(Entities.Carrot, Grounds.Soil)
		util.water(0.6)
	elif diagonal == 2:
		util.fertilise(Entities.Grass, Grounds.Grassland)
