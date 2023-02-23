def get_spot(students: int, tasks: int, row: int, spot: int)->(str, str):
    places = 2
    f1 = lambda x, y, z: (((x - y % 2) * places) + z) // 2
    f2 = lambda x, y, z: (((x - y % 2) * places) + z) % 2
    petya_row = f1(row, spot, tasks)
    petya_spot = f2(row, spot, tasks)
    if petya_spot:
        petya_row += 1
    else:
        petya_spot += 2
    return f'{petya_row} {petya_spot}' if petya_row * 2 + petya_spot < students else -1


if __name__=='__main__':
    students, tasks, row, spot = (int(input()) for _ in range(4))
    print(get_spot(students, tasks, row, spot))
