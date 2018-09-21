import sys
import math


def crossingFibreDC(arr, low, mid, high):
    total = 0
    leftTotal = -math.inf
    rightTotal = -math.inf
    for i in range(mid, low-1, -1):
        total += arr[i]
        if total > leftTotal:
            leftTotal = total

    total = 0
    for i in range(mid+1, high+1):
        total += arr[i]
        if total > rightTotal:
            rightTotal = total

    return leftTotal + rightTotal


def fibreDC(arr, low, high):
    if low == high:
        return arr[low]
    else:
        mid = (low+high) // 2
        return max(fibreDC(arr, low, mid), fibreDC(arr, mid+1, high), crossingFibreDC(arr, low, mid, high))


line = sys.stdin.readline().rstrip().split()
result = []

while len(line) != 1:
    inputArr = [int(x) for x in line]
    result.append(fibreDC(inputArr, 0, len(inputArr)-1))
    line = sys.stdin.readline().rstrip().split()

sys.stdout.write("\n".join(str(x) for x in result))
