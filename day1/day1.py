import math


def calculate(mass):
    return mass // 3 - 2


def recurse(int_input):
    final = int_input // 3 - 2
    if final <= 0:
        return 0
    return final + recurse(final)


final_answer_part_1 = 0
final_answer_part_2 = 0

with open("data.txt", "r") as file:
    data = file.readlines()

    for line in data:
        final_answer_part_1 += calculate(int(line))
        final_answer_part_2 += recurse(int(line))

    print(final_answer_part_1)
    print(final_answer_part_2)
