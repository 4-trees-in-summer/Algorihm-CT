def solution(s):
    answer = True
    stack = []
    
    for i in s :
        if i == '(' :
            stack.append(i)
        else :
            if not stack :
                return False
            elif stack[-1] == '(' :
                stack.pop()
    if stack :
        return False
    else :
        return True