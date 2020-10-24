import numpy as np
class Abelian_Theory_Group(object):
    def __init__(self, l):
        self.l=l
    def Group_Order(self,l=None):
        if l is None:
            l=self.l
        return np.prod(l[0])
    def Group_Generators(self):
        item = 1
        l = []
        a=self.l[0]
        for i in range(len(a)):
            l+=[[]]
            for ind in range(a[i]):
                l[-1].append(item)
                item += 1
        return l