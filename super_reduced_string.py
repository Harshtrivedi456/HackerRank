def superReducedString(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    result = ''.join(stack)
    return result if result else "Empty String"

# Sample inputs
print(superReducedString(input()))    # Empty String
# print(superReducedString("baab"))  # Empty String
# print(superReducedString("abc"))   # abc
