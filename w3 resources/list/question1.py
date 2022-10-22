#Write a Python function that takes two lists and returns True if 
# they have at least one common member.

def common_item(l1,l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False

print(common_item([2,3,4],[90,5,8]))


