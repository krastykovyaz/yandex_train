def num_f(n):
    if n == 1 or n == 0:
        return 1
    return num_f(n - 1) + num_f(n - 2)

if __name__=='__main__':
    n = 3
    print(num_f(n))