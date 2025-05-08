import random

def count_pi(count_point):
    all_point = 0
    point_in_circle = 0

    while all_point < count_point:
        x, y = random.random(), random.random()

        if (pow(x, 2) + pow(y, 2)) < 1:
            point_in_circle += 1
        
        all_point += 1

    return 4 * (point_in_circle / count_point)

print(count_pi(1000000000))