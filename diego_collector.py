from typing import List
def get_sticker(diego: List[int], collectors: List[int])->None:
    def is_in(diego_l: List[int], target: int)->int:
        save = []
        count = 0
        i = 0
        while i < len(diego_l) and diego_l[i] < target:
            if diego_l[i] not in save:
                save.append(diego_l[i])
                count += 1
            i += 1
        return count
    for col in collectors:
        print(is_in(diego, col))


if __name__=='__main__':
    inpt = '''1
5
2
4 6
'''

    inpt = inpt.split('\n')
    # diego = int(inpt[0])
    # inpt = [input() for _ in range(4)]
    diego_list = list(map(int, inpt[1].split()))
    # collectors = int(inpt[2])
    collectors_list = list(map(int, inpt[3].split()))
    get_sticker(sorted(diego_list),collectors_list)