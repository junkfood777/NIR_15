def h(x):
    part1 = x ^ 1
    part2 = 2 * (x & (1 + 2 * x) & (3 + 4 * x) & (7 + 8 * x) & (15 + 16 * x) & (31 + 32 * x) & (63 + 64 * x))
    part3 = 4 * (x ** 2 + 15)

    return (part1 ^ part2 ^ part3) % 256


Z2 = [0, 1]
h_composition = [h(h(x)) for x in Z2]

print(h_composition)