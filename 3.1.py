import functools, time
@functools.lru_cache(maxsize=128)
def multiplier(number: int):
    return number * 2

start = time.perf_counter(); multiplier(1); print('Time run:', time.perf_counter() - start)    

