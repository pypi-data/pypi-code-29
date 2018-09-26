## testing the global package
import fmga

## testing the local package
from function_maximize import maximize, unpack

def res():
    best_point = maximize(f, dimensions=4, mutation_probability=0.2, population_size=60, multiprocessing=True,
                          iterations=15)
    return best_point


if __name__ == '__main__':
    def f(*args):
        x, y, z = unpack(args, [1, 1, 2])
        print(args, x.shape, y.shape, z.shape)
        return x - y + z[0]

    best_point = res()
    print(best_point.coordinates, best_point.fitness)

