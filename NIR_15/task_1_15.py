def f(x):
    return (1 + 1 * x + 1 * (x ** 2)) % 2

def g(x):
    return (1 * x + 0) % 2

results_f = {x: f(x) for x in [0, 1]}
results_g = {x: g(x) for x in [0, 1]}

results_fg = {x: f(g(x)) for x in [0, 1]}
results_gf = {x: g(f(x)) for x in [0, 1]}

print(results_f, results_g, results_fg, results_gf)
