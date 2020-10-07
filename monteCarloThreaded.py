import random
import math
import time
from multiprocessing import Process, Queue

def buildPoint ():
    nx = random.uniform(-1, 1)
    ny = random.uniform(-1, 1)
    return pow(nx,2) + pow(ny,2) <= 0.25

def runNPoints (n, q):
    q.put(sum(buildPoint() for x in range(n)))

if __name__ == "__main__":
    n = 10000000

    start = time.time()
    q = Queue()

    nJobs = 10
    jobs = []

    for i in range(nJobs):
        p = Process(target=runNPoints, args=(math.floor(n / nJobs), q))
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()

    totalSum = 0
    while not q.empty():
        totalSum += q.get()

    end = time.time()
    print(end - start)

    print ("N", n)
    print ("In Circle", totalSum)
    print ("PI", 16 * (totalSum / n))
