from concurrent.futures import ProcessPoolExecutor
import time


def sleeper(id_):
    print(f'{id_} started' )
    time.sleep(2)
    print(f'{id_} ended')

pool = ProcessPoolExecutor(max_workers=5)

futures = []

for i in range(1, 13, 1):
    f = pool.submit(sleeper, i)
    futures.append(f)

for i in futures:
    i.result()