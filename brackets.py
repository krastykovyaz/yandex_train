import sys


def is_valid(brackets: str)->bool:
    stack = []
    b_dict = {')': '(', ']': '[', '}': '{'}
    for br in brackets:
        if br in list(b_dict.values()):
            stack.append(br)
        else:
            if stack[-1] == b_dict[br]:
                stack.pop()
            else:
                return False
    return len(stack) == 0



if __name__=='__main__':
    # brackets = '{()([])}'
    brakets = sys.stdin.readline()
    sys.stdout.write('yes' if is_valid(brakets) else 'no')