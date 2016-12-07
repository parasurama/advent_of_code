import pandas as pd

df = pd.read_csv('puzzle_inputs/input3.txt', delimiter='\s+', header=None)
triangles = list(df.to_records(index=False))


def check_triangle(lengths):
    if (lengths[0] + lengths[1]) > lengths[2] and (lengths[0] + lengths[2]) > lengths[1] \
            and (lengths[1] + lengths[2]) > lengths[0]:
        return True
    else:
        return False


def get_num_triangles(list_of_sides):
    triangle_results = []
    for item in list_of_sides:
        triangle_results.append(check_triangle(item))
    return triangle_results.count(True)
print(get_num_triangles(triangles))

#################################### PART 2 ################################################

flat_list = list(pd.concat([df[0], df[1], df[2]]))
new_triangles = [flat_list[x:x+3] for x in range(0, len(flat_list), 3)]

print(get_num_triangles(new_triangles))


