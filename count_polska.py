def count_polska(expression: str)->int:
    stack = []
    dig = '0123456789'
    for val in expression:
        if val in dig:
            stack.append(int(val))
        else:
            if val == '*':
                res = stack[-1] * stack[-2]
            elif val == '+':
                res = stack[-1] + stack[-2]
            elif val == '/':
                res = stack[-1] / stack[-2]
            elif val == '-':
                res = stack[-1] - stack[-2]
            stack.pop()
            stack[-1] = res
    return stack[-1]


if __name__=='__main__':
    exp = '63145*+*2*+'
    print(count_polska(exp))