TARGETS = (
	Unlocks.Speed,
	Unlocks.Grass,
	Unlocks.Expand,
	Unlocks.Carrots,
	Unlocks.Watering,
	Unlocks.Trees,
	Unlocks.Fertilizer,
	Unlocks.Pumpkins,
	Unlocks.Simulation,
	Unlocks.Mazes,
	Unlocks.Cactus,
	Unlocks.Polyculture,
	Unlocks.Leaderboard,
	Unlocks.Top_Hat,
	Unlocks.Megafarm,
	Unlocks.Dinosaurs)

def unlock_all():
	for target in TARGETS:
		try_unlock(target)
	
def try_unlock(target):
	costs = get_cost(target)
	for item in costs:
		if num_items(item) < costs[item]:
			return False
	unlock(target)
	return True