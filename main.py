import random
import multiprocessing

def count_pi(count_point):
    all_point = 0
    point_in_circle = 0

    while all_point < count_point:
        x, y = random.random(), random.random()

        if (pow(x, 2) + pow(y, 2)) < 1:
            point_in_circle += 1
        
        all_point += 1

    return 4 * (point_in_circle / count_point)

def parallel_worker(count_point):
    cpu_count = multiprocessing.cpu_count()
    point_list = []  

    for i in range(cpu_count):
        point_list.append(count_point / cpu_count)

    return point_list

if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        print(pool.map(count_pi, parallel_worker(1000000000)))