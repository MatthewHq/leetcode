class fraudCheck:

    def __init__(self, expenditure, d):
        self.expenditure = expenditure
        self.d = d
        if len(expenditure) != 0:
            self.iter = d
            self.sortedTrail = sorted(self.self.expenditure[0:d])

    def insertionSort(self):
        self.iter += 1
        self.sortedTrail = sorted(self.expenditure[self.iter-self.d:self.iter])

    def getMedian(self):
        i = len(self.sortedTrail)
        if i % 2 == 1:
            med = self.sortedTrail[int(i/2)]
        else:
            med = (self.sortedTrail[int(i/2)] +
                   self.sortedTrail[int(i/2)-1])/2
        return med

    def notifCount(self):
        if len(self.expenditure) == 0:
            return 0
        count = 0
        for i in range(self.d, len(self.expenditure)):
            med = self.getMedian()
            if self.expenditure[self.iter] >= 2*med:
                count += 1
            
            if i != len(self.expenditure)-1:
                self.insertionSort()
        return count


def activityNotifications(expenditure, d):
    # Write your code here
    fraudNotif = fraudCheck(expenditure, d)
    return fraudNotif.notifCount()