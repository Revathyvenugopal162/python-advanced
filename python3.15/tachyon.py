# high frequency statistical sampling profiler
"""Added as a profiling.sampling profiler

unlike deterministic profiler, sampling periodically captures traces from running processes."""

# compare_profilers.py

import math
import multiprocessing

def count_primes(start: int, end: int) -> int:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(1 for i in range(start, end) if is_prime(i))

def heavy_math():
    total = 0

    for i in range(20_000_000):
        total += math.sqrt(i)

    return total


def string_work():
    items = []

    for i in range(500_000):
        items.append(str(i))

    return len(items)

def multiprocess_count_primes(n: int, num_processes: int) -> int:
    with multiprocessing.Pool(processes=num_processes) as pool:
        step = n // num_processes
        tasks = [
            (i * step, (i + 1) * step if i != num_processes - 1 else n)
            for i in range(num_processes)
        ]
        results = [pool.apply_async(count_primes, args=task) for task in tasks]
        return sum([result.get() for result in results])


def main():
    heavy_math()
    string_work()
    multiprocess_count_primes(10_000, 4)


if __name__ == "__main__":
    main()
    
# no profiler - time python tachyon.py
# cprofiler - python -m cProfile tachyon.py
# python3.15 -m profiling.sampling run --heatmap --browser tachyon.py 
#python -m profiling.sampling run --flamegraph -o profile.html tachyon.py
# python3.15 -m cProfile -o cprofile.pstats tachyon.py