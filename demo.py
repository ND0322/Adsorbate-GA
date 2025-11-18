from multiprocessing import Pool
import time, os

def check(x):
    time.sleep(1)
    return os.getpid()

if __name__ == '__main__':
    with Pool(os.cpu_count()) as pool:
        t0 = time.time()
        pids = pool.map(check, range(8))
        print("Time:", time.time() - t0)
        print("Processes:", set(pids))
