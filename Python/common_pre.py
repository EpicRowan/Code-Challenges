
def longestCommonPrefix(arr):
    result = ""
    for x,y in zip(arr[0], arr[-1]):
        if x == y:
            result += x
        else:
            break
    return result

print(longestCommonPrefix(["pie", "pig", "pit"]))



