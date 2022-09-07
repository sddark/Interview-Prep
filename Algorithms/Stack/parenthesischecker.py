def ispar(x):
    # code here
    stack = []
    for i in x:
        if i == '}':
            if len(stack) == 0:
                return False
            temp = stack.pop()
            if temp != '{':
                return False
        elif i == ']':
            if len(stack) == 0:
                return False
            temp = stack.pop()
            if temp != '[':
                return False
        elif i == ')':
            if len(stack) == 0:
                return False
            temp = stack.pop()
            if temp != '(':
                return False
                
        else: stack.append(i)
    
    if len(stack) > 0:
        return False
    else:
        return True

print(ispar([ '[', ']','{', '}','(', ')',]))