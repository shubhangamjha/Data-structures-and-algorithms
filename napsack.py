class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost

def getMaxValue(wt, val, capacity):
    iVal = []
    for i in range(len(wt)):
        iVal.append(ItemValue(wt[i], val[i], i))

    iVal.sort(reverse=True)

    totalValue = 0
    for i in iVal:
        curWt = int(i.wt)
        curVal = int(i.val)
        if capacity - curWt >= 0:
            capacity -= curWt
            totalValue += curVal
        else:
            fraction = capacity / curWt
            totalValue += curVal * fraction
            capacity = int(capacity - (curWt * fraction))
            break
    return totalValue

n = int(input("Enter the number of items: "))
wt = list(map(int, input("Enter the weights of the items: ").split()))
val = list(map(int, input("Enter the values of the items: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

maxValue = getMaxValue(wt, val, capacity)
print("Maximum value in Knapsack =", maxValue)
