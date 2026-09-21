from __builtins__ import *
import maze
import pumpkins
import tech
import util

SIZE = get_world_size()
COUNT = maze.get_substance_count()
HATS = (
        Hats.Brown_Hat,
        Hats.Gold_Hat,
        Hats.Green_Hat,
        Hats.Gray_Hat,
        Hats.Purple_Hat,
        Hats.Straw_Hat,
        Hats.Traffic_Cone,
        )

def run_drone(unlock=False):
    y = get_pos_y()
    change_hat(HATS[y % len(HATS)])
    while True:
        pumpkins.run_drone()
        if unlock:
            tech.unlock_all()

def main():
    clear()

    rows = util.get_rows()
    for i in range(max_drones() - 1):
        spawn_drone(run_drone)
        for y in range(rows):
            move(North)
    run_drone(True)

main()
