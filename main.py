from __builtins__ import *
import maze
import pumpkins
import tech
import util
import sunflowers

SIZE = get_world_size()
HATS = (
		Hats.Brown_Hat,
		Hats.Gold_Hat,
		Hats.Green_Hat,
		Hats.Gray_Hat,
		Hats.Purple_Hat,
		Hats.Straw_Hat,
		Hats.Traffic_Cone,
		)


def run_maze():
	change_hat(Hats.Gold_Hat)
	while True:
		maze.run_drone(10, 11)
		tech.unlock_all()


def run_pumpkins():
	while True:
		pumpkins.run_drone(6, 10)


def run_sunflowers():
	flowers = {}
	while True:
		max_petals = sunflowers.run_drone(4, 6, flowers)


def main():
	clear()
	spawn_drone(run_pumpkins)
	util.go_to(10, 0)
	spawn_drone(run_sunflowers)
	util.go_to(0, 6)
	run_maze()

main()
