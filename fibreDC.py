import sys
import math


# fromSide 0 => left, 1 => right, 2 => side doesn't matter
def searchPathFromSide(arr, fromSide):
    length = len(arr)
    if length == 1:
        return arr[0]
    elif length == 2:
        if fromSide == 1:
            return max(arr[0], arr[0]+arr[1])
        elif fromSide == 0:
            return max(arr[1], arr[0]+arr[1])
        elif fromSide == 2:
            return max(arr[0], arr[1], arr[0]+arr[1])
    else:
        divider = int(math.floor(length/2))
        left = arr[:divider]
        right = arr[divider+1:]
        leftMax = searchPathFromSide(left, 0)
        rightMax = searchPathFromSide(right, 1)
        midValue = arr[divider]
        if fromSide == 1:
            leftSum = sum(left)
            return max(leftSum, leftSum+midValue, leftSum+midValue+rightMax)
        elif fromSide == 0:
            rightSum = sum(right)
            return max(rightSum, midValue+rightSum, leftMax+midValue+rightSum)
        elif fromSide == 2:
            return max(leftMax, leftMax+midValue, rightMax, midValue+rightMax, leftMax+midValue+rightMax)


line = sys.stdin.readline().rstrip().split()
result = []

while len(line) != 1:
    result.append(searchPathFromSide([int(x) for x in line], 2))
    line = sys.stdin.readline().rstrip().split()

print("\n".join(str(x) for x in result))
