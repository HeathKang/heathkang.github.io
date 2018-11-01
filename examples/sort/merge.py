"""
归并排序
"""
from base import Comparable, Base
from copy import deepcopy

class Merge(Base):
    def sort(self, a:[Comparable]):
        self.sort_individual(a, 0, len(a))

    def sort_individual(self, a:[Comparable], lo:int, hi:int):
        print("lo:{}".format(lo))
        print("hi:{}".format(hi))
        # 到极限情况
        if lo >= hi - 1:
            return

        mid = (hi - lo)//2 + lo
        self.sort_individual(a, lo, mid)
        self.sort_individual(a, mid, hi)
        self.merge(a, lo, hi, mid)

    def merge(self, a:[Comparable], lo:int, hi: int, mid: int):
        """
        归并 a[lo:mid] 和 a[mid: hi]
        """
        a_low:[Comparable] = deepcopy(a[lo:mid]) # 额外的空间
        a_high:[Comparable] = deepcopy(a[mid:hi]) # 额外的空间

        for i in range(lo,hi):
            if a_low and a_high: # 当a_low 和 a_high都非空时
                if self.less(a_high[0], a_low[0]):
                    a[i] = a_high[0]
                    a_high.pop(0)
                else:
                    a[i] = a_low[0]
                    a_low.pop(0)
            
            elif a_low: # 当a_high为空时
                a[i] = a_low[0]
                a_low.pop(0)
            
            elif a_high: # 当 a_low 为空时
                a[i] = a_high[0]
                a_high.pop(0)


def main():
    test_list = [1,4,5,3,14,23,50,3,100,201,22,21]
    comparable_list = [Comparable(i) for i in test_list]
    sort_method = Merge()
    sort_method.sort(comparable_list)
    
    sort_method.show(comparable_list)
    print(sort_method.inSorted(comparable_list))

if __name__ == '__main__':
    main()