import sys


# def comboGenerator(arr):
#     length = len(arr)
#     count = 1
#     while count <= length:
#         for i in range(length + 1 - count):
#             yield sum(arr[i:i+count])
#         count += 1

# def calculateProfit(arr):
#     return max(x for x in comboGenerator(arr))

def fibreBrute(arr):
    memory = []
    memory.append([arr.pop(0)])
    for i in arr:
        temp = [i+x for x in memory[-1]]
        temp.append(i)
        memory.append(temp)
    return max([max(x) for x in memory])

line = sys.stdin.readline().rstrip().split()
result = []

while len(line) != 1:
    result.append(fibreBrute([int(x) for x in line]))
    line = sys.stdin.readline().rstrip().split()

sys.stdout.write("\n".join(str(x) for x in result))
