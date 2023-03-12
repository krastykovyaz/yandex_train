import sys

def get_values(matrix, coordinates):
    # x_min = coordinates[0][0] - 1
    # y_min = coordinates[0][1] - 1
    # x_max = coordinates[0][2] - 1
    # y_max = coordinates[0][3] - 1
    for coordinate in coordinates:
        x_min, y_min, x_max, y_max = tuple(c-1 for c in coordinate)

        prefix_double = 0
        while x_min < x_max + 1:
            y_gain = y_min
            prefix_sum = [matrix[x_min][y_min]]
            while y_gain < y_max + 1:
                if y_gain == y_min + 1:
                    prefix_sum.append(matrix[x_min][y_gain - 1] + matrix[x_min][y_gain])
                y_gain += 1
            print(prefix_sum)
            prefix_double += prefix_sum[-1]
            x_min += 1

        sys.stdout.write(str(prefix_double))
        sys.stdout.write('\n')


if __name__=='__main__':
    m,n,k = tuple(map(int, sys.stdin.readline().split()))
    coordinates, matrix = [], []
    for _ in range(m):
        matrix.append(tuple(map(int, sys.stdin.readline().split())))
    for _ in range(k):
        coordinates.append(tuple(map(int, sys.stdin.readline().split())))
    get_values(matrix, coordinates)