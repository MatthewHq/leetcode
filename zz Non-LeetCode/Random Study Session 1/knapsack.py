
class KS:

    def __init__(self, capacity, sizes, values):
        self.capacity = capacity
        self.sizes = sizes
        self.values = values
        self.dynMap = [[] for i in range(2)]
        self.denomMultipliers = {}

    def getValue(self):
        # valPerWeight = []

        # for i in range(len(sizes)):
        #     valPerWeight.append(values[i]/sizes[i])
        # print(valPerWeight)

        for cap in range(1, self.capacity+1):
            for denom in range(len(self.sizes)):
                if cap/self.sizes[denom] >= 1:
                    print("cap: {} | {} / {}: {} and final value {}".format(
                        cap, cap, self.sizes[denom], int(cap/self.sizes[denom]),self.calculateLocalVal(
                        cap, denom, int(cap/self.sizes[denom]))))
        print(self.denomMultipliers)
                    

    def calculateLocalVal(self, currentCap, denom, multiplier):
        currVal = self.values[denom]*multiplier
        localValues = {}
        localValues[denom] = multiplier
        self.denomMultipliers[currentCap] = localValues
        currentCap -= self.sizes[denom]*multiplier
        print("{} remains with value of {}".format(currentCap, currVal))
        if self.denomMultipliers.get(currentCap) != None:
            for key in self.denomMultipliers[currentCap].keys():
                currVal += self.values[key]*self.denomMultipliers[currentCap][key]
                print("Added {}".format(self.values[key]*self.denomMultipliers[currentCap][key]))

        

        # remaining=currentCap
        return currVal

        # help('FORMATTING')


capacity = 25
size = [22, 10, 9, 7]
value = [19, 9, 9, 6]
ks = KS(capacity, size, value)
ks.getValue()


# r = {6: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# y={}
# for item in sorted(r.items()):
#     y[item[0]]=item[1]
# print(y)


# print(r)
# print(y)
# print((r.items()))
# print(sorted(r.items(), key=lambda q: q[1]))
# print(sorted(r.items(), key=lambda x: x[0]))
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}

# test = [[0 for x in range(10)]for y in range(20)]
# print(len(test))
# print(len(test[0]))
