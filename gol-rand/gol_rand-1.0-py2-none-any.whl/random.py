from gol_rand.grid_utils import (
    get_new_grid,
    populate_grid,
    get_random_number_from_grid
)
import time


default_seed = str(int(round(time.time() * 1000))) +\
    "abcdefghijklmnopqrstuvwxyz"


def get_random_number(
    seed=default_seed,
    grid_width=16,
    gof_intervals=1,
    create_images=False
):
    grid = get_new_grid(size=grid_width)
    grid = populate_grid(grid=grid, seed=seed)

    number = get_random_number_from_grid(
        grid, times=gof_intervals, create_images=create_images)

    return number
