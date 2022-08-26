# test=set()

# # test.add("aaa")
# test.add("aaa")
# test.add("aaa")

# test.add("aaaa")
# print(len(test))


# for i in range(10):
#     print(i%3)


# for i in range(3):
#     print(i)


# s="AABA"

# s=s[1:3]
# print(s)

# arr=[1,3,4,5,6,67]
# arr2=arr.copy()

# arr[0]=10
# print(arr)
# print(arr2)


pat = ['a', 'a','a','a']


def allPatterns(candidates):
    if len(candidates) < 3:
        return None
    inds = [0, 1, 2]
    result = []
    for i1 in range(len(candidates)-2):
        for i2 in range(i1+1, len(candidates)-1):
            for i3 in range(i2+1, len(candidates)):
                # print(i1, i2, i3)
                result.append([candidates[i1],candidates[i2],candidates[i3]])
    return result
    


print(allPatterns(pat))
