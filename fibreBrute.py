import sys


def comboMofo(arr):
    length = len(arr)
    count = 1
    while count <= length:
        for i in range(length + 1 - count):
            yield sum(arr[i:i+count])
        count += 1


def calculateProfit(arr):
    return max(x for x in comboMofo(arr))


line = sys.stdin.readline().rstrip().split()
result = []

while len(line) != 1:
    result.append(calculateProfit([int(x) for x in line]))
    line = sys.stdin.readline().rstrip().split()

sys.stdout.write("\n".join(str(x) for x in result))
