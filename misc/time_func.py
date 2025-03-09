import time

start = time.perf_counter()
i = 0
while i < 1_000_000_000:
    i += 1

print(f"{time.perf_counter() - start:.2f} sec")
