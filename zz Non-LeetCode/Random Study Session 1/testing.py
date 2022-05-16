# def test1(x):
#     x=x-1
#     print(x)

# test1(3)

class testClass:
    var1=1

    def func1(self):
        print(self.var1)
        print(testClass.var1)
        self.var1=2
        print(self.var1)
        print(testClass.var1)


test=testClass()
test.func1()

# arr=[1,2,3,3,4,5]
# print(range(len(arr)))

# print(arr.index(3))

# for i in range(len(arr)):
    # print(i)
    # print(arr[i])