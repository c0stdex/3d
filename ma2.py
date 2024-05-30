import time
from multiprocessing import Pool, cpu_count

def factorize_sync(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_range(start, end, number):
    factors = []
    for i in range(start, end):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(number):
    num_cores = cpu_count()
    chunk_size = number // num_cores
    with Pool(processes=num_cores) as pool:
        results = pool.starmap(factorize_range, [(i, i + chunk_size, number) for i in range(1, number, chunk_size)])

    factors = []
    for result in results:
        factors.extend(result)
    return factors

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

