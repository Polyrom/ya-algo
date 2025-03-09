import sys

print(f"{sys.getsizeof(42) = } bytes for a small int")
print(f"{sys.getsizeof([]) = } bytes for an empty list")
print(f"{sys.getsizeof([42]) = } bytes (+8 bytes for each pointer)")
print(f"{sys.getsizeof([42, 12, 8]) = } bytes (+8 bytes for each pointer + an empty slot for a new elem beforehand)")
print(f"{sys.getsizeof([42, 12, 8, 9]) = } bytes (equal to a list with 3 elems) -> total 28 * 4 + 88 = 200 bytes")
