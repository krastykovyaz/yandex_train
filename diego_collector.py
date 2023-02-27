from typing import List
def get_sticker(diego: List[int], collectors: List[int])->None:
    res = []
    if len(diego) == 1:
        for coll in collectors:
            if coll > diego[0]:
                print(1)
            else:
                print(0)
    else:
        for coll in collectors:
            sorted_lst_orig = sorted(diego)
            dig = set()
            diego = [d for d in diego if d not in dig and not dig.add(d)]
            def looking(sorted_lst: List[int], item: int, idx: int) -> List[int]:
                if sorted_lst and sorted_lst[-1] < item:
                    return idx
                elif len(sorted_lst) == 0:
                    return 0
                mid = len(sorted_lst) // 2
                if item < sorted_lst[mid]:
                    return looking(sorted_lst[:mid], item, idx - mid)
                else:
                    return looking(sorted_lst[mid:], item, idx + mid - 1)
            print(looking(sorted_lst_orig, coll, len(sorted_lst_orig)))





if __name__=='__main__':
    inpt = '''3
100 1 50
3
300 0 75
'''

    inpt = inpt.split('\n')
    diego = int(inpt[0])
    inpt = [input() for _ in range(4)]
    diego_list = list(map(int, inpt[1].split()))
    collectors = int(inpt[2])
    collectors_list = list(map(int, inpt[3].split()))
    get_sticker(sorted(diego_list),collectors_list)