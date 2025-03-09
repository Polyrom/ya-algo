# read two inputs on new lines and cast to int
a = int(input())
b = int(input())

# read two inputs separated by whitespace and cast to int
a, b = map(int, input().split())

# read an array
# usually, an array is defined with its length in first input
# and elements of the array in second input separated by whitespace
n = int(input())
arr = list(map(int, input().split()))

print(" ".join(list(map(str, arr))))
