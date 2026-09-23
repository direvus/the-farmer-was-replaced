from __builtins__ import *
import maze
import pumpkins
import tech
import util

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


def main():
	clear()
    spawn_drone(run_pumpkins)
    for y in range(6):
        move(North)
	run_maze()

main()
