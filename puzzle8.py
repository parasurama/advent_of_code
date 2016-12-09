import numpy as np
import seaborn as sns

with open('puzzle_inputs/input8.txt') as f:
    instructions = f.readlines()
    instructions = [x.split() for x in instructions]

class Screen:
    def __init__(self):
        self.grid = np.zeros([6, 50])

    def create_rectangle(self, cols, rows):
        self.grid[0:rows,0:cols] = 1

    def rotate(self, axis, index, shift):
        if axis == 'x':
            self.grid[:, index] = np.roll(self.grid[:, index], shift)
        if axis == 'y':
            self.grid[index, :] = np.roll(self.grid[index, :], shift)

dank_screen = Screen()

for line in instructions:
    if line[0] == 'rect':
        dims = line[1].split('x')
        dank_screen.create_rectangle(int(dims[0]), int(dims[1]))
    if line[0] == 'rotate':
        axis = line[2].split('=')[0]
        index = line[2].split('=')[1]
        shift = line[4]
        dank_screen.rotate(axis, int(index), int(shift))

print(dank_screen.grid.sum())

sns.heatmap(dank_screen.grid)
