import copy
#################### PART 1 ####################################

# read in puzzle input
with open('puzzle_inputs/input1.txt') as f:
    f = f.readline()
path = f.split(',')
path = [x.strip() for x in path]

# define directions in sequence
headings = ('north', 'east', 'south', 'west')

def move_point(point, step):
    """step as in L5, R4 etc"""
    left_right = step[0]
    step_size = int(step[1:])

    if left_right == 'L':
        new_heading = headings[(headings.index(point[2])-1)%4]

    if left_right == 'R':
        new_heading = headings[(headings.index(point[2])+1)%4]

    if new_heading == 'north':
        point[1] += step_size

    if new_heading == 'south':
        point[1] -= step_size

    if new_heading == 'west':
        point[0] += step_size

    if new_heading == 'east':
        point[0] -= step_size

    point[2] = new_heading
    return point


# set initial point (0,0) facing north:
point = [0, 0, 'north']
all_points = []
for step in path:
    point = move_point(point, step)
    all_points.append(copy.deepcopy(point))

print(point)
print('distance = ', abs(point[0]) + abs(point[1]))

#################### PART 2 ############################################
all_points.insert(0, [0, 0])
granular_points = []

# interpolate so step size is 1
for i in range(len(all_points) -1):
    granular_points.append(all_points[i][:2])
    x_distance = all_points[i+1][0] - all_points[i][0]
    y_distance = all_points[i+1][1] - all_points[i][1]
    for x in range(abs(x_distance) -1):
        temp_x = x_distance/abs(x_distance)
        granular_points.append([int(granular_points[-1][0]+temp_x), int(granular_points[-1][1])])
    for y in range(abs(y_distance) -1):
        temp_y = y_distance/abs(y_distance)
        granular_points.append([int(granular_points[-1][0]), int(granular_points[-1][1]+temp_y)])


# append last point to granular points
granular_points.append(point[:2])

# find first point where it occurs twice

for i in range(len(granular_points)):
    for j in range(i+i, len(granular_points)):
        if granular_points[i] == granular_points[j]:
            crossed_point = granular_points[i]
            break

print('Part 2 Distance: ', crossed_point[0]+crossed_point[1])

