from operator import add, mul

with open("data.txt", "r") as input_file:
    intcode = [int(integer) for integer in input_file.read().split(",")]


def run(noun, verb, integers):
    integers[1] = noun
    integers[2] = verb

    i = 0
    while integers[i] != 99:
        op = (add, mul)[integers[i] - 1]
        integers[integers[i + 3]] = op(integers[integers[i + 1]], integers[integers[i + 2]])
        i += 4
    return integers[0]


print(run(12, 2, intcode[:]))  # part 1

for i in range(99):
    for j in range(99):
        if run(i, j, intcode[:]) == 19690720:
            print(100 * i + j)  # part 2
            break
