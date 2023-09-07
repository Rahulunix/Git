Given a string, say S, print it in reverse manner eliminating the repeated characters and spaces?
ans:-

def reverseString(s):
        s = s[::-1]
        ans = ""
        for i in s:
            if i not in ans:
                ans +=i
        return ans.replace(" ","")
print(reverseString("geegs for geegs"))

output :- SKEGROF