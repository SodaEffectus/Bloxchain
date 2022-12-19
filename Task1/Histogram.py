import time
import random

gist = [0] * 10
n = 1000000
time_work = [0] * 100


def main():
    for i in range(100):
        a = initListWithRandomNumbers()
        start_time = time.time_ns()
        calcSumm(a)
        end_time = time.time_ns()
        time_work[i] = end_time - start_time
    time_work.sort()
    print("Runtime of the calcSumm is ", time_work[49])
    print(gist)


def initListWithRandomNumbers():
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(0, 999))
    return rand_list


def calcSumm(arr):
    i = 0
    for i in range(n):
        gist[int(arr[i] / 100)] = gist[(arr[i] // 100)] + 1
    return gist


main()
