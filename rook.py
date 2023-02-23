from typing import List, Tuple, Dict

def is_beat(coordinates: List[Tuple[int, int]])->bool:
    def get_dict(hash_, item)->None:
        if item in hash_:
            hash_[item] += 1
        hash_[item] = 1

    def get_pairs(hashrow , hashcol)->int:
        pairs = 0
        for k in hashrow.keys():
            if k in hashcol.keys():
                pairs += min(hashcol[k], hashrow[k])
        return pairs

    hashrow = {}
    hashcol = {}
    for f,s in coordinates:
        get_dict(hashrow, f)
        get_dict(hashcol, s)
    return get_pairs(hashrow, hashcol)



if __name__=='__main__':
    coord = [(2, 1), (4, 5), (6, 7), (2, 6)]
    print(is_beat(coord))
