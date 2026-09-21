import maze
import pumpkins
import tech

change_hat(Hats.Purple_Hat)
COUNT = maze.get_substance_count()

clear()
while True:
	# unlock anything that is available to unlock
	tech.unlock_all()
	
	# run the maze once, if we've got the substance for it
	if num_items(Items.Weird_Substance) > COUNT:
		maze.run()

	# run the pumpkin farm until we succeed in harvesting the mega pumpkin
	while not pumpkins.run():
		pass