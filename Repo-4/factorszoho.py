import math
class Element:
    def __init__(self, index, no_of_fact):
        self.index = index
        self.no_of_fact = no_of_fact

def countFactors(n):
    count = 0
    sq = int(math.sqrt(n))

    if sq * sq == n:
        count += 1

    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0 and n/i != i:
            count += 2
    return count

def compare(e1, e2):
    if e1.no_of_fact == e2.no_of_fact:
        return e1.index < e2.index

    return e1.no_of_fact > e2.no_of_fact

def printOnBasisOfFactors(arr):
    n = len(arr)
    num = []

    for i in range(n):
        num.append(Element(i, countFactors(arr[i])))

    num.sort(key=lambda x: (x.no_of_fact, -x.index), reverse=True)

    for i in range(n):
        print(arr[num[i].index], end=" ")

arr = [8, 2, 3, 12, 16]
printOnBasisOfFactors(arr)
