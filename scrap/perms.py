def steps_to(stair):
    if stair == 1:
        return 1
    elif stair ==2:
        return 2
    elif stair == 3:
        return 4
    return (steps_to(stair-3) + steps_to(stair-2) + steps_to(stair-1))
from timeit import repeat
setup_code = "from __main__ import steps_to"
stmt = "steps_to(30)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
print(times)
print(f"Minimum execution time: {min(times)}")