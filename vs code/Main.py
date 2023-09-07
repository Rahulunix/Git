
def IsPalindrome(p):
    str = []

    for i in p.lower():
        if i.isalnum():
            str.append(i)

    if str == str[::-1]:
        return True
    else:
        return False

print(IsPalindrome("trty"))