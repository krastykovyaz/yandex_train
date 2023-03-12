import sys
from typing import List
def time_server(times: List[str])->str:
    def to_sec(string):
        hh, mm, ss = list(map(int, string.split(':')))
        mm += (hh * 60)
        ss += (mm * 60)
        return ss
    def to_clock(ss):
        mm = ss // 60
        ss %= 60
        hh = mm // 60
        mm %= 60
        f = lambda x: '0' + str(int(x)) if len(str(int(x))) == 1 else int(x)
        return f"{f(hh)}:{f(mm)}:{f(ss)}"
    A, B, C = [to_sec(t) for t in times]
    diff = C - A
    client_server = 0.5 * diff if diff % 2 == 0 else (0.5 * diff) + 0.5
    server_client = client_server + B
    return to_clock(server_client)


if __name__=='__main__':
    times = []
    for _ in range(3):
        times.append(sys.stdin.readline())
    print(time_server(times))