import sys
import math


def calculateProfit(arr):
    length = len(arr)
    output = [[-math.inf for x in range(length+1)] for y in range(length+1)]

    for index, item in enumerate(arr):
        output[index][index+1] = item

    for j in range(length+1):
        for k in range(j, length+1):
            for i in range(k+1):
                output[j][k] = max(
                    output[j][k], output[j][i] + output[i][k])

    return max(max(x) for x in output)


dataInput = sys.stdin.read()
data = [[int(y) for y in x.split()] for x in dataInput.split("\n")]

resultBuffer = []
for i in data[:-2]:
    resultBuffer.append(str(calculateProfit(i))+"\n")

sys.stdout.writelines(resultBuffer)
