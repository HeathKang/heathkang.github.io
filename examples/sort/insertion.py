"""
插入排序
"""
from base import Comparable, Base


class Insertion(Base):
    def sort(self, a:[Comparable]):
        for i in range(0, len(a)):
            for j in range(i):
                if self.less(a[i], a[j]):
                    self.exch(a, i, j)


def main():
    test_list = [1,4,5,3,14,23,50]
    comparable_list = [Comparable(i) for i in test_list]
    sort_method = Insertion()
    sort_method.sort(comparable_list)
    
    sort_method.show(comparable_list)
    print(sort_method.inSorted(comparable_list))

if __name__ == '__main__':
    main()