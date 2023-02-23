from typing import List, Union
from collections import defaultdict
def count_time_spaceships(cubes: int, timetable: Union[List[str], List[int]])->List[int]:
    timetable = timetable[1:]
    cube_collector = defaultdict(list)

    for i in range(int(cubes)):
        slice = timetable[i].split()
        op = slice[-1]
        day, hour, minute, cube_id = list(map(int, slice[:-1]))
        if op != 'B':
            hours = day * 24 + hour
            munites = hours * 60 + minute
            event = 0 if op == 'A' else 1
            cube_collector[cube_id].append((munites, event))
    res = []
    for cube in sorted(cube_collector):
        ans = 0
        cube_collector[cube].sort()
        for events in cube_collector[cube]:
            if events[1] == 0:
                start = events[0]
            else:
                ans += events[0] - start
        res.append(ans)
    return res




    pass

if __name__=='__main__':
    string = """8
                50 7 25 3632 A
                14 23 52 212372 S
                15 0 5 3632 C
                14 21 30 212372 A
                50 7 26 3632 C
                14 21 30 3632 A
                14 21 40 212372 B
                14 23 52 3632 B"""
    values = [v.strip() for v in string.split('\n')]
    n = values[0]
    print(*count_time_spaceships(n, values))
