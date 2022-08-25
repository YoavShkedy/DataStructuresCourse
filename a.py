import random


def find(lst, k=1):
    if len(lst) == 1:
        print("\narr length == 1, returning", lst[0])
        return lst[0]

    print("\nk =", k)
    print("Current arr =", lst)
    median = sorted(lst)[(len(lst)-1)//2]
    print("median =", median)
    smallEqual = [x for x in lst if x <= median]
    print("smallEqual =", smallEqual)
    greater = [x for x in lst if x > median]
    print("greater =", greater)
    s = sum(smallEqual)
    print("s =", s)

    if s == k:
        print("s == k: returning", median)
        return median
    elif s > k:
        print("s > k: continuing recursively with smallEqual =", smallEqual, "and k =", k)
        return find(smallEqual, k)
    elif s < k:
        print("s < k: continuing recursively with greater =", greater, "and k =", k - s)
        return find(greater, k - s)


arr = [-6, -3, -2, 0, 1, 4, 10, 12, 17, 25, 30]
random.shuffle(arr)
print("\nres = " + str(find(arr)))
