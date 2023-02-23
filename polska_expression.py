import sys
def account(exp: str):
    stack = []
    dig = '0123456789'
    for ch in exp:
        if ch in dig:
            stack.append(int(ch))
        else:
            res = None
            if ch == '+':
                res = stack[-2] + stack[-1]
            elif ch == '-':
                res = stack[-2] - stack[-1]
            elif ch == '*':
                res = stack[-2] * stack[-1]
            elif ch == '/':
                res = stack[-2] / stack[-1]
            stack.pop()
            # if stack:
            stack.pop()
            stack.append(int(res))
    return str(stack[-1])




if __name__=='__main__':
    exp = sys.stdin.readline().split()
    sys.stdout.write(account(exp))