from util import (water, do_harvest, do_plant, fertilise)

SIZE = get_world_size()
PUMPKIN_SIZE = 5
	
def run_row():
	pass
	
def run():
	mega_pumpkin = True
	result = False
	max_sunflower = 0
	for x in range(SIZE):
		for y in range(SIZE):
			if x < PUMPKIN_SIZE and y < PUMPKIN_SIZE:
				if get_entity_type() != Entities.Pumpkin:
					do_plant(Entities.Pumpkin, Grounds.Soil)
					mega_pumpkin = False
				water(0.6)
				if (x == PUMPKIN_SIZE - 1 and y == PUMPKIN_SIZE - 1 and
					mega_pumpkin and can_harvest()):
					do_plant(Entities.Pumpkin, Grounds.Soil)
					result = True
			else:
						
				diagonal = (x - y) % 4
				if diagonal == 0:
					do_plant(Entities.Tree, Grounds.Grassland)
					water(0.6)
				elif diagonal == 1:
					do_plant(Entities.Carrot, Grounds.Soil)
					water(0.6)
				elif diagonal == 2:
					fertilise(Entities.Grass, Grounds.Grassland)
				elif diagonal == 3:
					if get_entity_type() != Entities.Sunflower:
						do_plant(Entities.Sunflower, Grounds.Soil)
					petals = measure()
					if can_harvest() and petals >= max_sunflower:
						harvest()
						plant(Entities.Sunflower)
						petals = measure()
					if petals and petals > max_sunflower:
						max_sunflower = petals
					
			move(East)
		move(North)
	return result