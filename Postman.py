import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

dots= [(0, 2),(2, 5), (5, 2), (6, 6), (8, 3)]
lendots = len(dots)

def distance(point_1, point_2):
    return np.sqrt((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2)

distances = np.empty([lendots, lendots])
for i in range(lendots):
    for j in range(lendots):
        distances[i,j] = distance(dots[i],dots[j])
        
path, distance=solve_tsp_dynamic_programming(distances)
path.append(0)
print(path,distance)

answer = f"{dots[0]}"
length = 0
for i,v in enumerate(path[1:]):
    length += distances[path[i], path[i+1]]
    answer += f" -> {dots[v]} [{length}]"
answer += f" = {length}"
print(answer)