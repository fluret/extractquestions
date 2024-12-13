perfect_cubes = {x for x in range(1, 101) if int(x**(1/3))**3 == x}
print(perfect_cubes)