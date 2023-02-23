def form_polska(expression: str)->str:
    dig = '0123456789'
    stack = []
    polska = []
    for c in expression:
        if c not in dig:
            if c in '*/' and stack[-1] in '*/':
                polska.append(c)
                continue
            if len(stack) > 1 and (c == '+' or c == '-') and (stack[-1] == '*' or stack[-1] == '/')\
                    or c == ')':
                i = 0
                while i < len(stack) and stack[i] != '(':
                    polska.append(stack[-1])
                    stack.pop()
                    i += 1
                stack.pop()
                if c != ')':
                    stack.append(c)
            else:
                stack.append(c)
        else:
            polska.append(c)
    return polska + stack[::-1]




if __name__=='__main__':
    expression = '6+3*(1+4*5)*2'
    print(form_polska(expression))