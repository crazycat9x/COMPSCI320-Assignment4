import sys
import math
import time

def fibreDP(arr):
    result = -math.inf
    results = []
    for i in arr:
        result = max(i, i+result)
        results.append(result)
    return max(results)

line = sys.stdin.readline().rstrip().split()
result = []

while len(line) != 1:
    result.append(fibreDP([int(x) for x in line]))
    line = sys.stdin.readline().rstrip().split()

sys.stdout.write("\n".join(str(x) for x in result))
