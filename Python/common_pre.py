
def longestCommonPrefix(arr):
    
    arr.sort()
    result = ""
    for x, y in zip(arr[0], arr[-1]):
        if x == y: p+=x
        else: break
    return result

print(longestCommonPrefix(["pie", "pig"]))
